# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import billing_model_create_params, billing_model_update_params
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
from ..types.billing_model import BillingModel
from ..types.billing_model_list_response import BillingModelListResponse

__all__ = ["BillingModelsResource", "AsyncBillingModelsResource"]


class BillingModelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return BillingModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return BillingModelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal["costplus", "subscription", "hybrid"],
        default_price_modifier: Optional[float] | NotGiven = NOT_GIVEN,
        prepaid_amount: Optional[float] | NotGiven = NOT_GIVEN,
        prepaid_max: Optional[float] | NotGiven = NOT_GIVEN,
        threshold: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/billing-model",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "default_price_modifier": default_price_modifier,
                    "prepaid_amount": prepaid_amount,
                    "prepaid_max": prepaid_max,
                    "threshold": threshold,
                },
                billing_model_create_params.BillingModelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
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
    ) -> BillingModel:
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
            f"/api/v1/billing-model/{billing_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
        )

    def update(
        self,
        billing_model_id: str,
        *,
        type: Literal["costplus", "subscription", "hybrid"],
        default_price_modifier: Optional[float] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prepaid_amount: Optional[float] | NotGiven = NOT_GIVEN,
        prepaid_max: Optional[float] | NotGiven = NOT_GIVEN,
        threshold: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_model_id:
            raise ValueError(f"Expected a non-empty value for `billing_model_id` but received {billing_model_id!r}")
        return self._put(
            f"/api/v1/billing-model/{billing_model_id}",
            body=maybe_transform(
                {
                    "type": type,
                    "default_price_modifier": default_price_modifier,
                    "name": name,
                    "prepaid_amount": prepaid_amount,
                    "prepaid_max": prepaid_max,
                    "threshold": threshold,
                },
                billing_model_update_params.BillingModelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModelListResponse:
        return self._get(
            "/api/v1/billing-model",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModelListResponse,
        )

    def set_default(
        self,
        billing_model_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_model_id:
            raise ValueError(f"Expected a non-empty value for `billing_model_id` but received {billing_model_id!r}")
        return self._put(
            f"/api/v1/billing-model/{billing_model_id}/default",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
        )


class AsyncBillingModelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncBillingModelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal["costplus", "subscription", "hybrid"],
        default_price_modifier: Optional[float] | NotGiven = NOT_GIVEN,
        prepaid_amount: Optional[float] | NotGiven = NOT_GIVEN,
        prepaid_max: Optional[float] | NotGiven = NOT_GIVEN,
        threshold: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/billing-model",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "default_price_modifier": default_price_modifier,
                    "prepaid_amount": prepaid_amount,
                    "prepaid_max": prepaid_max,
                    "threshold": threshold,
                },
                billing_model_create_params.BillingModelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
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
    ) -> BillingModel:
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
            f"/api/v1/billing-model/{billing_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
        )

    async def update(
        self,
        billing_model_id: str,
        *,
        type: Literal["costplus", "subscription", "hybrid"],
        default_price_modifier: Optional[float] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prepaid_amount: Optional[float] | NotGiven = NOT_GIVEN,
        prepaid_max: Optional[float] | NotGiven = NOT_GIVEN,
        threshold: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_model_id:
            raise ValueError(f"Expected a non-empty value for `billing_model_id` but received {billing_model_id!r}")
        return await self._put(
            f"/api/v1/billing-model/{billing_model_id}",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "default_price_modifier": default_price_modifier,
                    "name": name,
                    "prepaid_amount": prepaid_amount,
                    "prepaid_max": prepaid_max,
                    "threshold": threshold,
                },
                billing_model_update_params.BillingModelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModelListResponse:
        return await self._get(
            "/api/v1/billing-model",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModelListResponse,
        )

    async def set_default(
        self,
        billing_model_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingModel:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_model_id:
            raise ValueError(f"Expected a non-empty value for `billing_model_id` but received {billing_model_id!r}")
        return await self._put(
            f"/api/v1/billing-model/{billing_model_id}/default",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingModel,
        )


class BillingModelsResourceWithRawResponse:
    def __init__(self, billing_models: BillingModelsResource) -> None:
        self._billing_models = billing_models

        self.create = to_raw_response_wrapper(
            billing_models.create,
        )
        self.retrieve = to_raw_response_wrapper(
            billing_models.retrieve,
        )
        self.update = to_raw_response_wrapper(
            billing_models.update,
        )
        self.list = to_raw_response_wrapper(
            billing_models.list,
        )
        self.set_default = to_raw_response_wrapper(
            billing_models.set_default,
        )


class AsyncBillingModelsResourceWithRawResponse:
    def __init__(self, billing_models: AsyncBillingModelsResource) -> None:
        self._billing_models = billing_models

        self.create = async_to_raw_response_wrapper(
            billing_models.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            billing_models.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            billing_models.update,
        )
        self.list = async_to_raw_response_wrapper(
            billing_models.list,
        )
        self.set_default = async_to_raw_response_wrapper(
            billing_models.set_default,
        )


class BillingModelsResourceWithStreamingResponse:
    def __init__(self, billing_models: BillingModelsResource) -> None:
        self._billing_models = billing_models

        self.create = to_streamed_response_wrapper(
            billing_models.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            billing_models.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            billing_models.update,
        )
        self.list = to_streamed_response_wrapper(
            billing_models.list,
        )
        self.set_default = to_streamed_response_wrapper(
            billing_models.set_default,
        )


class AsyncBillingModelsResourceWithStreamingResponse:
    def __init__(self, billing_models: AsyncBillingModelsResource) -> None:
        self._billing_models = billing_models

        self.create = async_to_streamed_response_wrapper(
            billing_models.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            billing_models.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            billing_models.update,
        )
        self.list = async_to_streamed_response_wrapper(
            billing_models.list,
        )
        self.set_default = async_to_streamed_response_wrapper(
            billing_models.set_default,
        )
