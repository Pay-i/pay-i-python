"""Ingest retry manager for the Pay-i instrumentation layer.

Handles inline retry with exponential backoff and a background retry queue
for failed ingest calls.  Extracted from ``instrument.py`` so the
``_PayiInstrumentor`` class stays focused on instrumentation orchestration.
"""
from __future__ import annotations

import copy
import time
import atexit
import random
import asyncio
import logging
import threading
from typing import TYPE_CHECKING, Any, Union, Callable, Optional, Awaitable
from collections import deque

import httpx
import httpcore

from payi import APIStatusError, APIConnectionError
from payi.types import IngestUnitsParams
from payi.types.ingest_response import IngestResponse

if TYPE_CHECKING:
    from .instrument import PayiInstrumentIngestRetryConfig

# ---------------------------------------------------------------------------
# Retry defaults
# ---------------------------------------------------------------------------

# Inline-retry defaults for ingest calls at the instrumentation layer.
# These retries are on top of the SDK's built-in retries (DEFAULT_MAX_RETRIES=2).
# When httpx connection pools contain stale connections (common behind Azure App Gateway
# or other reverse proxies), the SDK's retries may all hit stale connections from the
# same pool. The instrumentation-layer retry gives the pool time to evict dead connections,
# so subsequent attempts are more likely to get a fresh connection.
# Callers can override via PayiInstrumentConfig keys ingest_max_retries / ingest_retry_initial_delay.
_INGEST_MAX_RETRIES_DEFAULT = 0  # 2
_INGEST_RETRY_INITIAL_DELAY_DEFAULT = 0.5  # seconds, doubles on each retry

# Transport-level exceptions that indicate a stale or broken pooled connection.
# Only these warrant an instrumentation-layer retry — other APIConnectionError causes
# (e.g. DNS resolution failure, TLS certificate errors) should not be retried here.
_RETRYABLE_CONNECTION_EXCEPTIONS = (
    httpx.TimeoutException,
    httpx.ReadError,
    httpx.WriteError,
    httpx.RemoteProtocolError,
    httpx.ConnectError,

    httpcore.TimeoutException,
    httpcore.ReadError,
    httpcore.WriteError,
    httpcore.RemoteProtocolError,
    httpcore.ConnectError,

    ConnectionResetError,
)

# Retry-queue defaults for background re-delivery of failed ingest calls.
_RETRY_QUEUE_MAX_SIZE_DEFAULT = 0          # 0 = unlimited (queue.Queue convention)
_RETRY_QUEUE_WORKER_INTERVAL_DEFAULT = 5.0  # seconds between drain cycles
_RETRY_QUEUE_WORKER_JITTER = 0.5           # +/- seconds applied to each sleep
_RETRY_QUEUE_DRAIN_TIMEOUT = 10.0          # seconds to wait for final drain on shutdown
_RETRY_QUEUE_BATCH_WINDOW = 2.0            # seconds to keep sending within a single drain cycle


# ---------------------------------------------------------------------------
# Helper used by both the manager and callers in instrument.py
# ---------------------------------------------------------------------------

def _qualified_exception_name(exc: BaseException | None) -> str:
    if exc is None:
        return "None"
    exc_type = type(exc)
    return f"{exc_type.__module__}.{exc_type.__qualname__}"


def is_retryable_connection_error(e: Union[APIConnectionError, APIStatusError]) -> bool:
    """Check whether an error is retryable at the instrumentation layer.

    Returns True for transport-level APIConnectionErrors (stale pooled
    connections) and for 504 Gateway Timeout APIStatusErrors (App Gateway
    upstream timeout — functionally equivalent to a stale connection).
    """
    if isinstance(e, APIStatusError):
        return e.status_code == 504
    cause = e.__cause__
    return isinstance(cause, _RETRYABLE_CONNECTION_EXCEPTIONS)


# ---------------------------------------------------------------------------
# Queue item
# ---------------------------------------------------------------------------

class _RetryQueueItem:
    """An ingest call that exhausted immediate retries and is awaiting background retry."""
    __slots__ = ('ingest_units', 'extra_headers', 'retry_count')

    def __init__(self, ingest_units: IngestUnitsParams, extra_headers: 'dict[str, str]') -> None:
        self.ingest_units = ingest_units
        self.extra_headers = extra_headers
        self.retry_count = 0


# ---------------------------------------------------------------------------
# Callable type aliases for dependency injection
# ---------------------------------------------------------------------------

SyncIngestFn = Callable[..., IngestResponse]
AsyncIngestFn = Callable[..., Awaitable[IngestResponse]]
OnSuccessFn = Callable[[IngestResponse], Any]
OnConnectionErrorFn = Callable[[APIConnectionError, IngestUnitsParams], Any]
OnApiStatusErrorFn = Callable[[APIStatusError], Any]


# ---------------------------------------------------------------------------
# IngestRetryManager
# ---------------------------------------------------------------------------

class IngestRetryManager:
    """Manages inline retry and background retry queue for failed ingest calls.

    All Pay-i / AsyncPayi client dependencies are injected as callables so this
    class has no direct reference to the client objects.
    """

    def __init__(
        self,
        *,
        sync_ingest_fn: Optional[SyncIngestFn] = None,
        async_ingest_fn: Optional[AsyncIngestFn] = None,
        on_success: OnSuccessFn,
        on_connection_error: OnConnectionErrorFn,
        on_api_status_error: OnApiStatusErrorFn,
        config: PayiInstrumentIngestRetryConfig,
        logger: Optional[logging.Logger] = None,
    ):
        self._logger: logging.Logger = logger if logger else logging.getLogger("payi.instrument")
        self._retry_logger: logging.Logger = self._logger.getChild("retry")

        self._sync_ingest_fn = sync_ingest_fn
        self._async_ingest_fn = async_ingest_fn
        self._on_success = on_success
        self._on_connection_error = on_connection_error
        self._on_api_status_error = on_api_status_error

        # --- Inline retry config ---
        ingest_max_retries = config.get("max_inline_retries", None)
        ingest_max_retries = ingest_max_retries if ingest_max_retries is not None else _INGEST_MAX_RETRIES_DEFAULT
        self._ingest_max_retries: int = ingest_max_retries
        if self._ingest_max_retries < 0:
            raise ValueError("ingest_max_retries must be a non-negative integer")

        ingest_initial_delay = config.get("inline_retry_initial_delay", None)
        ingest_initial_delay = ingest_initial_delay if ingest_initial_delay is not None else _INGEST_RETRY_INITIAL_DELAY_DEFAULT
        self._ingest_retry_initial_delay: float = ingest_initial_delay
        if self._ingest_retry_initial_delay < 0:
            raise ValueError("ingest_retry_initial_delay must be a non-negative number")

        # --- Retry queue for background re-delivery of failed ingest calls ---
        queue_enabled = config.get("queue_enabled", None)
        self._ingest_retry_queue_enabled: bool = queue_enabled if queue_enabled is not None else True

        if self._ingest_retry_queue_enabled:
            queue_max_size = config.get("queue_max_size", None)
            self._retry_queue_max_size: int = queue_max_size if queue_max_size is not None else _RETRY_QUEUE_MAX_SIZE_DEFAULT
            if self._retry_queue_max_size < 0:
                raise ValueError("queue_max_size must be a non-negative integer")

            queue_interval = config.get("queue_interval", None)
            self._retry_queue_interval: float = queue_interval if queue_interval is not None else _RETRY_QUEUE_WORKER_INTERVAL_DEFAULT
            if self._retry_queue_interval <= 0:
                raise ValueError("queue_interval must be a positive number")

            self._retry_queue: deque[_RetryQueueItem] = deque()
            self._retry_queue_lock: threading.Lock = threading.Lock()
            self._retry_queue_worker_thread: Optional[threading.Thread] = None
            self._retry_queue_shutdown: threading.Event = threading.Event()
            self._retry_queue_started_lock: threading.Lock = threading.Lock()

    # ------------------------------------------------------------------
    # Inline retry (sync / async)
    # ------------------------------------------------------------------

    def ingest_with_inline_retry(
        self,
        ingest_units: IngestUnitsParams,
        extra_headers: 'dict[str, str]',
        no_retry: bool = False,
    ) -> IngestResponse:
        """Call sync ingest.units() with retry on transport-level connection errors.

        When the httpx connection pool contains stale connections (e.g. closed by an Azure App
        Gateway idle timeout), the SDK's built-in retries may all draw from the same poisoned
        pool.  This outer retry gives the pool time to evict dead connections between attempts.

        Retries on known transport errors (ReadError, WriteError, RemoteProtocolError,
        ConnectError, ConnectionResetError) and on 504 Gateway Timeout.  Other errors
        are raised immediately.
        """
        max_retries = self._ingest_max_retries if not no_retry else 0
        last_error: Optional[Union[APIConnectionError, APIStatusError]] = None

        for attempt in range(1 + max_retries):
            try:
                return self._sync_ingest_fn(**ingest_units, extra_headers=extra_headers)  # type: ignore[misc]
            except (APIConnectionError, APIStatusError) as e:
                if not is_retryable_connection_error(e):
                    raise
                last_error = e
                if attempt < max_retries:
                    delay = self._ingest_retry_initial_delay * (2 ** attempt)
                    self._retry_logger.warning(
                        f"Pay-i ingest retryable error (attempt {attempt + 1}/{1 + max_retries}), "
                        f"retrying in {delay:.1f}s: {_qualified_exception_name(e.__cause__) if e.__cause__ else e}"
                    )
                    time.sleep(delay)
                    continue
                raise

        raise last_error  # type: ignore[misc]

    async def aingest_with_inline_retry(
        self,
        ingest_units: IngestUnitsParams,
        extra_headers: 'dict[str, str]',
        no_retry: bool = False,
    ) -> IngestResponse:
        """Async variant of ingest_with_inline_retry."""
        max_retries = self._ingest_max_retries if not no_retry else 0
        last_error: Optional[Union[APIConnectionError, APIStatusError]] = None

        for attempt in range(1 + max_retries):
            try:
                return await self._async_ingest_fn(**ingest_units, extra_headers=extra_headers)  # type: ignore[misc]
            except (APIConnectionError, APIStatusError) as e:
                if not is_retryable_connection_error(e):
                    raise
                last_error = e
                if attempt < max_retries:
                    delay = self._ingest_retry_initial_delay * (2 ** attempt)
                    self._retry_logger.warning(
                        f"Pay-i ingest retryable error (attempt {attempt + 1}/{1 + max_retries}), "
                        f"retrying in {delay:.1f}s: {_qualified_exception_name(e.__cause__) if e.__cause__ else e}"
                    )
                    await asyncio.sleep(delay)
                    continue
                raise

        raise last_error  # type: ignore[misc]

    # ------------------------------------------------------------------
    # Background retry queue
    # ------------------------------------------------------------------

    def enqueue_failed_ingest(
        self,
        ingest_units: IngestUnitsParams,
        extra_headers: 'dict[str, str]',
        api_ex: Union[APIConnectionError, APIStatusError],
    ) -> bool:
        """Enqueue a failed ingest call for background retry.

        Returns True if the item was enqueued, False if the queue is full.
        Deep-copies ingest_units to prevent mutation by the caller after enqueue.
        """
        if not self._ingest_retry_queue_enabled:
            return False

        item = _RetryQueueItem(
            ingest_units=copy.deepcopy(ingest_units),
            extra_headers=extra_headers.copy(),
        )

        with self._retry_queue_lock:
            if self._retry_queue_max_size > 0 and len(self._retry_queue) >= self._retry_queue_max_size:
                self._retry_logger.warning(
                    "Pay-i retry queue is full (max_size=%d), dropping ingest request",
                    self._retry_queue_max_size,
                )
                return False
            self._retry_queue.append(item)

        self._retry_logger.error(f"Delayed retry of Pay-i ingest exception {api_ex}, cause {_qualified_exception_name(api_ex.__cause__)}, request {ingest_units}")

        self._retry_logger.debug(
            "Pay-i enqueued failed ingest for background retry (queue depth ~%d)",
            len(self._retry_queue),
        )

        # Lazily start the worker thread on first enqueue
        self._ensure_retry_queue_worker()
        return True

    def _ensure_retry_queue_worker(self) -> None:
        """Lazily start the background retry-queue worker thread (once)."""
        with self._retry_queue_started_lock:
            if self._retry_queue_worker_thread is not None:
                return

            thread = threading.Thread(
                target=self._retry_queue_worker_loop,
                name="payi-retry-queue-worker",
                daemon=True,
            )
            thread.start()
            self._retry_queue_worker_thread = thread
            self._retry_logger.debug("Pay-i retry queue worker thread started")

            atexit.register(self.shutdown)

    def _retry_queue_worker_loop(self) -> None:
        """Background thread that periodically drains and retries failed ingest calls."""
        self._retry_logger.debug("Pay-i retry queue worker loop started")

        while not self._retry_queue_shutdown.is_set():
            jitter = random.uniform(-_RETRY_QUEUE_WORKER_JITTER, _RETRY_QUEUE_WORKER_JITTER)
            sleep_time = max(0.1, self._retry_queue_interval + jitter)

            # Use Event.wait() so shutdown can interrupt the sleep
            if self._retry_queue_shutdown.wait(timeout=sleep_time):
                break  # Shutdown signaled during sleep

            self._drain_retry_queue()

        self._retry_logger.debug("Pay-i retry queue worker loop exited")

    def _drain_retry_queue(self) -> None:
        """Peek at front, try to send, pop only on success or non-retryable error.

        Sends as many items as possible within a time window.  On retryable
        failure the item stays at the front with its retry_count bumped and the
        batch stops.
        """
        deadline = time.monotonic() + _RETRY_QUEUE_BATCH_WINDOW
        sent = 0

        while time.monotonic() < deadline:
            with self._retry_queue_lock:
                if not self._retry_queue:
                    break
                item = self._retry_queue[0]  # peek

            if not self._retry_single_queued_item(item):
                break  # failed — item stays at front, next cycle retries

            # Success — remove the item we just sent
            with self._retry_queue_lock:
                if self._retry_queue and self._retry_queue[0] is item:
                    self._retry_queue.popleft()
            sent += 1

        if sent:
            self._retry_logger.debug("Pay-i retry queue batch sent %d items", sent)

    def _retry_single_queued_item(self, item: _RetryQueueItem) -> bool:
        """Attempt to re-send a single queued ingest call.

        Returns True on success, False on failure.  On retryable failure the
        item stays in the queue with its retry_count bumped.  On non-retryable
        error the item is removed from the queue and dropped.
        """
        try:
            if self._sync_ingest_fn:
                response = self.ingest_with_inline_retry(item.ingest_units, item.extra_headers, no_retry=True)
            else:
                response = self._run_async_ingest_from_thread(item.ingest_units, item.extra_headers)

            self._retry_logger.debug(
                "Pay-i retry queue: successfully re-sent ingest request (retry_count=%d)",
                item.retry_count,
            )
            if response:
                self._on_success(response)
            return True

        except (APIConnectionError, APIStatusError) as e:
            if is_retryable_connection_error(e):
                item.retry_count += 1
                self._retry_logger.debug(
                    "Pay-i retry queue: kept at front (retry_count=%d)",
                    item.retry_count,
                )
            else:
                # Non-retryable — remove and drop
                with self._retry_queue_lock:
                    if self._retry_queue and self._retry_queue[0] is item:
                        self._retry_queue.popleft()
                if isinstance(e, APIConnectionError):
                    self._on_connection_error(e, item.ingest_units)
                else:
                    self._on_api_status_error(e)
            return False

        except Exception as e:
            with self._retry_queue_lock:
                if self._retry_queue and self._retry_queue[0] is item:
                    self._retry_queue.popleft()
            self._retry_logger.error(
                "Pay-i retry queue: unexpected error retrying ingest (retry_count=%d): %s",
                item.retry_count, e,
            )
            return False

    def _run_async_ingest_from_thread(
        self,
        ingest_units: IngestUnitsParams,
        extra_headers: 'dict[str, str]',
    ) -> IngestResponse:
        """Run async ingest-with-retry from the background worker thread."""
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(
                self.aingest_with_inline_retry(ingest_units, extra_headers, no_retry=True)
            )
        finally:
            loop.close()

    # ------------------------------------------------------------------
    # Shutdown
    # ------------------------------------------------------------------

    def shutdown(self) -> None:
        """Signal the worker thread to stop, then try to send remaining items once."""
        if not self._ingest_retry_queue_enabled:
            return

        if self._retry_queue_worker_thread is None:
            return

        self._logger.debug("Pay-i retry queue: initiating shutdown")
        self._retry_queue_shutdown.set()

        self._retry_queue_worker_thread.join(timeout=_RETRY_QUEUE_DRAIN_TIMEOUT)

        if self._retry_queue_worker_thread.is_alive():
            self._logger.warning("Pay-i retry queue worker did not exit within %.1f seconds", _RETRY_QUEUE_DRAIN_TIMEOUT)

        # Final best-effort drain: send each item once without retry,
        # stop on the first APIConnectionError.
        with self._retry_queue_lock:
            items = list(self._retry_queue)
            self._retry_queue.clear()

        sent = 0
        remaining = len(items)
        for item in items:
            try:
                if self._sync_ingest_fn:
                    self._sync_ingest_fn(**item.ingest_units, extra_headers=item.extra_headers)
                else:
                    self._run_async_ingest_from_thread(item.ingest_units, item.extra_headers)
                sent += 1
            except APIConnectionError:
                self._logger.debug("Pay-i retry queue shutdown: connection error, stopping final drain")
                break
            except Exception as e:
                self._logger.debug("Pay-i retry queue shutdown: error sending item: %s", e)

        if remaining > 0:
            self._logger.debug("Pay-i retry queue shutdown: sent %d/%d remaining items", sent, remaining)
