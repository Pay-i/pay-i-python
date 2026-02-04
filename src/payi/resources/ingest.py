# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import ingest_units_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.bulk_ingest_response import BulkIngestResponse
from ..types.bulk_ingest_request_param import BulkIngestRequestParam
from ..types.shared_params.ingest_units import IngestUnits
from ..types.pay_i_common_models_api_router_header_info_param import PayICommonModelsAPIRouterHeaderInfoParam

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
        events: Iterable[BulkIngestRequestParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            body=maybe_transform(events, Iterable[BulkIngestRequestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIngestResponse,
        )

    def units(
        self,
        *,
        category: str,
        units: Dict[str, IngestUnits],
        end_to_end_latency_ms: Optional[int] | Omit = omit,
        event_timestamp: Union[str, datetime, None] | Omit = omit,
        http_status_code: Optional[int] | Omit = omit,
        properties: Optional[Dict[str, Optional[str]]] | Omit = omit,
        provider_request_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]] | Omit = omit,
        provider_request_json: Optional[str] | Omit = omit,
        provider_request_reasoning_json: Optional[str] | Omit = omit,
        provider_response_function_calls: Optional[Iterable[ingest_units_params.ProviderResponseFunctionCall]]
        | Omit = omit,
        provider_response_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]] | Omit = omit,
        provider_response_id: Optional[str] | Omit = omit,
        provider_response_json: Union[str, SequenceNotStr[str], None] | Omit = omit,
        provider_uri: Optional[str] | Omit = omit,
        resource: Optional[str] | Omit = omit,
        time_to_first_completion_token_ms: Optional[int] | Omit = omit,
        time_to_first_token_ms: Optional[int] | Omit = omit,
        use_case_properties: Optional[Dict[str, Optional[str]]] | Omit = omit,
        x_proxy_account_name: str | Omit = omit,
        x_proxy_limit_ids: str | Omit = omit,
        x_proxy_logging_disable: str | Omit = omit,
        x_proxy_use_case_id: str | Omit = omit,
        x_proxy_use_case_name: str | Omit = omit,
        x_proxy_use_case_step: str | Omit = omit,
        x_proxy_use_case_version: int | Omit = omit,
        x_proxy_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "xProxy-Account-Name": x_proxy_account_name,
                    "xProxy-Limit-IDs": x_proxy_limit_ids,
                    "xProxy-Logging-Disable": x_proxy_logging_disable,
                    "xProxy-UseCase-ID": x_proxy_use_case_id,
                    "xProxy-UseCase-Name": x_proxy_use_case_name,
                    "xProxy-UseCase-Step": x_proxy_use_case_step,
                    "xProxy-UseCase-Version": str(x_proxy_use_case_version)
                    if is_given(x_proxy_use_case_version)
                    else not_given,
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
                    "units": units,
                    "end_to_end_latency_ms": end_to_end_latency_ms,
                    "event_timestamp": event_timestamp,
                    "http_status_code": http_status_code,
                    "properties": properties,
                    "provider_request_headers": provider_request_headers,
                    "provider_request_json": provider_request_json,
                    "provider_request_reasoning_json": provider_request_reasoning_json,
                    "provider_response_function_calls": provider_response_function_calls,
                    "provider_response_headers": provider_response_headers,
                    "provider_response_id": provider_response_id,
                    "provider_response_json": provider_response_json,
                    "provider_uri": provider_uri,
                    "resource": resource,
                    "time_to_first_completion_token_ms": time_to_first_completion_token_ms,
                    "time_to_first_token_ms": time_to_first_token_ms,
                    "use_case_properties": use_case_properties,
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
        events: Iterable[BulkIngestRequestParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            body=await async_maybe_transform(events, Iterable[BulkIngestRequestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIngestResponse,
        )

    async def units(
        self,
        *,
        category: str,
        units: Dict[str, IngestUnits],
        end_to_end_latency_ms: Optional[int] | Omit = omit,
        event_timestamp: Union[str, datetime, None] | Omit = omit,
        http_status_code: Optional[int] | Omit = omit,
        properties: Optional[Dict[str, Optional[str]]] | Omit = omit,
        provider_request_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]] | Omit = omit,
        provider_request_json: Optional[str] | Omit = omit,
        provider_request_reasoning_json: Optional[str] | Omit = omit,
        provider_response_function_calls: Optional[Iterable[ingest_units_params.ProviderResponseFunctionCall]]
        | Omit = omit,
        provider_response_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]] | Omit = omit,
        provider_response_id: Optional[str] | Omit = omit,
        provider_response_json: Union[str, SequenceNotStr[str], None] | Omit = omit,
        provider_uri: Optional[str] | Omit = omit,
        resource: Optional[str] | Omit = omit,
        time_to_first_completion_token_ms: Optional[int] | Omit = omit,
        time_to_first_token_ms: Optional[int] | Omit = omit,
        use_case_properties: Optional[Dict[str, Optional[str]]] | Omit = omit,
        x_proxy_account_name: str | Omit = omit,
        x_proxy_limit_ids: str | Omit = omit,
        x_proxy_logging_disable: str | Omit = omit,
        x_proxy_use_case_id: str | Omit = omit,
        x_proxy_use_case_name: str | Omit = omit,
        x_proxy_use_case_step: str | Omit = omit,
        x_proxy_use_case_version: int | Omit = omit,
        x_proxy_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "xProxy-Account-Name": x_proxy_account_name,
                    "xProxy-Limit-IDs": x_proxy_limit_ids,
                    "xProxy-Logging-Disable": x_proxy_logging_disable,
                    "xProxy-UseCase-ID": x_proxy_use_case_id,
                    "xProxy-UseCase-Name": x_proxy_use_case_name,
                    "xProxy-UseCase-Step": x_proxy_use_case_step,
                    "xProxy-UseCase-Version": str(x_proxy_use_case_version)
                    if is_given(x_proxy_use_case_version)
                    else not_given,
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
                    "units": units,
                    "end_to_end_latency_ms": end_to_end_latency_ms,
                    "event_timestamp": event_timestamp,
                    "http_status_code": http_status_code,
                    "properties": properties,
                    "provider_request_headers": provider_request_headers,
                    "provider_request_json": provider_request_json,
                    "provider_request_reasoning_json": provider_request_reasoning_json,
                    "provider_response_function_calls": provider_response_function_calls,
                    "provider_response_headers": provider_response_headers,
                    "provider_response_id": provider_response_id,
                    "provider_response_json": provider_response_json,
                    "provider_uri": provider_uri,
                    "resource": resource,
                    "time_to_first_completion_token_ms": time_to_first_completion_token_ms,
                    "time_to_first_token_ms": time_to_first_token_ms,
                    "use_case_properties": use_case_properties,
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
