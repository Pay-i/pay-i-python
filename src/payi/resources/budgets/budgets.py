# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...types import budget_list_params, budget_create_params, budget_update_params
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
from ..._base_client import (
    make_request_options,
)
from ...types.budget_response import BudgetResponse
from ...types.default_response import DefaultResponse
from ...types.paged_budget_list import PagedBudgetList
from ...types.budget_history_response import BudgetHistoryResponse

__all__ = ["BudgetsResource", "AsyncBudgetsResource"]


class BudgetsResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BudgetsResourceWithRawResponse:
        return BudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BudgetsResourceWithStreamingResponse:
        return BudgetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        budget_name: str,
        max: float,
        base_cost_estimate: Literal["max"] | NotGiven = NOT_GIVEN,
        budget_response_type: Literal["block", "allow"] | NotGiven = NOT_GIVEN,
        budget_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        budget_type: Literal["conservative", "liberal"] | NotGiven = NOT_GIVEN,
        currency: Literal["usd"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetResponse:
        """
        Create a Budget

        Args:
          budget_name (str): The name of the budget.
          max (float): The maximum budget amount.
          base_cost_estimate (Union[float, Literal['max']], optional): The base cost estimate. Defaults to 'max'.
          budget_response_type (Literal['block', 'allow'], optional): The budget response type. Defaults to 'block'.
          budget_tags (Union[List[str], None], optional): List of budget tags. Defaults to None.
          budget_type (Literal['conservative', 'liberal'], optional): The budget type. Defaults to 'conservative'.
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        return self._post(
            "/api/v1/budgets",
            body=maybe_transform(
                {
                    "budget_name": budget_name,
                    "max": max,
                    "base_cost_estimate": base_cost_estimate,
                    "budget_response_type": budget_response_type,
                    "budget_tags": budget_tags,
                    "budget_type": budget_type,
                    "currency": currency,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetResponse,
        )

    def retrieve(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetResponse:
        """
        Get a Budget's details

        Args:
          budget_id (str): The ID of the budget.
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return self._get(
            f"/api/v1/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetResponse,
        )

    def update(
        self,
        budget_id: str,
        *,
        budget_name: str,
        max: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetResponse:
        """
        Update a Budget

        Args:
          budget_id (str): The ID of the budget.
          budget_name (Union[str, optional]): The updated name of the budget. Defaults to None.
          max (Union[float, optional])): The maximum budget amount. Defaults to None.
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return self._put(
            f"/api/v1/budgets/{budget_id}",
            body=maybe_transform(
                {
                    "budget_name": budget_name,
                    "max": max,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetResponse,
        )

    def list(
        self,
        *,
        budget_name: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort_ascending: bool | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagedBudgetList:
        """
        Get all Budgets

        Args:
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        return self._get(
            "/api/v1/budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "budget_name": budget_name,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_ascending": sort_ascending,
                        "sort_by": sort_by,
                        "tags": tags,
                    },
                    budget_list_params.BudgetListParams,
                ),
            ),
            cast_to=PagedBudgetList,
        )

    def delete(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultResponse:
        """
        Delete a Budget

        Args:
          budget_id (str): The ID of the budget.
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return self._delete(
            f"/api/v1/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultResponse,
        )

    def reset(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetHistoryResponse:
        """
        Reset the Budget

        Args:
          budget_id (str): The ID of the budget.
          extra_headers (Dict[str, str], optional): Additional headers for the request. Defaults to None.
          extra_query (Dict[str, str], optional): Additional query parameters. Defaults to None.
          extra_body (Dict[str, Any], optional): Additional body parameters. Defaults to None.
          timeout (Union[float, None], optional): The timeout for the request in seconds. Defaults to None.
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return self._post(
            f"/api/v1/budgets/{budget_id}/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetHistoryResponse,
        )


class AsyncBudgetsResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBudgetsResourceWithRawResponse:
        return AsyncBudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBudgetsResourceWithStreamingResponse:
        return AsyncBudgetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        budget_name: str,
        max: float,
        base_cost_estimate: Literal["max"] | NotGiven = NOT_GIVEN,
        budget_response_type: Literal["block", "allow"] | NotGiven = NOT_GIVEN,
        budget_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        budget_type: Literal["conservative", "liberal"] | NotGiven = NOT_GIVEN,
        currency: Literal["usd"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetResponse:
        """
        Create a Budget

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/budgets",
            body=await async_maybe_transform(
                {
                    "budget_name": budget_name,
                    "max": max,
                    "base_cost_estimate": base_cost_estimate,
                    "budget_response_type": budget_response_type,
                    "budget_tags": budget_tags,
                    "budget_type": budget_type,
                    "currency": currency,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetResponse,
        )

    async def retrieve(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetResponse:
        """
        Get a Budget's details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return await self._get(
            f"/api/v1/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetResponse,
        )

    async def update(
        self,
        budget_id: str,
        *,
        budget_name: str,
        max: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetResponse:
        """
        Update a Budget

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return await self._put(
            f"/api/v1/budgets/{budget_id}",
            body=await async_maybe_transform(
                {
                    "budget_name": budget_name,
                    "max": max,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetResponse,
        )

    async def list(
        self,
        *,
        budget_name: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort_ascending: bool | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagedBudgetList:
        """
        Get all Budgets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "budget_name": budget_name,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_ascending": sort_ascending,
                        "sort_by": sort_by,
                        "tags": tags,
                    },
                    budget_list_params.BudgetListParams,
                ),
            ),
            cast_to=PagedBudgetList,
        )

    async def delete(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultResponse:
        """
        Delete a Budget

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return await self._delete(
            f"/api/v1/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultResponse,
        )

    async def reset(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetHistoryResponse:
        """
        Reset the Budget

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return await self._post(
            f"/api/v1/budgets/{budget_id}/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetHistoryResponse,
        )


class BudgetsResourceWithRawResponse:
    def __init__(self, budgets: BudgetsResource) -> None:
        self._budgets = budgets

        self.create = to_raw_response_wrapper(
            budgets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            budgets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            budgets.update,
        )
        self.list = to_raw_response_wrapper(
            budgets.list,
        )
        self.delete = to_raw_response_wrapper(
            budgets.delete,
        )
        self.reset = to_raw_response_wrapper(
            budgets.reset,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._budgets.tags)


class AsyncBudgetsResourceWithRawResponse:
    def __init__(self, budgets: AsyncBudgetsResource) -> None:
        self._budgets = budgets

        self.create = async_to_raw_response_wrapper(
            budgets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            budgets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            budgets.update,
        )
        self.list = async_to_raw_response_wrapper(
            budgets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            budgets.delete,
        )
        self.reset = async_to_raw_response_wrapper(
            budgets.reset,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._budgets.tags)


class BudgetsResourceWithStreamingResponse:
    def __init__(self, budgets: BudgetsResource) -> None:
        self._budgets = budgets

        self.create = to_streamed_response_wrapper(
            budgets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            budgets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            budgets.update,
        )
        self.list = to_streamed_response_wrapper(
            budgets.list,
        )
        self.delete = to_streamed_response_wrapper(
            budgets.delete,
        )
        self.reset = to_streamed_response_wrapper(
            budgets.reset,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._budgets.tags)


class AsyncBudgetsResourceWithStreamingResponse:
    def __init__(self, budgets: AsyncBudgetsResource) -> None:
        self._budgets = budgets

        self.create = async_to_streamed_response_wrapper(
            budgets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            budgets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            budgets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            budgets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            budgets.delete,
        )
        self.reset = async_to_streamed_response_wrapper(
            budgets.reset,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._budgets.tags)
