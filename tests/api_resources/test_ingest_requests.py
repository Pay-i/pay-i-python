# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from payi import Payi, AsyncPayi
from payi.types import SuccessfulProxyResult
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIngestRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Payi) -> None:
        ingest_request = client.ingest_requests.create()
        assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Payi) -> None:
        ingest_request = client.ingest_requests.create(
            category="string",
            resource="string",
            units={
                "input": 0,
                "output": 0,
            },
            x_proxy_budget_ids="budgetId1, budgetId_2",
            x_proxy_request_tags="requestTag1, request_tag_2",
        )
        assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Payi) -> None:
        response = client.ingest_requests.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest_request = response.parse()
        assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Payi) -> None:
        with client.ingest_requests.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest_request = response.parse()
            assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIngestRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPayi) -> None:
        ingest_request = await async_client.ingest_requests.create()
        assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPayi) -> None:
        ingest_request = await async_client.ingest_requests.create(
            category="string",
            resource="string",
            units={
                "input": 0,
                "output": 0,
            },
            x_proxy_budget_ids="budgetId1, budgetId_2",
            x_proxy_request_tags="requestTag1, request_tag_2",
        )
        assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPayi) -> None:
        response = await async_client.ingest_requests.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest_request = await response.parse()
        assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPayi) -> None:
        async with async_client.ingest_requests.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest_request = await response.parse()
            assert_matches_type(SuccessfulProxyResult, ingest_request, path=["response"])

        assert cast(Any, response.is_closed) is True
