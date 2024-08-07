# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .types import (
    TypesResource,
    AsyncTypesResource,
    TypesResourceWithRawResponse,
    AsyncTypesResourceWithRawResponse,
    TypesResourceWithStreamingResponse,
    AsyncTypesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.experience_instance import ExperienceInstance

__all__ = ["ExperiencesResource", "AsyncExperiencesResource"]


class ExperiencesResource(SyncAPIResource):
    @cached_property
    def types(self) -> TypesResource:
        return TypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExperiencesResourceWithRawResponse:
        return ExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperiencesResourceWithStreamingResponse:
        return ExperiencesResourceWithStreamingResponse(self)

    def create(
        self,
        experience_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceInstance:
        """Creates a new experience instance.

        This ID can then be passed into router calls
        for a specific user experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return self._post(
            f"/api/v1/experiences/instances/{experience_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceInstance,
        )

    def retrieve(
        self,
        experience_instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceInstance:
        """
        Get details for an experience instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_instance_id:
            raise ValueError(
                f"Expected a non-empty value for `experience_instance_id` but received {experience_instance_id!r}"
            )
        return self._get(
            f"/api/v1/experiences/instances/{experience_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceInstance,
        )

    def delete(
        self,
        experience_instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceInstance:
        """Deletes an experience instance.

        This will remove all costs associated with this
        experience instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_instance_id:
            raise ValueError(
                f"Expected a non-empty value for `experience_instance_id` but received {experience_instance_id!r}"
            )
        return self._delete(
            f"/api/v1/experiences/instances/{experience_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceInstance,
        )


class AsyncExperiencesResource(AsyncAPIResource):
    @cached_property
    def types(self) -> AsyncTypesResource:
        return AsyncTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExperiencesResourceWithRawResponse:
        return AsyncExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperiencesResourceWithStreamingResponse:
        return AsyncExperiencesResourceWithStreamingResponse(self)

    async def create(
        self,
        experience_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceInstance:
        """Creates a new experience instance.

        This ID can then be passed into router calls
        for a specific user experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_type_id:
            raise ValueError(f"Expected a non-empty value for `experience_type_id` but received {experience_type_id!r}")
        return await self._post(
            f"/api/v1/experiences/instances/{experience_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceInstance,
        )

    async def retrieve(
        self,
        experience_instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceInstance:
        """
        Get details for an experience instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_instance_id:
            raise ValueError(
                f"Expected a non-empty value for `experience_instance_id` but received {experience_instance_id!r}"
            )
        return await self._get(
            f"/api/v1/experiences/instances/{experience_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceInstance,
        )

    async def delete(
        self,
        experience_instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperienceInstance:
        """Deletes an experience instance.

        This will remove all costs associated with this
        experience instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_instance_id:
            raise ValueError(
                f"Expected a non-empty value for `experience_instance_id` but received {experience_instance_id!r}"
            )
        return await self._delete(
            f"/api/v1/experiences/instances/{experience_instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceInstance,
        )


class ExperiencesResourceWithRawResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.create = to_raw_response_wrapper(
            experiences.create,
        )
        self.retrieve = to_raw_response_wrapper(
            experiences.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            experiences.delete,
        )

    @cached_property
    def types(self) -> TypesResourceWithRawResponse:
        return TypesResourceWithRawResponse(self._experiences.types)


class AsyncExperiencesResourceWithRawResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.create = async_to_raw_response_wrapper(
            experiences.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            experiences.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            experiences.delete,
        )

    @cached_property
    def types(self) -> AsyncTypesResourceWithRawResponse:
        return AsyncTypesResourceWithRawResponse(self._experiences.types)


class ExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.create = to_streamed_response_wrapper(
            experiences.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            experiences.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            experiences.delete,
        )

    @cached_property
    def types(self) -> TypesResourceWithStreamingResponse:
        return TypesResourceWithStreamingResponse(self._experiences.types)


class AsyncExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.create = async_to_streamed_response_wrapper(
            experiences.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            experiences.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            experiences.delete,
        )

    @cached_property
    def types(self) -> AsyncTypesResourceWithStreamingResponse:
        return AsyncTypesResourceWithStreamingResponse(self._experiences.types)
