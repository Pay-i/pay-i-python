# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ingest_units_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
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
from .._base_client import (
    make_request_options,
)
from ..types.proxy_result import ProxyResult

__all__ = ["IngestResource", "AsyncIngestResource"]


class IngestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngestResourceWithRawResponse:
        return IngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestResourceWithStreamingResponse:
        return IngestResourceWithStreamingResponse(self)

    def units(
        self,
        *,
        category: str,
        input: int,
        output: int,
        resource: str,
        budget_ids: list[str] | NotGiven = NOT_GIVEN,
        request_tags: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyResult:
        """
        Ingest a request

        Args:
          category (str): The name of the category
          resource (str): The name of the resource.
          input (int): The number of input units
          output (int): The number of output units
          budget_ids (list[str], optional): The budget IDs to associate with the request. Defaults to None.
          request_tags (list[str], optional): The request tags to associate with the request. Defaults to None.
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        valid_ids_str: str | NotGiven = NOT_GIVEN
        valid_tags_str: str | NotGiven = NOT_GIVEN

        if isinstance(budget_ids, NotGiven):
            valid_ids_str = NOT_GIVEN
        elif not isinstance(budget_ids, list): # type: ignore
            raise TypeError("budget_ids must be a list")
        else:
            # Proceed with the list comprehension if budget_ids is not NotGiven
            valid_ids = [id.strip() for id in budget_ids if id.strip()]
            valid_ids_str = ",".join(valid_ids) if valid_ids else NOT_GIVEN

        if isinstance(request_tags, NotGiven):
            valid_tags_str = NOT_GIVEN
        elif not isinstance(request_tags, list): # type: ignore
            raise TypeError("request_tags must be a list")
        else:
            # Proceed with the list comprehension if budget_ids is not NotGiven
            valid_tags = [tag.strip() for tag in request_tags if tag.strip()]
            valid_tags_str = ",".join(valid_tags) if valid_tags else NOT_GIVEN

        extra_headers = {
            **strip_not_given(
                {
                    "xProxy-Budget-IDs": valid_ids_str,
                    "xProxy-Request-Tags": valid_tags_str,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/api/v1/ingest",
            body=maybe_transform(
                {
                    "category": category,
                    "input": input,
                    "output": output,
                    "resource": resource,
                },
                ingest_units_params.IngestUnitsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyResult,
        )


class AsyncIngestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngestResourceWithRawResponse:
        return AsyncIngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestResourceWithStreamingResponse:
        return AsyncIngestResourceWithStreamingResponse(self)

    async def units(
        self,
        *,
        category: str,
        input: int,
        output: int,
        resource: str,
        budget_ids: list[str] | NotGiven = NOT_GIVEN,
        request_tags: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyResult:
        """
        Ingest a request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        valid_ids_str: str | NotGiven = NOT_GIVEN
        valid_tags_str: str | NotGiven = NOT_GIVEN

        if isinstance(budget_ids, NotGiven):
            valid_ids_str = NOT_GIVEN
        else:
            # Proceed with the list comprehension if budget_ids is not NotGiven
            valid_ids = [id.strip() for id in budget_ids if id.strip()]
            valid_ids_str = ",".join(valid_ids) if valid_ids else NOT_GIVEN
        if isinstance(request_tags, NotGiven):
            valid_tags_str = NOT_GIVEN
        else:
            # Proceed with the list comprehension if budget_ids is not NotGiven
            valid_tags = [tag.strip() for tag in request_tags if tag.strip()]
            valid_tags_str = ",".join(valid_tags) if valid_tags else NOT_GIVEN

        extra_headers = {
            **strip_not_given(
                {
                    "xProxy-Budget-IDs": valid_ids_str,
                    "xProxy-Request-Tags": valid_tags_str,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/api/v1/ingest",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "input": input,
                    "output": output,
                    "resource": resource,
                },
                ingest_units_params.IngestUnitsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyResult,
        )


class IngestResourceWithRawResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.units = to_raw_response_wrapper(
            ingest.units,
        )


class AsyncIngestResourceWithRawResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.units = async_to_raw_response_wrapper(
            ingest.units,
        )


class IngestResourceWithStreamingResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.units = to_streamed_response_wrapper(
            ingest.units,
        )


class AsyncIngestResourceWithStreamingResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.units = async_to_streamed_response_wrapper(
            ingest.units,
        )
