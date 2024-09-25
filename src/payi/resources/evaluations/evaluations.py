# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .requests import (
    RequestsResource,
    AsyncRequestsResource,
    RequestsResourceWithRawResponse,
    AsyncRequestsResourceWithRawResponse,
    RequestsResourceWithStreamingResponse,
    AsyncRequestsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .experiences import (
    ExperiencesResource,
    AsyncExperiencesResource,
    ExperiencesResourceWithRawResponse,
    AsyncExperiencesResourceWithRawResponse,
    ExperiencesResourceWithStreamingResponse,
    AsyncExperiencesResourceWithStreamingResponse,
)

__all__ = ["EvaluationsResource", "AsyncEvaluationsResource"]


class EvaluationsResource(SyncAPIResource):
    @cached_property
    def experiences(self) -> ExperiencesResource:
        return ExperiencesResource(self._client)

    @cached_property
    def requests(self) -> RequestsResource:
        return RequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return EvaluationsResourceWithStreamingResponse(self)


class AsyncEvaluationsResource(AsyncAPIResource):
    @cached_property
    def experiences(self) -> AsyncExperiencesResource:
        return AsyncExperiencesResource(self._client)

    @cached_property
    def requests(self) -> AsyncRequestsResource:
        return AsyncRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncEvaluationsResourceWithStreamingResponse(self)


class EvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def experiences(self) -> ExperiencesResourceWithRawResponse:
        return ExperiencesResourceWithRawResponse(self._evaluations.experiences)

    @cached_property
    def requests(self) -> RequestsResourceWithRawResponse:
        return RequestsResourceWithRawResponse(self._evaluations.requests)


class AsyncEvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def experiences(self) -> AsyncExperiencesResourceWithRawResponse:
        return AsyncExperiencesResourceWithRawResponse(self._evaluations.experiences)

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithRawResponse:
        return AsyncRequestsResourceWithRawResponse(self._evaluations.requests)


class EvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def experiences(self) -> ExperiencesResourceWithStreamingResponse:
        return ExperiencesResourceWithStreamingResponse(self._evaluations.experiences)

    @cached_property
    def requests(self) -> RequestsResourceWithStreamingResponse:
        return RequestsResourceWithStreamingResponse(self._evaluations.requests)


class AsyncEvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def experiences(self) -> AsyncExperiencesResourceWithStreamingResponse:
        return AsyncExperiencesResourceWithStreamingResponse(self._evaluations.experiences)

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithStreamingResponse:
        return AsyncRequestsResourceWithStreamingResponse(self._evaluations.requests)
