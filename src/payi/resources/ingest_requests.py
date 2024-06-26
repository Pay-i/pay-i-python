# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ingest_request_create_params
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
from .._base_client import (
    make_request_options,
)
from ..types.successful_proxy_result import SuccessfulProxyResult

__all__ = ["IngestRequestsResource", "AsyncIngestRequestsResource"]


class IngestRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngestRequestsResourceWithRawResponse:
        return IngestRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestRequestsResourceWithStreamingResponse:
        return IngestRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: str,
        resource: str,
        units: ingest_request_create_params.Units,
        x_proxy_budget_ids: str | NotGiven = NOT_GIVEN,
        x_proxy_request_tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuccessfulProxyResult:
        """
        Ingest a request

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
                    "xProxy-Request-Tags": x_proxy_request_tags,
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
                },
                ingest_request_create_params.IngestRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessfulProxyResult,
        )


class AsyncIngestRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngestRequestsResourceWithRawResponse:
        return AsyncIngestRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestRequestsResourceWithStreamingResponse:
        return AsyncIngestRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: str,
        resource: str,
        units: ingest_request_create_params.Units,
        x_proxy_budget_ids: str | NotGiven = NOT_GIVEN,
        x_proxy_request_tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuccessfulProxyResult:
        """
        Ingest a request

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
                    "xProxy-Request-Tags": x_proxy_request_tags,
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
                },
                ingest_request_create_params.IngestRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessfulProxyResult,
        )


class IngestRequestsResourceWithRawResponse:
    def __init__(self, ingest_requests: IngestRequestsResource) -> None:
        self._ingest_requests = ingest_requests

        self.create = to_raw_response_wrapper(
            ingest_requests.create,
        )


class AsyncIngestRequestsResourceWithRawResponse:
    def __init__(self, ingest_requests: AsyncIngestRequestsResource) -> None:
        self._ingest_requests = ingest_requests

        self.create = async_to_raw_response_wrapper(
            ingest_requests.create,
        )


class IngestRequestsResourceWithStreamingResponse:
    def __init__(self, ingest_requests: IngestRequestsResource) -> None:
        self._ingest_requests = ingest_requests

        self.create = to_streamed_response_wrapper(
            ingest_requests.create,
        )


class AsyncIngestRequestsResourceWithStreamingResponse:
    def __init__(self, ingest_requests: AsyncIngestRequestsResource) -> None:
        self._ingest_requests = ingest_requests

        self.create = async_to_streamed_response_wrapper(
            ingest_requests.create,
        )
