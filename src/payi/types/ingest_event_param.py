# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IngestEventParam", "Units", "ProviderRequestHeader", "ProviderResponseHeader"]


class Units(TypedDict, total=False):
    input: int

    output: int


class ProviderRequestHeader(TypedDict, total=False):
    name: Required[str]

    value: Optional[str]


class ProviderResponseHeader(TypedDict, total=False):
    name: Required[str]

    value: Optional[str]


class IngestEventParam(TypedDict, total=False):
    category: Required[str]

    resource: Required[str]

    units: Required[Dict[str, Units]]

    csat_rating: Optional[int]

    end_to_end_latency_ms: Optional[int]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    experience_id: Optional[str]

    experience_name: Optional[str]

    experience_properties: Optional[Dict[str, str]]

    http_status_code: Optional[int]

    limit_ids: Optional[List[str]]

    properties: Optional[Dict[str, str]]

    provider_request_headers: Optional[Iterable[ProviderRequestHeader]]

    provider_request_json: Optional[str]

    provider_response_headers: Optional[Iterable[ProviderResponseHeader]]

    provider_response_json: Union[str, List[str], None]

    provider_uri: Optional[str]

    request_tags: Optional[List[str]]

    time_to_first_token_ms: Optional[int]

    user_id: Optional[str]
