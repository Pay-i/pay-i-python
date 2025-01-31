# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from tests.utils import assert_matches_type
from payi.types.experiences import (
    ExperienceType,
    TypeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        type = client.experiences.types.create(
            description="x",
            name="x",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Payi) -> None:
        type = client.experiences.types.create(
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
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.experiences.types.with_raw_response.create(
            description="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.experiences.types.with_streaming_response.create(
            description="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Payi) -> None:
        type = client.experiences.types.retrieve(
            "experience_name",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Payi) -> None:
        response = client.experiences.types.with_raw_response.retrieve(
            "experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Payi) -> None:
        with client.experiences.types.with_streaming_response.retrieve(
            "experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            client.experiences.types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Payi) -> None:
        type = client.experiences.types.update(
            experience_name="experience_name",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Payi) -> None:
        type = client.experiences.types.update(
            experience_name="experience_name",
            description="description",
            logging_enabled=True,
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Payi) -> None:
        response = client.experiences.types.with_raw_response.update(
            experience_name="experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Payi) -> None:
        with client.experiences.types.with_streaming_response.update(
            experience_name="experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            client.experiences.types.with_raw_response.update(
                experience_name="",
            )

    @parametrize
    def test_method_list(self, client: Payi) -> None:
        type = client.experiences.types.list()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Payi) -> None:
        type = client.experiences.types.list(
            name="name",
        )
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Payi) -> None:
        response = client.experiences.types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Payi) -> None:
        with client.experiences.types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(TypeListResponse, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Payi) -> None:
        type = client.experiences.types.delete(
            "experience_name",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Payi) -> None:
        response = client.experiences.types.with_raw_response.delete(
            "experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Payi) -> None:
        with client.experiences.types.with_streaming_response.delete(
            "experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            client.experiences.types.with_raw_response.delete(
                "",
            )


class TestAsyncTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.create(
            description="x",
            name="x",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.create(
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
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.types.with_raw_response.create(
            description="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.types.with_streaming_response.create(
            description="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.retrieve(
            "experience_name",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.types.with_raw_response.retrieve(
            "experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.types.with_streaming_response.retrieve(
            "experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            await async_client.experiences.types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.update(
            experience_name="experience_name",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.update(
            experience_name="experience_name",
            description="description",
            logging_enabled=True,
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.types.with_raw_response.update(
            experience_name="experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.types.with_streaming_response.update(
            experience_name="experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            await async_client.experiences.types.with_raw_response.update(
                experience_name="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.list()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.list(
            name="name",
        )
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(TypeListResponse, type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(TypeListResponse, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPayi) -> None:
        type = await async_client.experiences.types.delete(
            "experience_name",
        )
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.types.with_raw_response.delete(
            "experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type = await response.parse()
        assert_matches_type(ExperienceType, type, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.types.with_streaming_response.delete(
            "experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type = await response.parse()
            assert_matches_type(ExperienceType, type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            await async_client.experiences.types.with_raw_response.delete(
                "",
            )
