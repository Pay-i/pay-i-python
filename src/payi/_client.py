# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PayiError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Payi",
    "AsyncPayi",
    "Client",
    "AsyncClient",
]


class Payi(SyncAPIClient):
    budgets: resources.BudgetsResource
    ingest: resources.IngestResource
    categories: resources.CategoriesResource
    experiences: resources.ExperiencesResource
    csat: resources.CsatResource
    billing_models: resources.BillingModelsResource
    price_modifiers: resources.PriceModifiersResource
    with_raw_response: PayiWithRawResponse
    with_streaming_response: PayiWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous payi client instance.

        This automatically infers the `api_key` argument from the `PAYI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PAYI_API_KEY")
        if api_key is None:
            raise PayiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PAYI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PAYI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.pay-i.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.budgets = resources.BudgetsResource(self)
        self.ingest = resources.IngestResource(self)
        self.categories = resources.CategoriesResource(self)
        self.experiences = resources.ExperiencesResource(self)
        self.csat = resources.CsatResource(self)
        self.billing_models = resources.BillingModelsResource(self)
        self.price_modifiers = resources.PriceModifiersResource(self)
        self.with_raw_response = PayiWithRawResponse(self)
        self.with_streaming_response = PayiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPayi(AsyncAPIClient):
    budgets: resources.AsyncBudgetsResource
    ingest: resources.AsyncIngestResource
    categories: resources.AsyncCategoriesResource
    experiences: resources.AsyncExperiencesResource
    csat: resources.AsyncCsatResource
    billing_models: resources.AsyncBillingModelsResource
    price_modifiers: resources.AsyncPriceModifiersResource
    with_raw_response: AsyncPayiWithRawResponse
    with_streaming_response: AsyncPayiWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async payi client instance.

        This automatically infers the `api_key` argument from the `PAYI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PAYI_API_KEY")
        if api_key is None:
            raise PayiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PAYI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PAYI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.pay-i.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.budgets = resources.AsyncBudgetsResource(self)
        self.ingest = resources.AsyncIngestResource(self)
        self.categories = resources.AsyncCategoriesResource(self)
        self.experiences = resources.AsyncExperiencesResource(self)
        self.csat = resources.AsyncCsatResource(self)
        self.billing_models = resources.AsyncBillingModelsResource(self)
        self.price_modifiers = resources.AsyncPriceModifiersResource(self)
        self.with_raw_response = AsyncPayiWithRawResponse(self)
        self.with_streaming_response = AsyncPayiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PayiWithRawResponse:
    def __init__(self, client: Payi) -> None:
        self.budgets = resources.BudgetsResourceWithRawResponse(client.budgets)
        self.ingest = resources.IngestResourceWithRawResponse(client.ingest)
        self.categories = resources.CategoriesResourceWithRawResponse(client.categories)
        self.experiences = resources.ExperiencesResourceWithRawResponse(client.experiences)
        self.csat = resources.CsatResourceWithRawResponse(client.csat)
        self.billing_models = resources.BillingModelsResourceWithRawResponse(client.billing_models)
        self.price_modifiers = resources.PriceModifiersResourceWithRawResponse(client.price_modifiers)


class AsyncPayiWithRawResponse:
    def __init__(self, client: AsyncPayi) -> None:
        self.budgets = resources.AsyncBudgetsResourceWithRawResponse(client.budgets)
        self.ingest = resources.AsyncIngestResourceWithRawResponse(client.ingest)
        self.categories = resources.AsyncCategoriesResourceWithRawResponse(client.categories)
        self.experiences = resources.AsyncExperiencesResourceWithRawResponse(client.experiences)
        self.csat = resources.AsyncCsatResourceWithRawResponse(client.csat)
        self.billing_models = resources.AsyncBillingModelsResourceWithRawResponse(client.billing_models)
        self.price_modifiers = resources.AsyncPriceModifiersResourceWithRawResponse(client.price_modifiers)


class PayiWithStreamedResponse:
    def __init__(self, client: Payi) -> None:
        self.budgets = resources.BudgetsResourceWithStreamingResponse(client.budgets)
        self.ingest = resources.IngestResourceWithStreamingResponse(client.ingest)
        self.categories = resources.CategoriesResourceWithStreamingResponse(client.categories)
        self.experiences = resources.ExperiencesResourceWithStreamingResponse(client.experiences)
        self.csat = resources.CsatResourceWithStreamingResponse(client.csat)
        self.billing_models = resources.BillingModelsResourceWithStreamingResponse(client.billing_models)
        self.price_modifiers = resources.PriceModifiersResourceWithStreamingResponse(client.price_modifiers)


class AsyncPayiWithStreamedResponse:
    def __init__(self, client: AsyncPayi) -> None:
        self.budgets = resources.AsyncBudgetsResourceWithStreamingResponse(client.budgets)
        self.ingest = resources.AsyncIngestResourceWithStreamingResponse(client.ingest)
        self.categories = resources.AsyncCategoriesResourceWithStreamingResponse(client.categories)
        self.experiences = resources.AsyncExperiencesResourceWithStreamingResponse(client.experiences)
        self.csat = resources.AsyncCsatResourceWithStreamingResponse(client.csat)
        self.billing_models = resources.AsyncBillingModelsResourceWithStreamingResponse(client.billing_models)
        self.price_modifiers = resources.AsyncPriceModifiersResourceWithStreamingResponse(client.price_modifiers)


Client = Payi

AsyncClient = AsyncPayi
