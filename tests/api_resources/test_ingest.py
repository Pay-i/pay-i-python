# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from payi.types import ProxyResult
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIngest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_units(self, client: Payi) -> None:
        ingest = client.ingest.units(
            category="x",
            input=1,
            output=1,
            resource="x",
        )
        assert_matches_type(ProxyResult, ingest, path=["response"])

    @parametrize
    def test_method_units_with_all_params(self, client: Payi) -> None:
        ingest = client.ingest.units(
            category="x",
            input=1,
            output=1,
            resource="x",
            budget_ids=["budgetId1", "budgetId_2"],
            request_tags=["requestTag1", "request_tag_2"],
        )
        assert_matches_type(ProxyResult, ingest, path=["response"])

    @parametrize
    def test_raw_response_units(self, client: Payi) -> None:
        response = client.ingest.with_raw_response.units(
            category="x",
            input=1,
            output=1,
            resource="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = response.parse()
        assert_matches_type(ProxyResult, ingest, path=["response"])

    @parametrize
    def test_streaming_response_units(self, client: Payi) -> None:
        with client.ingest.with_streaming_response.units(
            category="x",
            input=1,
            output=1,
            resource="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = response.parse()
            assert_matches_type(ProxyResult, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIngest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_units(self, async_client: AsyncPayi) -> None:
        ingest = await async_client.ingest.units(
            category="x",
            input=1,
            output=1,
            resource="x",
        )
        assert_matches_type(ProxyResult, ingest, path=["response"])

    @parametrize
    async def test_method_units_with_all_params(self, async_client: AsyncPayi) -> None:
        ingest = await async_client.ingest.units(
            category="x",
            input=1,
            output=1,
            resource="x",
            budget_ids=["budgetId1", "budgetId_2"],
            request_tags=["requestTag1", "request_tag_2"],
        )
        assert_matches_type(ProxyResult, ingest, path=["response"])

    @parametrize
    async def test_raw_response_units(self, async_client: AsyncPayi) -> None:
        response = await async_client.ingest.with_raw_response.units(
            category="x",
            input=1,
            output=1,
            resource="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = await response.parse()
        assert_matches_type(ProxyResult, ingest, path=["response"])

    @parametrize
    async def test_streaming_response_units(self, async_client: AsyncPayi) -> None:
        async with async_client.ingest.with_streaming_response.units(
            category="x",
            input=1,
            output=1,
            resource="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = await response.parse()
            assert_matches_type(ProxyResult, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True
