# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from payi.types import BillingModel, BillingModelListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        billing_model = client.billing_models.create(
            name="x",
            type="costplus",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Payi) -> None:
        billing_model = client.billing_models.create(
            name="x",
            type="costplus",
            default_price_modifier=0,
            prepaid_amount=0,
            prepaid_max=0,
            threshold=0,
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.billing_models.with_raw_response.create(
            name="x",
            type="costplus",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.billing_models.with_streaming_response.create(
            name="x",
            type="costplus",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Payi) -> None:
        billing_model = client.billing_models.retrieve(
            "billing_model_id",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Payi) -> None:
        response = client.billing_models.with_raw_response.retrieve(
            "billing_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Payi) -> None:
        with client.billing_models.with_streaming_response.retrieve(
            "billing_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            client.billing_models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Payi) -> None:
        billing_model = client.billing_models.update(
            billing_model_id="billing_model_id",
            type="costplus",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Payi) -> None:
        billing_model = client.billing_models.update(
            billing_model_id="billing_model_id",
            type="costplus",
            default_price_modifier=0,
            name="name",
            prepaid_amount=0,
            prepaid_max=0,
            threshold=0,
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Payi) -> None:
        response = client.billing_models.with_raw_response.update(
            billing_model_id="billing_model_id",
            type="costplus",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Payi) -> None:
        with client.billing_models.with_streaming_response.update(
            billing_model_id="billing_model_id",
            type="costplus",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            client.billing_models.with_raw_response.update(
                billing_model_id="",
                type="costplus",
            )

    @parametrize
    def test_method_list(self, client: Payi) -> None:
        billing_model = client.billing_models.list()
        assert_matches_type(BillingModelListResponse, billing_model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Payi) -> None:
        response = client.billing_models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = response.parse()
        assert_matches_type(BillingModelListResponse, billing_model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Payi) -> None:
        with client.billing_models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = response.parse()
            assert_matches_type(BillingModelListResponse, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_default(self, client: Payi) -> None:
        billing_model = client.billing_models.set_default(
            "billing_model_id",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_raw_response_set_default(self, client: Payi) -> None:
        response = client.billing_models.with_raw_response.set_default(
            "billing_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    def test_streaming_response_set_default(self, client: Payi) -> None:
        with client.billing_models.with_streaming_response.set_default(
            "billing_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_default(self, client: Payi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            client.billing_models.with_raw_response.set_default(
                "",
            )


class TestAsyncBillingModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.create(
            name="x",
            type="costplus",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.create(
            name="x",
            type="costplus",
            default_price_modifier=0,
            prepaid_amount=0,
            prepaid_max=0,
            threshold=0,
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.billing_models.with_raw_response.create(
            name="x",
            type="costplus",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = await response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.billing_models.with_streaming_response.create(
            name="x",
            type="costplus",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = await response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.retrieve(
            "billing_model_id",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPayi) -> None:
        response = await async_client.billing_models.with_raw_response.retrieve(
            "billing_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = await response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPayi) -> None:
        async with async_client.billing_models.with_streaming_response.retrieve(
            "billing_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = await response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            await async_client.billing_models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.update(
            billing_model_id="billing_model_id",
            type="costplus",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.update(
            billing_model_id="billing_model_id",
            type="costplus",
            default_price_modifier=0,
            name="name",
            prepaid_amount=0,
            prepaid_max=0,
            threshold=0,
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPayi) -> None:
        response = await async_client.billing_models.with_raw_response.update(
            billing_model_id="billing_model_id",
            type="costplus",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = await response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPayi) -> None:
        async with async_client.billing_models.with_streaming_response.update(
            billing_model_id="billing_model_id",
            type="costplus",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = await response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            await async_client.billing_models.with_raw_response.update(
                billing_model_id="",
                type="costplus",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.list()
        assert_matches_type(BillingModelListResponse, billing_model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPayi) -> None:
        response = await async_client.billing_models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = await response.parse()
        assert_matches_type(BillingModelListResponse, billing_model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPayi) -> None:
        async with async_client.billing_models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = await response.parse()
            assert_matches_type(BillingModelListResponse, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_default(self, async_client: AsyncPayi) -> None:
        billing_model = await async_client.billing_models.set_default(
            "billing_model_id",
        )
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_raw_response_set_default(self, async_client: AsyncPayi) -> None:
        response = await async_client.billing_models.with_raw_response.set_default(
            "billing_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_model = await response.parse()
        assert_matches_type(BillingModel, billing_model, path=["response"])

    @parametrize
    async def test_streaming_response_set_default(self, async_client: AsyncPayi) -> None:
        async with async_client.billing_models.with_streaming_response.set_default(
            "billing_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_model = await response.parse()
            assert_matches_type(BillingModel, billing_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_default(self, async_client: AsyncPayi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_model_id` but received ''"):
            await async_client.billing_models.with_raw_response.set_default(
                "",
            )
