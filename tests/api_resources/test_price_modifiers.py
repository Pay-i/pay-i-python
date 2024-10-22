# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from payi.types import (
    PriceModifier,
    PriceModifierRetrieveResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPriceModifiers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        price_modifier = client.price_modifiers.create(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.price_modifiers.with_raw_response.create(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_modifier = response.parse()
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.price_modifiers.with_streaming_response.create(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_modifier = response.parse()
            assert_matches_type(PriceModifier, price_modifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Payi) -> None:
        price_modifier = client.price_modifiers.retrieve(
            "billing_model_id",
        )
        assert_matches_type(PriceModifierRetrieveResponse, price_modifier, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Payi) -> None:
        response = client.price_modifiers.with_raw_response.retrieve(
            "billing_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_modifier = response.parse()
        assert_matches_type(PriceModifierRetrieveResponse, price_modifier, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Payi) -> None:
        with client.price_modifiers.with_streaming_response.retrieve(
            "billing_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_modifier = response.parse()
            assert_matches_type(PriceModifierRetrieveResponse, price_modifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            client.price_modifiers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Payi) -> None:
        price_modifier = client.price_modifiers.update(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Payi) -> None:
        response = client.price_modifiers.with_raw_response.update(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_modifier = response.parse()
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Payi) -> None:
        with client.price_modifiers.with_streaming_response.update(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_modifier = response.parse()
            assert_matches_type(PriceModifier, price_modifier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPriceModifiers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        price_modifier = await async_client.price_modifiers.create(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.price_modifiers.with_raw_response.create(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_modifier = await response.parse()
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.price_modifiers.with_streaming_response.create(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_modifier = await response.parse()
            assert_matches_type(PriceModifier, price_modifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPayi) -> None:
        price_modifier = await async_client.price_modifiers.retrieve(
            "billing_model_id",
        )
        assert_matches_type(PriceModifierRetrieveResponse, price_modifier, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPayi) -> None:
        response = await async_client.price_modifiers.with_raw_response.retrieve(
            "billing_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_modifier = await response.parse()
        assert_matches_type(PriceModifierRetrieveResponse, price_modifier, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPayi) -> None:
        async with async_client.price_modifiers.with_streaming_response.retrieve(
            "billing_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_modifier = await response.parse()
            assert_matches_type(PriceModifierRetrieveResponse, price_modifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            await async_client.price_modifiers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPayi) -> None:
        price_modifier = await async_client.price_modifiers.update(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPayi) -> None:
        response = await async_client.price_modifiers.with_raw_response.update(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_modifier = await response.parse()
        assert_matches_type(PriceModifier, price_modifier, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPayi) -> None:
        async with async_client.price_modifiers.with_streaming_response.update(
            billing_model_id="x",
            category="x",
            price_modifier=0,
            resource="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_modifier = await response.parse()
            assert_matches_type(PriceModifier, price_modifier, path=["response"])

        assert cast(Any, response.is_closed) is True
