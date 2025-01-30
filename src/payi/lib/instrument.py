import json
import uuid
import asyncio
import inspect
import logging
import traceback
from typing import Any, Set, Union, Callable, Optional

from wrapt import ObjectProxy  # type: ignore

from payi import Payi, AsyncPayi
from payi.types import IngestUnitsParams

from .Stopwatch import Stopwatch
from .Instruments import Instruments


class PayiInstrumentor:
    def __init__(
        self,
        payi: Union[Payi, AsyncPayi, None] = None,
        instruments: Union[Set[Instruments], None] = None,
        log_prompt_and_response: bool = True,
        prompt_and_response_logger: Optional[
            Callable[[str, "dict[str, str]"], None]
        ] = None,  # (request id, dict of data to store) -> None
    ):
        self._payi: Union[Payi, AsyncPayi, None] = payi
        self._context_stack: list[dict[str, Any]] = []  # Stack of context dictionaries
        self._log_prompt_and_response: bool = log_prompt_and_response
        self._prompt_and_response_logger: Optional[Callable[[str, dict[str, str]], None]] = prompt_and_response_logger

        self._blocked_limits: set[str] = set()
        self._exceeded_limits: set[str] = set()

        if instruments is None or Instruments.ALL in instruments:
            self._instrument_all()
        else:
            self._instrument_specific(instruments)

    def _instrument_all(self) -> None:
        self._instrument_openai()
        self._instrument_anthropic()

    def _instrument_specific(self, instruments: Set[Instruments]) -> None:
        if Instruments.OPENAI in instruments:
            self._instrument_openai()
        if Instruments.ANTHROPIC in instruments:
            self._instrument_anthropic()

    def _instrument_openai(self) -> None:
        from .OpenAIInstrumentor import OpenAiInstrumentor

        try:
            OpenAiInstrumentor.instrument(self)

        except Exception as e:
            logging.error(f"Error instrumenting OpenAI: {e}")

    def _instrument_anthropic(self) -> None:
        from .AnthropicInstrumentor import AnthropicIntrumentor

        try:
            AnthropicIntrumentor.instrument(self)

        except Exception as e:
            logging.error(f"Error instrumenting Anthropic: {e}")

    def _ingest_units(self, ingest_units: IngestUnitsParams) -> None:
        # return early if there are no units to ingest and on a successul ingest request
        if int(ingest_units.get("http_status_code") or 0) < 400:
            units = ingest_units.get("units", {})
            if not units or all(unit.get("input", 0) == 0 and unit.get("output", 0) == 0 for unit in units.values()):
                logging.error(
                    'No units to ingest.  For OpenAI streaming calls, make sure you pass stream_options={"include_usage": True}'
                )
                return

        try:
            if isinstance(self._payi, AsyncPayi):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    ingest_result = loop.run_until_complete(self._payi.ingest.units(**ingest_units))
                finally:
                    loop.close()
            elif isinstance(self._payi, Payi):
                ingest_result = self._payi.ingest.units(**ingest_units)
            else:
                logging.error("No payi instance to ingest units")
                return

            if ingest_result.xproxy_result.limits:
                for limit_id, state in ingest_result.xproxy_result.limits.items():
                    removeBlockedId: bool = False

                    if state.state == "blocked":
                        self._blocked_limits.add(limit_id)
                    elif state.state == "exceeded":
                        self._exceeded_limits.add(limit_id)
                        removeBlockedId = True
                    elif state.state == "ok":
                        removeBlockedId = True

                    # opportunistically remove blocked limits
                    if removeBlockedId:
                        self._blocked_limits.discard(limit_id)

            if self._log_prompt_and_response and self._prompt_and_response_logger:
                request_id = ingest_result.xproxy_result.request_id

                log_data = {}
                response_json = ingest_units.pop("provider_response_json", None)
                request_json = ingest_units.pop("provider_request_json", None)
                stack_trace = ingest_units.get("properties", {}).pop("system.stack_trace", None)  # type: ignore

                if response_json is not None:
                    # response_json is a list of strings, convert a single json string
                    log_data["provider_response_json"] = json.dumps(response_json)
                if request_json is not None:
                    log_data["provider_request_json"] = request_json
                if stack_trace is not None:
                    log_data["stack_trace"] = stack_trace

                self._prompt_and_response_logger(request_id, log_data)  # type: ignore

        except Exception as e:
            logging.error(f"Error Pay-i ingesting result: {e}")

    def _call_func(
        self,
        func: Any,
        proxy: bool,
        limit_ids: Optional["list[str]"],
        request_tags: Optional["list[str]"],
        experience_name: Optional[str],
        experience_id: Optional[str],
        user_id: Optional[str],
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        if len(self._context_stack) > 0:
            # copy current context into the upcoming context
            context = self._context_stack[-1].copy()
            context.pop("proxy", None)
            previous_experience_name = context["experience_name"]
            previous_experience_id = context["experience_id"]
        else:
            context = {}
            previous_experience_name = None
            previous_experience_id = None

        with self:
            context["proxy"] = proxy

            # Handle experience name and ID logic
            if not experience_name:
                # If no experience_name specified, use previous values
                context["experience_name"] = previous_experience_name
                context["experience_id"] = previous_experience_id
            else:
                # If experience_name is specified
                if experience_name == previous_experience_name:
                    # Same experience name, use previous ID unless new one specified
                    context["experience_name"] = experience_name
                    context["experience_id"] = experience_id if experience_id else previous_experience_id
                else:
                    # Different experience name, use specified ID or generate one
                    context["experience_name"] = experience_name
                    context["experience_id"] = experience_id if experience_id else str(uuid.uuid4())

            # set any values explicitly passed by the caller, otherwise use what is already in the context
            if limit_ids:
                context["limit_ids"] = limit_ids
            if request_tags:
                context["request_tags"] = request_tags
            if user_id:
                context["user_id"] = user_id

            self.set_context(context)

            return func(*args, **kwargs)

    def __enter__(self) -> Any:
        # Push a new context dictionary onto the stack
        self._context_stack.append({})
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        # Pop the current context off the stack
        if self._context_stack:
            self._context_stack.pop()

    def set_context(self, context: "dict[str, Any]") -> None:
        # Update the current top of the stack with the provided context
        if self._context_stack:
            self._context_stack[-1].update(context)

    def get_context(self) -> Optional["dict[str, Any]"]:
        # Return the current top of the stack
        return self._context_stack[-1] if self._context_stack else None

    def chat_wrapper(
        self,
        category: str,
        process_chunk: Callable[[Any, IngestUnitsParams], None],
        process_synchronous_response: Optional[Callable[[Any, IngestUnitsParams, bool], None]],
        wrapped: Any,
        instance: Any,
        args: Any,
        kwargs: Any,
    ) -> Any:
        context = self.get_context()

        if not context:
            # should not happen
            return wrapped(*args, **kwargs)

        if context.get("proxy", True):
            proxy_extra_headers = kwargs.get("extra_headers", {})

            self._update_headers(context, proxy_extra_headers)

            if "extra_headers" not in kwargs:
                kwargs["extra_headers"] = proxy_extra_headers

            return wrapped(*args, **kwargs)

        ingest: IngestUnitsParams = {"category": category, "resource": kwargs.get("model"), "units": {}}

        # blocked_limit = next((limit for limit in (context.get('limit_ids') or []) if limit in self._blocked_limits), None)
        # if blocked_limit:
        #      raise Exception(f"Limit {blocked_limit} is blocked")
        current_frame = inspect.currentframe()
        # f_back excludes the current frame, strip() cleans up whitespace and newlines
        stack = [frame.strip() for frame in traceback.format_stack(current_frame.f_back)]  # type: ignore

        # TODO add back once feature is in prod
        # ingest['properties'] = { 'system.stack_trace': json.dumps(stack) }

        sw = Stopwatch()
        stream = kwargs.get("stream", False)

        try:
            limit_ids = context.get("limit_ids")
            request_tags = context.get("request_tags")
            experience_name = context.get("experience_name")
            experience_id = context.get("experience_id")
            user_id = context.get("user_id")

            if limit_ids:
                ingest["limit_ids"] = limit_ids
            if request_tags:
                ingest["request_tags"] = request_tags
            if experience_name:
                ingest["experience_name"] = experience_name
            if experience_id:
                ingest["experience_id"] = experience_id
            if user_id:
                ingest["user_id"] = user_id

            extra_headers: dict[str, str] = kwargs.get("extra_headers") or {}

            if len(extra_headers) > 0:
                ingest["provider_request_headers"] = {k: [v] for k, v in extra_headers.items()}  # type: ignore

            provider_prompt = {}
            for k, v in kwargs.items():
                if k == "messages":
                    provider_prompt[k] = [m.model_dump() if hasattr(m, "model_dump") else m for m in v]
                elif k in ["extra_headers", "extra_query"]:
                    pass
                else:
                    provider_prompt[k] = v

            if self._log_prompt_and_response:
                ingest["provider_request_json"] = json.dumps(provider_prompt)

            sw.start()
            response = wrapped(*args, **kwargs.copy())

        except Exception as e:  # pylint: disable=broad-except
            sw.stop()
            duration = sw.elapsed_ms_int()

            # TODO ingest error

            raise e

        if stream:
            return ChatStreamWrapper(
                response=response,
                instance=instance,
                instrumentor=self,
                log_prompt_and_response=self._log_prompt_and_response,
                ingest=ingest,
                stopwatch=sw,
                process_chunk=process_chunk,
            )

        sw.stop()
        duration = sw.elapsed_ms_int()
        ingest["end_to_end_latency_ms"] = duration
        ingest["http_status_code"] = 200

        if process_synchronous_response:
            process_synchronous_response(response, ingest, self._log_prompt_and_response)

        self._ingest_units(ingest)

        return response

    @staticmethod
    def _update_headers(
        context: "dict[str, Any]",
        extra_headers: "dict[str, str]",
    ) -> None:
        limit_ids: Optional[list[str]] = context.get("limit_ids")
        request_tags: Optional[list[str]] = context.get("request_tags")
        experience_name: Optional[str] = context.get("experience_name")
        experience_id: Optional[str] = context.get("experience_id")
        user_id: Optional[str] = context.get("user_id")

        if limit_ids is not None:
            existing_limit_ids = extra_headers.get("xProxy-Limit-IDs")
            limit_ids_str = ",".join(limit_ids)
            if existing_limit_ids is None:
                extra_headers["xProxy-Limit-IDs"] = limit_ids_str
            else:
                extra_headers["xProxy-Limit-IDs"] = f"{existing_limit_ids},{limit_ids_str}"

        if request_tags is not None:
            existing_request_tags = extra_headers.get("xProxy-Request-Tags")
            request_tags_str = ",".join(request_tags)
            if existing_request_tags is None:
                extra_headers["xProxy-Request-Tags"] = request_tags_str
            else:
                extra_headers["xProxy-Request-Tags"] = f"{existing_request_tags},{request_tags_str}"

        if experience_name is not None:
            extra_headers["xProxy-Experience-Name"] = experience_name

        if experience_id is not None:
            extra_headers["xProxy-Experience-ID"] = experience_id

        if user_id is not None:
            extra_headers["xProxy-User-ID"] = user_id

    @staticmethod
    def payi_wrapper(func: Any) -> Any:
        def _payi_wrapper(o: Any) -> Any:
            def wrapper(wrapped: Any, instance: Any, args: Any, kwargs: Any) -> Any:
                return func(
                    o,
                    wrapped,
                    instance,
                    args,
                    kwargs,
                )

            return wrapper

        return _payi_wrapper


class ChatStreamWrapper(ObjectProxy):  # type: ignore
    def __init__(
        self,
        response: Any,
        instance: Any,
        instrumentor: PayiInstrumentor,
        ingest: IngestUnitsParams,
        stopwatch: Stopwatch,
        process_chunk: Optional[Callable[[Any, IngestUnitsParams], None]] = None,
        log_prompt_and_response: bool = True,
    ) -> None:
        super().__init__(response)  # type: ignore

        self._response = response
        self._instance = instance

        self._instrumentor = instrumentor
        self._stopwatch: Stopwatch = stopwatch
        self._ingest: IngestUnitsParams = ingest
        self._log_prompt_and_response: bool = log_prompt_and_response
        self._responses: list[str] = []

        self._process_chunk: Optional[Callable[[Any, IngestUnitsParams], None]] = process_chunk

        self._first_token: bool = True

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: 
        self.__wrapped__.__exit__(exc_type, exc_val, exc_tb)  # type: ignore

    async def __aenter__(self) -> Any:
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.__wrapped__.__aexit__(exc_type, exc_val, exc_tb)  # type: ignore

    def __iter__(self) -> Any:
        return self

    def __aiter__(self) -> Any:
        return self

    def __next__(self) -> Any:
        try:
            chunk: Any = self.__wrapped__.__next__()  # type: ignore
        except Exception as e:
            if isinstance(e, StopIteration):
                self._stop_iteration()
            raise e
        else:
            self._evaluate_chunk(chunk)
            return chunk

    async def __anext__(self) -> Any:
        try:
            chunk: Any = await self.__wrapped__.__anext__()  # type: ignore
        except Exception as e:
            if isinstance(e, StopAsyncIteration):
                self._stop_iteration()
            raise e
        else:
            self._evaluate_chunk(chunk)
            return chunk

    def _evaluate_chunk(self, chunk: Any) -> None:
        if self._first_token:
            self._ingest["time_to_first_token_ms"] = self._stopwatch.elapsed_ms_int()
            self._first_token = False

        if self._log_prompt_and_response:
            self._responses.append(chunk.to_json())

        if self._process_chunk:
            self._process_chunk(chunk, self._ingest)

    def _stop_iteration(self) -> None:
        self._stopwatch.stop()
        self._ingest["end_to_end_latency_ms"] = self._stopwatch.elapsed_ms_int()
        self._ingest["http_status_code"] = 200

        if self._log_prompt_and_response:
            self._ingest["provider_response_json"] = self._responses

        self._instrumentor._ingest_units(self._ingest)


global _instrumentor
_instrumentor: PayiInstrumentor


def payi_instrument(
    payi: Optional[Union[Payi, AsyncPayi]] = None,
    instruments: Optional[Set[Instruments]] = None,
    log_prompt_and_response: bool = True,
    prompt_and_response_logger: Optional[Callable[[str, "dict[str, str]"], None]] = None,
) -> None:
    global _instrumentor
    _instrumentor = PayiInstrumentor(
        payi=payi,
        instruments=instruments,
        log_prompt_and_response=log_prompt_and_response,
        prompt_and_response_logger=prompt_and_response_logger,
    )


def ingest(
    limit_ids: Optional["list[str]"] = None,
    request_tags: Optional["list[str]"] = None,
    experience_name: Optional[str] = None,
    experience_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> Any:
    def _ingest(func: Any) -> Any:
        def _ingest_wrapper(*args: Any, **kwargs: Any) -> Any:
            return _instrumentor._call_func(
                func,
                False,  # false -> ingest
                limit_ids,
                request_tags,
                experience_name,
                experience_id,
                user_id,
                *args,
                **kwargs,
            )

        return _ingest_wrapper

    return _ingest


def proxy(
    limit_ids: Optional["list[str]"] = None,
    request_tags: Optional["list[str]"] = None,
    experience_name: Optional[str] = None,
    experience_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> Any:
    def _proxy(func: Any) -> Any:
        def _proxy_wrapper(*args: Any, **kwargs: Any) -> Any:
            return _instrumentor._call_func(
                func, True, limit_ids, request_tags, experience_name, experience_id, user_id, *args, **kwargs
            )

        return _proxy_wrapper

    return _proxy
