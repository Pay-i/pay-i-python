# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import price_modifier_create_params, price_modifier_update_params
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
from .._base_client import make_request_options
from ..types.price_modifier import PriceModifier
from ..types.price_modifier_retrieve_response import PriceModifierRetrieveResponse

__all__ = ["PriceModifiersResource", "AsyncPriceModifiersResource"]


class PriceModifiersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceModifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return PriceModifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceModifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return PriceModifiersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing_model_id: str,
        category: str,
        price_modifier: float,
        resource: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceModifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/price-modifier",
            body=maybe_transform(
                {
                    "billing_model_id": billing_model_id,
                    "category": category,
                    "price_modifier": price_modifier,
                    "resource": resource,
                },
                price_modifier_create_params.PriceModifierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceModifier,
        )

    def retrieve(
        self,
        billing_model_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceModifierRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_model_id:
            raise ValueError(f"Expected a non-empty value for `billing_model_id` but received {billing_model_id!r}")
        return self._get(
            f"/api/v1/price-modifier/{billing_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceModifierRetrieveResponse,
        )

    def update(
        self,
        *,
        billing_model_id: str,
        category: str,
        price_modifier: float,
        resource: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceModifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/price-modifier",
            body=maybe_transform(
                {
                    "billing_model_id": billing_model_id,
                    "category": category,
                    "price_modifier": price_modifier,
                    "resource": resource,
                },
                price_modifier_update_params.PriceModifierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceModifier,
        )


class AsyncPriceModifiersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceModifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceModifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceModifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncPriceModifiersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing_model_id: str,
        category: str,
        price_modifier: float,
        resource: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceModifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/price-modifier",
            body=await async_maybe_transform(
                {
                    "billing_model_id": billing_model_id,
                    "category": category,
                    "price_modifier": price_modifier,
                    "resource": resource,
                },
                price_modifier_create_params.PriceModifierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceModifier,
        )

    async def retrieve(
        self,
        billing_model_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceModifierRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_model_id:
            raise ValueError(f"Expected a non-empty value for `billing_model_id` but received {billing_model_id!r}")
        return await self._get(
            f"/api/v1/price-modifier/{billing_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceModifierRetrieveResponse,
        )

    async def update(
        self,
        *,
        billing_model_id: str,
        category: str,
        price_modifier: float,
        resource: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceModifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/price-modifier",
            body=await async_maybe_transform(
                {
                    "billing_model_id": billing_model_id,
                    "category": category,
                    "price_modifier": price_modifier,
                    "resource": resource,
                },
                price_modifier_update_params.PriceModifierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceModifier,
        )


class PriceModifiersResourceWithRawResponse:
    def __init__(self, price_modifiers: PriceModifiersResource) -> None:
        self._price_modifiers = price_modifiers

        self.create = to_raw_response_wrapper(
            price_modifiers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            price_modifiers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            price_modifiers.update,
        )


class AsyncPriceModifiersResourceWithRawResponse:
    def __init__(self, price_modifiers: AsyncPriceModifiersResource) -> None:
        self._price_modifiers = price_modifiers

        self.create = async_to_raw_response_wrapper(
            price_modifiers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            price_modifiers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            price_modifiers.update,
        )


class PriceModifiersResourceWithStreamingResponse:
    def __init__(self, price_modifiers: PriceModifiersResource) -> None:
        self._price_modifiers = price_modifiers

        self.create = to_streamed_response_wrapper(
            price_modifiers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            price_modifiers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            price_modifiers.update,
        )


class AsyncPriceModifiersResourceWithStreamingResponse:
    def __init__(self, price_modifiers: AsyncPriceModifiersResource) -> None:
        self._price_modifiers = price_modifiers

        self.create = async_to_streamed_response_wrapper(
            price_modifiers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            price_modifiers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            price_modifiers.update,
        )
