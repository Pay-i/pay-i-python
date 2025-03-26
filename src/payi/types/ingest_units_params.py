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

    provider_response_id: Optional[str]

    provider_response_json: Union[str, List[str], None]

    provider_uri: Optional[str]

    time_to_first_token_ms: Optional[int]

    use_case_properties: Optional[Dict[str, str]]

    limit_ids: Annotated[Union[list[str], None], PropertyInfo(alias="xProxy-Limit-IDs")]

    request_tags: Annotated[Union[list[str], None], PropertyInfo(alias="xProxy-Request-Tags")]

    experience_name: Annotated[Union[str, None], PropertyInfo(alias="xProxy-Experience-Name")]

    experience_id: Annotated[Union[str, None], PropertyInfo(alias="xProxy-Experience-ID")]

    use_case_name: Annotated[Union[str, None], PropertyInfo(alias="xProxy-UseCase-Name")]

    use_case_id: Annotated[Union[str, None], PropertyInfo(alias="xProxy-UseCase-ID")]

    use_case_version: Annotated[Union[int, None], PropertyInfo(alias="xProxy-UseCase-Version")]

    resource_scope: Annotated[Union[str, None], PropertyInfo(alias="xProxy-Resource-Scope")]

    user_id: Annotated[Union[str, None], PropertyInfo(alias="xProxy-User-ID")]


class Units(TypedDict, total=False):
    input: int

    output: int
