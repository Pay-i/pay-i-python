# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .pay_i_common_models_api_router_header_info_param import PayICommonModelsAPIRouterHeaderInfoParam

__all__ = ["IngestUnitsParams", "Units"]


class IngestUnitsParams(TypedDict, total=False):
    category: Required[str]

    resource: Required[str]

    units: Required[Dict[str, Units]]

    end_to_end_latency_ms: Optional[int]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    experience_properties: Optional[Dict[str, str]]

    http_status_code: Optional[int]

    properties: Optional[Dict[str, str]]

    provider_request_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]]

    provider_request_json: Optional[str]

    provider_response_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]]

    provider_response_json: Union[str, List[str], None]

    provider_uri: Optional[str]

    time_to_first_token_ms: Optional[int]

    x_proxy_experience_id: Annotated[str, PropertyInfo(alias="xProxy-Experience-ID")]

    x_proxy_experience_name: Annotated[str, PropertyInfo(alias="xProxy-Experience-Name")]

    x_proxy_limit_ids: Annotated[str, PropertyInfo(alias="xProxy-Limit-IDs")]

    x_proxy_request_tags: Annotated[str, PropertyInfo(alias="xProxy-Request-Tags")]

    x_proxy_user_id: Annotated[str, PropertyInfo(alias="xProxy-User-ID")]


class Units(TypedDict, total=False):
    input: int

    output: int
