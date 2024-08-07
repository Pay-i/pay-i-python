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
from ...types.experiences import type_create_params, type_update_params
from ...types.experiences.experience_type import ExperienceType
from ...types.experiences.type_list_response import TypeListResponse

__all__ = ["TypesResource", "AsyncTypesResource"]


class TypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TypesResourceWithRawResponse:
        return TypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesResourceWithStreamingResponse:
        return TypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """Adds a new experience type.

        Instances of this type can be created via
        /experiences/instance.

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
        experience_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Get details for a specific Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return self._get(
            f"/api/v1/experiences/types/{experience_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    def update(
        self,
        experience_type_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Updates an existing experience type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return self._patch(
            f"/api/v1/experiences/types/{experience_type_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TypeListResponse:
        """Get all Experience Types"""
        return self._get(
            "/api/v1/experiences/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypeListResponse,
        )

    def delete(
        self,
        experience_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """Deletes an experience type.

        This will remove visiblity of this type from all
        dashboard stats.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return self._delete(
            f"/api/v1/experiences/types/{experience_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )


class AsyncTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTypesResourceWithRawResponse:
        return AsyncTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesResourceWithStreamingResponse:
        return AsyncTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """Adds a new experience type.

        Instances of this type can be created via
        /experiences/instance.

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
        experience_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Get details for a specific Experience Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return await self._get(
            f"/api/v1/experiences/types/{experience_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceType,
        )

    async def update(
        self,
        experience_type_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """
        Updates an existing experience type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return await self._patch(
            f"/api/v1/experiences/types/{experience_type_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TypeListResponse:
        """Get all Experience Types"""
        return await self._get(
            "/api/v1/experiences/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypeListResponse,
        )

    async def delete(
        self,
        experience_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceType:
        """Deletes an experience type.

        This will remove visiblity of this type from all
        dashboard stats.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return await self._delete(
            f"/api/v1/experiences/types/{experience_type_id}",
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
