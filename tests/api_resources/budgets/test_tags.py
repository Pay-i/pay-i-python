# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from tests.utils import assert_matches_type
from payi.types.budgets import (
    TagListResponse,
    TagCreateResponse,
    TagDeleteResponse,
    TagRemoveResponse,
    TagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        tag = client.budgets.tags.create(
            "string",
            budget_tags=["tag1", "tag2"],
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.budgets.tags.with_raw_response.create(
            "string",
            budget_tags=["tag1", "tag2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.budgets.tags.with_streaming_response.create(
            "string",
            budget_tags=["tag1", "tag2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.tags.with_raw_response.create(
                "",
                budget_tags=["tag1", "tag2"],
            )

    @parametrize
    def test_method_update(self, client: Payi) -> None:
        tag = client.budgets.tags.update(
            "string",
            budget_tags=["tag1", "tag2"],
        )
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Payi) -> None:
        response = client.budgets.tags.with_raw_response.update(
            "string",
            budget_tags=["tag1", "tag2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Payi) -> None:
        with client.budgets.tags.with_streaming_response.update(
            "string",
            budget_tags=["tag1", "tag2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagUpdateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.tags.with_raw_response.update(
                "",
                budget_tags=["tag1", "tag2"],
            )

    @parametrize
    def test_method_list(self, client: Payi) -> None:
        tag = client.budgets.tags.list(
            "string",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Payi) -> None:
        response = client.budgets.tags.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Payi) -> None:
        with client.budgets.tags.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.tags.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Payi) -> None:
        tag = client.budgets.tags.delete(
            "string",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Payi) -> None:
        response = client.budgets.tags.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Payi) -> None:
        with client.budgets.tags.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.tags.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_remove(self, client: Payi) -> None:
        tag = client.budgets.tags.remove(
            "string",
            budget_tags=["tag1", "tag2"],
        )
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Payi) -> None:
        response = client.budgets.tags.with_raw_response.remove(
            "string",
            budget_tags=["tag1", "tag2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Payi) -> None:
        with client.budgets.tags.with_streaming_response.remove(
            "string",
            budget_tags=["tag1", "tag2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagRemoveResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.tags.with_raw_response.remove(
                "",
                budget_tags=["tag1", "tag2"],
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        tag = await async_client.budgets.tags.create(
            "string",
            budget_tags=["tag1", "tag2"],
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.tags.with_raw_response.create(
            "string",
            budget_tags=["tag1", "tag2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.tags.with_streaming_response.create(
            "string",
            budget_tags=["tag1", "tag2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.tags.with_raw_response.create(
                "",
                budget_tags=["tag1", "tag2"],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPayi) -> None:
        tag = await async_client.budgets.tags.update(
            "string",
            budget_tags=["tag1", "tag2"],
        )
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.tags.with_raw_response.update(
            "string",
            budget_tags=["tag1", "tag2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagUpdateResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.tags.with_streaming_response.update(
            "string",
            budget_tags=["tag1", "tag2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagUpdateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.tags.with_raw_response.update(
                "",
                budget_tags=["tag1", "tag2"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPayi) -> None:
        tag = await async_client.budgets.tags.list(
            "string",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.tags.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.tags.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.tags.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPayi) -> None:
        tag = await async_client.budgets.tags.delete(
            "string",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.tags.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.tags.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.tags.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncPayi) -> None:
        tag = await async_client.budgets.tags.remove(
            "string",
            budget_tags=["tag1", "tag2"],
        )
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncPayi) -> None:
        response = await async_client.budgets.tags.with_raw_response.remove(
            "string",
            budget_tags=["tag1", "tag2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncPayi) -> None:
        async with async_client.budgets.tags.with_streaming_response.remove(
            "string",
            budget_tags=["tag1", "tag2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagRemoveResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.tags.with_raw_response.remove(
                "",
                budget_tags=["tag1", "tag2"],
            )
