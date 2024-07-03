# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from payi.types import (
    BudgetResponse,
    DefaultResponse,
    PagedBudgetList,
    BudgetHistoryResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBudgets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        budget = client.budgets.create(
            budget_name="x",
            max=1,
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Payi) -> None:
        budget = client.budgets.create(
            budget_name="x",
            max=1,
            base_cost_estimate="max",
            budget_response_type="block",
            budget_tags=["tag1", "tag2"],
            budget_type="conservative",
            currency="usd",
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.budgets.with_raw_response.create(
            budget_name="x",
            max=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.budgets.with_streaming_response.create(
            budget_name="x",
            max=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Payi) -> None:
        budget = client.budgets.retrieve(
            "string",
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Payi) -> None:
        response = client.budgets.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Payi) -> None:
        with client.budgets.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Payi) -> None:
        budget = client.budgets.update(
            "string",
            budget_name="x",
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Payi) -> None:
        budget = client.budgets.update(
            "string",
            budget_name="x",
            max=1,
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Payi) -> None:
        response = client.budgets.with_raw_response.update(
            "string",
            budget_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Payi) -> None:
        with client.budgets.with_streaming_response.update(
            "string",
            budget_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.update(
                "",
                budget_name="x",
            )

    @parametrize
    def test_method_list(self, client: Payi) -> None:
        budget = client.budgets.list()
        assert_matches_type(PagedBudgetList, budget, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Payi) -> None:
        budget = client.budgets.list(
            budget_name="string",
            page_number=0,
            page_size=0,
            sort_ascending=True,
            sort_by="string",
            tags="string",
        )
        assert_matches_type(PagedBudgetList, budget, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Payi) -> None:
        response = client.budgets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(PagedBudgetList, budget, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Payi) -> None:
        with client.budgets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(PagedBudgetList, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Payi) -> None:
        budget = client.budgets.delete(
            "string",
        )
        assert_matches_type(DefaultResponse, budget, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Payi) -> None:
        response = client.budgets.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(DefaultResponse, budget, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Payi) -> None:
        with client.budgets.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(DefaultResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_reset(self, client: Payi) -> None:
        budget = client.budgets.reset(
            "string",
        )
        assert_matches_type(BudgetHistoryResponse, budget, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: Payi) -> None:
        response = client.budgets.with_raw_response.reset(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetHistoryResponse, budget, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: Payi) -> None:
        with client.budgets.with_streaming_response.reset(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetHistoryResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.reset(
                "",
            )


class TestAsyncBudgets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.create(
            budget_name="x",
            max=1,
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.create(
            budget_name="x",
            max=1,
            base_cost_estimate="max",
            budget_response_type="block",
            budget_tags=["tag1", "tag2"],
            budget_type="conservative",
            currency="usd",
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.with_raw_response.create(
            budget_name="x",
            max=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.with_streaming_response.create(
            budget_name="x",
            max=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.retrieve(
            "string",
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.update(
            "string",
            budget_name="x",
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.update(
            "string",
            budget_name="x",
            max=1,
        )
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.with_raw_response.update(
            "string",
            budget_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetResponse, budget, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.with_streaming_response.update(
            "string",
            budget_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.update(
                "",
                budget_name="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.list()
        assert_matches_type(PagedBudgetList, budget, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.list(
            budget_name="string",
            page_number=0,
            page_size=0,
            sort_ascending=True,
            sort_by="string",
            tags="string",
        )
        assert_matches_type(PagedBudgetList, budget, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(PagedBudgetList, budget, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(PagedBudgetList, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.delete(
            "string",
        )
        assert_matches_type(DefaultResponse, budget, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(DefaultResponse, budget, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(DefaultResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncPayi) -> None:
        budget = await async_client.budgets.reset(
            "string",
        )
        assert_matches_type(BudgetHistoryResponse, budget, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.with_raw_response.reset(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetHistoryResponse, budget, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.with_streaming_response.reset(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetHistoryResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.reset(
                "",
            )
