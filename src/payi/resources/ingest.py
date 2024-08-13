# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..types import ingest_units_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ingest_response import IngestResponse
from ..types.ingest_event_param import IngestEventParam
from ..types.bulk_ingest_response import BulkIngestResponse

__all__ = ["IngestResource", "AsyncIngestResource"]


class IngestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngestResourceWithRawResponse:
        return IngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestResourceWithStreamingResponse:
        return IngestResourceWithStreamingResponse(self)

    def bulk(
        self,
        *,
        events: Iterable[IngestEventParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkIngestResponse:
        """
        Bulk Ingest

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/ingest/bulk",
            body=maybe_transform(events, Iterable[IngestEventParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIngestResponse,
        )

    def units(
        self,
        *,
        category: str,
        input: int,
        output: int,
        resource: str,
        event_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        x_proxy_budget_ids: str | NotGiven = NOT_GIVEN,
        x_proxy_experience_id: str | NotGiven = NOT_GIVEN,
        x_proxy_request_tags: str | NotGiven = NOT_GIVEN,
        x_proxy_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IngestResponse:
        """
        Ingest an Event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "xProxy-Budget-IDs": x_proxy_budget_ids,
                    "xProxy-Experience-Id": x_proxy_experience_id,
                    "xProxy-Request-Tags": x_proxy_request_tags,
                    "xProxy-User-ID": x_proxy_user_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/api/v1/ingest",
            body=maybe_transform(
                {
                    "category": category,
                    "input": input,
                    "output": output,
                    "resource": resource,
                    "event_timestamp": event_timestamp,
                },
                ingest_units_params.IngestUnitsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestResponse,
        )


class AsyncIngestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngestResourceWithRawResponse:
        return AsyncIngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestResourceWithStreamingResponse:
        return AsyncIngestResourceWithStreamingResponse(self)

    async def bulk(
        self,
        *,
        events: Iterable[IngestEventParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkIngestResponse:
        """
        Bulk Ingest

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/ingest/bulk",
            body=await async_maybe_transform(events, Iterable[IngestEventParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIngestResponse,
        )

    async def units(
        self,
        *,
        category: str,
        input: int,
        output: int,
        resource: str,
        event_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        x_proxy_budget_ids: str | NotGiven = NOT_GIVEN,
        x_proxy_experience_id: str | NotGiven = NOT_GIVEN,
        x_proxy_request_tags: str | NotGiven = NOT_GIVEN,
        x_proxy_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IngestResponse:
        """
        Ingest an Event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "xProxy-Budget-IDs": x_proxy_budget_ids,
                    "xProxy-Experience-Id": x_proxy_experience_id,
                    "xProxy-Request-Tags": x_proxy_request_tags,
                    "xProxy-User-ID": x_proxy_user_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/api/v1/ingest",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "input": input,
                    "output": output,
                    "resource": resource,
                    "event_timestamp": event_timestamp,
                },
                ingest_units_params.IngestUnitsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IngestResponse,
        )


class IngestResourceWithRawResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.bulk = to_raw_response_wrapper(
            ingest.bulk,
        )
        self.units = to_raw_response_wrapper(
            ingest.units,
        )


class AsyncIngestResourceWithRawResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.bulk = async_to_raw_response_wrapper(
            ingest.bulk,
        )
        self.units = async_to_raw_response_wrapper(
            ingest.units,
        )


class IngestResourceWithStreamingResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.bulk = to_streamed_response_wrapper(
            ingest.bulk,
        )
        self.units = to_streamed_response_wrapper(
            ingest.units,
        )


class AsyncIngestResourceWithStreamingResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.bulk = async_to_streamed_response_wrapper(
            ingest.bulk,
        )
        self.units = async_to_streamed_response_wrapper(
            ingest.units,
        )
