# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .result import (
    ResultResource,
    AsyncResultResource,
    ResultResourceWithRawResponse,
    AsyncResultResourceWithRawResponse,
    ResultResourceWithStreamingResponse,
    AsyncResultResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ResponseIDResource", "AsyncResponseIDResource"]


class ResponseIDResource(SyncAPIResource):
    @cached_property
    def result(self) -> ResultResource:
        """Requests"""
        return ResultResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        """Requests"""
        return PropertiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResponseIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return ResponseIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return ResponseIDResourceWithStreamingResponse(self)


class AsyncResponseIDResource(AsyncAPIResource):
    @cached_property
    def result(self) -> AsyncResultResource:
        """Requests"""
        return AsyncResultResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        """Requests"""
        return AsyncPropertiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResponseIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Pay-i/pay-i-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponseIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Pay-i/pay-i-python#with_streaming_response
        """
        return AsyncResponseIDResourceWithStreamingResponse(self)


class ResponseIDResourceWithRawResponse:
    def __init__(self, response_id: ResponseIDResource) -> None:
        self._response_id = response_id

    @cached_property
    def result(self) -> ResultResourceWithRawResponse:
        """Requests"""
        return ResultResourceWithRawResponse(self._response_id.result)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        """Requests"""
        return PropertiesResourceWithRawResponse(self._response_id.properties)


class AsyncResponseIDResourceWithRawResponse:
    def __init__(self, response_id: AsyncResponseIDResource) -> None:
        self._response_id = response_id

    @cached_property
    def result(self) -> AsyncResultResourceWithRawResponse:
        """Requests"""
        return AsyncResultResourceWithRawResponse(self._response_id.result)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        """Requests"""
        return AsyncPropertiesResourceWithRawResponse(self._response_id.properties)


class ResponseIDResourceWithStreamingResponse:
    def __init__(self, response_id: ResponseIDResource) -> None:
        self._response_id = response_id

    @cached_property
    def result(self) -> ResultResourceWithStreamingResponse:
        """Requests"""
        return ResultResourceWithStreamingResponse(self._response_id.result)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        """Requests"""
        return PropertiesResourceWithStreamingResponse(self._response_id.properties)


class AsyncResponseIDResourceWithStreamingResponse:
    def __init__(self, response_id: AsyncResponseIDResource) -> None:
        self._response_id = response_id

    @cached_property
    def result(self) -> AsyncResultResourceWithStreamingResponse:
        """Requests"""
        return AsyncResultResourceWithStreamingResponse(self._response_id.result)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """Requests"""
        return AsyncPropertiesResourceWithStreamingResponse(self._response_id.properties)
