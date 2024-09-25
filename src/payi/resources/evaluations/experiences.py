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
from ...types.evaluations import experience_create_params
from ...types.shared.evaluation_response import EvaluationResponse

__all__ = ["ExperiencesResource", "AsyncExperiencesResource"]


class ExperiencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return ExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return ExperiencesResourceWithStreamingResponse(self)

    def create(
        self,
        experience_id: str,
        *,
        evaluation: int,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationResponse:
        """
        Create an Evaluation for an Experience

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_id:
            raise ValueError(f"Expected a non-empty value for `experience_id` but received {experience_id!r}")
        return self._post(
            f"/api/v1/evaluations/experiences/{experience_id}",
            body=maybe_transform(
                {
                    "evaluation": evaluation,
                    "user_id": user_id,
                },
                experience_create_params.ExperienceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResponse,
        )


class AsyncExperiencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncExperiencesResourceWithStreamingResponse(self)

    async def create(
        self,
        experience_id: str,
        *,
        evaluation: int,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationResponse:
        """
        Create an Evaluation for an Experience

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience_id:
            raise ValueError(f"Expected a non-empty value for `experience_id` but received {experience_id!r}")
        return await self._post(
            f"/api/v1/evaluations/experiences/{experience_id}",
            body=await async_maybe_transform(
                {
                    "evaluation": evaluation,
                    "user_id": user_id,
                },
                experience_create_params.ExperienceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResponse,
        )


class ExperiencesResourceWithRawResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.create = to_raw_response_wrapper(
            experiences.create,
        )


class AsyncExperiencesResourceWithRawResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.create = async_to_raw_response_wrapper(
            experiences.create,
        )


class ExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.create = to_streamed_response_wrapper(
            experiences.create,
        )


class AsyncExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.create = async_to_streamed_response_wrapper(
            experiences.create,
        )
