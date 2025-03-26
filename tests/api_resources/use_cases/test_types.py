# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from tests.utils import assert_matches_type
from payi.types.use_cases import UseCaseType, TypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        type = client.use_cases.types.create(
            description="x",
            name="x",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Payi) -> None:
        type = client.use_cases.types.create(
            description="x",
            name="x",
            limit_config={
                "max": 0,
                "limit_tags": ["tag1", "tag2"],
                "limit_type": "block",
                "threshold": 0,
            },
            logging_enabled=True,
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.use_cases.types.with_raw_response.create(
            description="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.use_cases.types.with_streaming_response.create(
            description="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Payi) -> None:
        type = client.use_cases.types.retrieve(
            "use_case_name",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Payi) -> None:
        response = client.use_cases.types.with_raw_response.retrieve(
            "use_case_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Payi) -> None:
        with client.use_cases.types.with_streaming_response.retrieve(
            "use_case_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `use_case_name` but received ''"):
            client.use_cases.types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Payi) -> None:
        type = client.use_cases.types.update(
            use_case_name="use_case_name",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Payi) -> None:
        type = client.use_cases.types.update(
            use_case_name="use_case_name",
            description="description",
            logging_enabled=True,
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Payi) -> None:
        response = client.use_cases.types.with_raw_response.update(
            use_case_name="use_case_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Payi) -> None:
        with client.use_cases.types.with_streaming_response.update(
            use_case_name="use_case_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `use_case_name` but received ''"):
            client.use_cases.types.with_raw_response.update(
                use_case_name="",
            )

    @parametrize
    def test_method_list(self, client: Payi) -> None:
        type = client.use_cases.types.list()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Payi) -> None:
        type = client.use_cases.types.list(
            use_case_name="use_case_name",
        )
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Payi) -> None:
        response = client.use_cases.types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Payi) -> None:
        with client.use_cases.types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(TypeListResponse, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Payi) -> None:
        type = client.use_cases.types.delete(
            "use_case_name",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Payi) -> None:
        response = client.use_cases.types.with_raw_response.delete(
            "use_case_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Payi) -> None:
        with client.use_cases.types.with_streaming_response.delete(
            "use_case_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `use_case_name` but received ''"):
            client.use_cases.types.with_raw_response.delete(
                "",
            )


class TestAsyncTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.create(
            description="x",
            name="x",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.create(
            description="x",
            name="x",
            limit_config={
                "max": 0,
                "limit_tags": ["tag1", "tag2"],
                "limit_type": "block",
                "threshold": 0,
            },
            logging_enabled=True,
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.use_cases.types.with_raw_response.create(
            description="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.use_cases.types.with_streaming_response.create(
            description="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.retrieve(
            "use_case_name",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPayi) -> None:
        response = await async_client.use_cases.types.with_raw_response.retrieve(
            "use_case_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPayi) -> None:
        async with async_client.use_cases.types.with_streaming_response.retrieve(
            "use_case_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `use_case_name` but received ''"):
            await async_client.use_cases.types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.update(
            use_case_name="use_case_name",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.update(
            use_case_name="use_case_name",
            description="description",
            logging_enabled=True,
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPayi) -> None:
        response = await async_client.use_cases.types.with_raw_response.update(
            use_case_name="use_case_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPayi) -> None:
        async with async_client.use_cases.types.with_streaming_response.update(
            use_case_name="use_case_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `use_case_name` but received ''"):
            await async_client.use_cases.types.with_raw_response.update(
                use_case_name="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.list()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.list(
            use_case_name="use_case_name",
        )
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPayi) -> None:
        response = await async_client.use_cases.types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPayi) -> None:
        async with async_client.use_cases.types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(TypeListResponse, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPayi) -> None:
        type = await async_client.use_cases.types.delete(
            "use_case_name",
        )
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPayi) -> None:
        response = await async_client.use_cases.types.with_raw_response.delete(
            "use_case_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(UseCaseType, type, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPayi) -> None:
        async with async_client.use_cases.types.with_streaming_response.delete(
            "use_case_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(UseCaseType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `use_case_name` but received ''"):
            await async_client.use_cases.types.with_raw_response.delete(
                "",
            )
