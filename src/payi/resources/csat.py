# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import csat_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
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
from ..types.csat import Csat
from .._base_client import make_request_options

__all__ = ["CsatResource", "AsyncCsatResource"]


class CsatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CsatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return CsatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CsatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return CsatResourceWithStreamingResponse(self)

    def create(
        self,
        experience_id: str,
        *,
        csat_rating: int,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Csat:
        """
        Created a CSAT rating for an Experience

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_id:
            raise ValueError(f"Expected a non-empty value for `experience_id` but received {experience_id!r}")
        return self._post(
            f"/api/v1/csat/experiences/{experience_id}",
            body=maybe_transform(
                {
                    "csat_rating": csat_rating,
                    "user_id": user_id,
                },
                csat_create_params.CsatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Csat,
        )


class AsyncCsatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCsatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCsatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCsatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncCsatResourceWithStreamingResponse(self)

    async def create(
        self,
        experience_id: str,
        *,
        csat_rating: int,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Csat:
        """
        Created a CSAT rating for an Experience

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_id:
            raise ValueError(f"Expected a non-empty value for `experience_id` but received {experience_id!r}")
        return await self._post(
            f"/api/v1/csat/experiences/{experience_id}",
            body=await async_maybe_transform(
                {
                    "csat_rating": csat_rating,
                    "user_id": user_id,
                },
                csat_create_params.CsatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Csat,
        )


class CsatResourceWithRawResponse:
    def __init__(self, csat: CsatResource) -> None:
        self._csat = csat

        self.create = to_raw_response_wrapper(
            csat.create,
        )


class AsyncCsatResourceWithRawResponse:
    def __init__(self, csat: AsyncCsatResource) -> None:
        self._csat = csat

        self.create = async_to_raw_response_wrapper(
            csat.create,
        )


class CsatResourceWithStreamingResponse:
    def __init__(self, csat: CsatResource) -> None:
        self._csat = csat

        self.create = to_streamed_response_wrapper(
            csat.create,
        )


class AsyncCsatResourceWithStreamingResponse:
    def __init__(self, csat: AsyncCsatResource) -> None:
        self._csat = csat

        self.create = async_to_streamed_response_wrapper(
            csat.create,
        )
