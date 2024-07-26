# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.categories import resources_all_create_params
from ...types.category_resource_response import CategoryResourceResponse
from ...types.categories.resources_all_delete_response import ResourcesAllDeleteResponse

__all__ = ["ResourcesAllResource", "AsyncResourcesAllResource"]


class ResourcesAllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesAllResourceWithRawResponse:
        return ResourcesAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesAllResourceWithStreamingResponse:
        return ResourcesAllResourceWithStreamingResponse(self)

    def create(
        self,
        resource: str,
        *,
        category: str,
        start_timestamp: Union[str, datetime],
        input_price: float | NotGiven = NOT_GIVEN,
        max_input_units: int | NotGiven = NOT_GIVEN,
        max_output_units: int | NotGiven = NOT_GIVEN,
        output_price: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryResourceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category:
            raise ValueError(f"Expected a non-empty value for `category` but received {category!r}")
        if not resource:
            raise ValueError(f"Expected a non-empty value for `resource` but received {resource!r}")
        return self._post(
            f"/api/v1/categories/{category}/resource/{resource}",
            body=maybe_transform(
                {
                    "start_timestamp": start_timestamp,
                    "input_price": input_price,
                    "max_input_units": max_input_units,
                    "max_output_units": max_output_units,
                    "output_price": output_price,
                },
                resources_all_create_params.ResourcesAllCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryResourceResponse,
        )

    def retrieve(
        self,
        start_timestamp: Union[str, datetime],
        *,
        category: str,
        resource: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryResourceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category:
            raise ValueError(f"Expected a non-empty value for `category` but received {category!r}")
        if not resource:
            raise ValueError(f"Expected a non-empty value for `resource` but received {resource!r}")
        if not start_timestamp:
            raise ValueError(f"Expected a non-empty value for `start_timestamp` but received {start_timestamp!r}")
        return self._get(
            f"/api/v1/categories/{category}/resource/{resource}/{start_timestamp}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryResourceResponse,
        )

    def delete(
        self,
        resource: str,
        *,
        category: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourcesAllDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category:
            raise ValueError(f"Expected a non-empty value for `category` but received {category!r}")
        if not resource:
            raise ValueError(f"Expected a non-empty value for `resource` but received {resource!r}")
        return self._delete(
            f"/api/v1/categories/{category}/resource/{resource}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourcesAllDeleteResponse,
        )


class AsyncResourcesAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesAllResourceWithRawResponse:
        return AsyncResourcesAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesAllResourceWithStreamingResponse:
        return AsyncResourcesAllResourceWithStreamingResponse(self)

    async def create(
        self,
        resource: str,
        *,
        category: str,
        start_timestamp: Union[str, datetime],
        input_price: float | NotGiven = NOT_GIVEN,
        max_input_units: int | NotGiven = NOT_GIVEN,
        max_output_units: int | NotGiven = NOT_GIVEN,
        output_price: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryResourceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category:
            raise ValueError(f"Expected a non-empty value for `category` but received {category!r}")
        if not resource:
            raise ValueError(f"Expected a non-empty value for `resource` but received {resource!r}")
        return await self._post(
            f"/api/v1/categories/{category}/resource/{resource}",
            body=await async_maybe_transform(
                {
                    "start_timestamp": start_timestamp,
                    "input_price": input_price,
                    "max_input_units": max_input_units,
                    "max_output_units": max_output_units,
                    "output_price": output_price,
                },
                resources_all_create_params.ResourcesAllCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryResourceResponse,
        )

    async def retrieve(
        self,
        start_timestamp: Union[str, datetime],
        *,
        category: str,
        resource: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryResourceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category:
            raise ValueError(f"Expected a non-empty value for `category` but received {category!r}")
        if not resource:
            raise ValueError(f"Expected a non-empty value for `resource` but received {resource!r}")
        if not start_timestamp:
            raise ValueError(f"Expected a non-empty value for `start_timestamp` but received {start_timestamp!r}")
        return await self._get(
            f"/api/v1/categories/{category}/resource/{resource}/{start_timestamp}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryResourceResponse,
        )

    async def delete(
        self,
        resource: str,
        *,
        category: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourcesAllDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category:
            raise ValueError(f"Expected a non-empty value for `category` but received {category!r}")
        if not resource:
            raise ValueError(f"Expected a non-empty value for `resource` but received {resource!r}")
        return await self._delete(
            f"/api/v1/categories/{category}/resource/{resource}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourcesAllDeleteResponse,
        )


class ResourcesAllResourceWithRawResponse:
    def __init__(self, resources_all: ResourcesAllResource) -> None:
        self._resources_all = resources_all

        self.create = to_raw_response_wrapper(
            resources_all.create,
        )
        self.retrieve = to_raw_response_wrapper(
            resources_all.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            resources_all.delete,
        )


class AsyncResourcesAllResourceWithRawResponse:
    def __init__(self, resources_all: AsyncResourcesAllResource) -> None:
        self._resources_all = resources_all

        self.create = async_to_raw_response_wrapper(
            resources_all.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            resources_all.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            resources_all.delete,
        )


class ResourcesAllResourceWithStreamingResponse:
    def __init__(self, resources_all: ResourcesAllResource) -> None:
        self._resources_all = resources_all

        self.create = to_streamed_response_wrapper(
            resources_all.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            resources_all.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            resources_all.delete,
        )


class AsyncResourcesAllResourceWithStreamingResponse:
    def __init__(self, resources_all: AsyncResourcesAllResource) -> None:
        self._resources_all = resources_all

        self.create = async_to_streamed_response_wrapper(
            resources_all.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            resources_all.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            resources_all.delete,
        )
