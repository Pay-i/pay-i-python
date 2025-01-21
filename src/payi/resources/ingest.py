# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return IngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
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
        resource: str,
        units: Dict[str, ingest_units_params.Units],
        end_to_end_latency_ms: Optional[int] | NotGiven = NOT_GIVEN,
        event_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        experience_properties: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        http_status_code: Optional[int] | NotGiven = NOT_GIVEN,
        properties: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        provider_request_headers: Optional[Iterable[ingest_units_params.ProviderRequestHeader]] | NotGiven = NOT_GIVEN,
        provider_request_json: Optional[str] | NotGiven = NOT_GIVEN,
        provider_response_headers: Optional[Iterable[ingest_units_params.ProviderResponseHeader]]
        | NotGiven = NOT_GIVEN,
        provider_response_json: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        provider_uri: Optional[str] | NotGiven = NOT_GIVEN,
        time_to_first_token_ms: Optional[int] | NotGiven = NOT_GIVEN,
        x_proxy_experience_id: str | NotGiven = NOT_GIVEN,
        x_proxy_experience_name: str | NotGiven = NOT_GIVEN,
        x_proxy_limit_ids: str | NotGiven = NOT_GIVEN,
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
                    "xProxy-Experience-ID": x_proxy_experience_id,
                    "xProxy-Experience-Name": x_proxy_experience_name,
                    "xProxy-Limit-IDs": x_proxy_limit_ids,
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
                    "resource": resource,
                    "units": units,
                    "end_to_end_latency_ms": end_to_end_latency_ms,
                    "event_timestamp": event_timestamp,
                    "experience_properties": experience_properties,
                    "http_status_code": http_status_code,
                    "properties": properties,
                    "provider_request_headers": provider_request_headers,
                    "provider_request_json": provider_request_json,
                    "provider_response_headers": provider_response_headers,
                    "provider_response_json": provider_response_json,
                    "provider_uri": provider_uri,
                    "time_to_first_token_ms": time_to_first_token_ms,
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
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
        resource: str,
        units: Dict[str, ingest_units_params.Units],
        end_to_end_latency_ms: Optional[int] | NotGiven = NOT_GIVEN,
        event_timestamp: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        experience_properties: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        http_status_code: Optional[int] | NotGiven = NOT_GIVEN,
        properties: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        provider_request_headers: Optional[Iterable[ingest_units_params.ProviderRequestHeader]] | NotGiven = NOT_GIVEN,
        provider_request_json: Optional[str] | NotGiven = NOT_GIVEN,
        provider_response_headers: Optional[Iterable[ingest_units_params.ProviderResponseHeader]]
        | NotGiven = NOT_GIVEN,
        provider_response_json: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        provider_uri: Optional[str] | NotGiven = NOT_GIVEN,
        time_to_first_token_ms: Optional[int] | NotGiven = NOT_GIVEN,
        x_proxy_experience_id: str | NotGiven = NOT_GIVEN,
        x_proxy_experience_name: str | NotGiven = NOT_GIVEN,
        x_proxy_limit_ids: str | NotGiven = NOT_GIVEN,
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
                    "xProxy-Experience-ID": x_proxy_experience_id,
                    "xProxy-Experience-Name": x_proxy_experience_name,
                    "xProxy-Limit-IDs": x_proxy_limit_ids,
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
                    "resource": resource,
                    "units": units,
                    "end_to_end_latency_ms": end_to_end_latency_ms,
                    "event_timestamp": event_timestamp,
                    "experience_properties": experience_properties,
                    "http_status_code": http_status_code,
                    "properties": properties,
                    "provider_request_headers": provider_request_headers,
                    "provider_request_json": provider_request_json,
                    "provider_response_headers": provider_response_headers,
                    "provider_response_json": provider_response_json,
                    "provider_uri": provider_uri,
                    "time_to_first_token_ms": time_to_first_token_ms,
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
