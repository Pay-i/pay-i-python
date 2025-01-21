# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.experiences import type_list_params, type_create_params, type_update_params
from ...types.experiences.experience_type import ExperienceType
from ...types.experiences.type_list_response import TypeListResponse

__all__ = ["TypesResource", "AsyncTypesResource"]


class TypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return TypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return TypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        logging_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Create an new Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/experiences/types",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "logging_enabled": logging_enabled,
                },
                type_create_params.TypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    def retrieve(
        self,
        experience_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Get Experience Type details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_name:
            raise ValueError(f"Expected a non-empty value for `experience_name` but received {experience_name!r}")
        return self._get(
            f"/api/v1/experiences/types/{experience_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    def update(
        self,
        experience_name: str,
        *,
        description: Optional[str],
        logging_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Update an Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_name:
            raise ValueError(f"Expected a non-empty value for `experience_name` but received {experience_name!r}")
        return self._patch(
            f"/api/v1/experiences/types/{experience_name}",
            body=maybe_transform(
                {
                    "description": description,
                    "logging_enabled": logging_enabled,
                },
                type_update_params.TypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TypeListResponse:
        """
        Get all Experience Types

        Args:
          name: Experience Type Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/experiences/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, type_list_params.TypeListParams),
            ),
            cast_to=TypeListResponse,
        )

    def delete(
        self,
        experience_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Delete an Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_name:
            raise ValueError(f"Expected a non-empty value for `experience_name` but received {experience_name!r}")
        return self._delete(
            f"/api/v1/experiences/types/{experience_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )


class AsyncTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        logging_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Create an new Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/experiences/types",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "logging_enabled": logging_enabled,
                },
                type_create_params.TypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    async def retrieve(
        self,
        experience_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Get Experience Type details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_name:
            raise ValueError(f"Expected a non-empty value for `experience_name` but received {experience_name!r}")
        return await self._get(
            f"/api/v1/experiences/types/{experience_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    async def update(
        self,
        experience_name: str,
        *,
        description: Optional[str],
        logging_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Update an Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_name:
            raise ValueError(f"Expected a non-empty value for `experience_name` but received {experience_name!r}")
        return await self._patch(
            f"/api/v1/experiences/types/{experience_name}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "logging_enabled": logging_enabled,
                },
                type_update_params.TypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    async def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TypeListResponse:
        """
        Get all Experience Types

        Args:
          name: Experience Type Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/experiences/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, type_list_params.TypeListParams),
            ),
            cast_to=TypeListResponse,
        )

    async def delete(
        self,
        experience_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Delete an Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_name:
            raise ValueError(f"Expected a non-empty value for `experience_name` but received {experience_name!r}")
        return await self._delete(
            f"/api/v1/experiences/types/{experience_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )


class TypesResourceWithRawResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.create = to_raw_response_wrapper(
            types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            types.update,
        )
        self.list = to_raw_response_wrapper(
            types.list,
        )
        self.delete = to_raw_response_wrapper(
            types.delete,
        )


class AsyncTypesResourceWithRawResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.create = async_to_raw_response_wrapper(
            types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            types.update,
        )
        self.list = async_to_raw_response_wrapper(
            types.list,
        )
        self.delete = async_to_raw_response_wrapper(
            types.delete,
        )


class TypesResourceWithStreamingResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.create = to_streamed_response_wrapper(
            types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            types.update,
        )
        self.list = to_streamed_response_wrapper(
            types.list,
        )
        self.delete = to_streamed_response_wrapper(
            types.delete,
        )


class AsyncTypesResourceWithStreamingResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.create = async_to_streamed_response_wrapper(
            types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            types.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            types.delete,
        )
