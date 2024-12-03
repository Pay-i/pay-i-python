# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from payi.types import ExperienceInstanceResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        experience = client.experiences.create(
            "experience_name",
        )
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.experiences.with_raw_response.create(
            "experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.experiences.with_streaming_response.create(
            "experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            client.experiences.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Payi) -> None:
        experience = client.experiences.retrieve(
            "experience_id",
        )
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Payi) -> None:
        response = client.experiences.with_raw_response.retrieve(
            "experience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Payi) -> None:
        with client.experiences.with_streaming_response.retrieve(
            "experience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_id` but received ''"):
            client.experiences.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Payi) -> None:
        experience = client.experiences.delete(
            "experience_id",
        )
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Payi) -> None:
        response = client.experiences.with_raw_response.delete(
            "experience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = response.parse()
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Payi) -> None:
        with client.experiences.with_streaming_response.delete(
            "experience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = response.parse()
            assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_id` but received ''"):
            client.experiences.with_raw_response.delete(
                "",
            )


class TestAsyncExperiences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        experience = await async_client.experiences.create(
            "experience_name",
        )
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.with_raw_response.create(
            "experience_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.with_streaming_response.create(
            "experience_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_name` but received ''"):
            await async_client.experiences.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPayi) -> None:
        experience = await async_client.experiences.retrieve(
            "experience_id",
        )
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.with_raw_response.retrieve(
            "experience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.with_streaming_response.retrieve(
            "experience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_id` but received ''"):
            await async_client.experiences.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPayi) -> None:
        experience = await async_client.experiences.delete(
            "experience_id",
        )
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPayi) -> None:
        response = await async_client.experiences.with_raw_response.delete(
            "experience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experience = await response.parse()
        assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPayi) -> None:
        async with async_client.experiences.with_streaming_response.delete(
            "experience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experience = await response.parse()
            assert_matches_type(ExperienceInstanceResponse, experience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experience_id` but received ''"):
            await async_client.experiences.with_raw_response.delete(
                "",
            )
