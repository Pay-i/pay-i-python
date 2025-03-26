# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .pay_i_common_models_api_router_header_info_param import PayICommonModelsAPIRouterHeaderInfoParam

__all__ = ["IngestEventParam", "Units"]


class Units(TypedDict, total=False):
    input: int

    output: int


class IngestEventParam(TypedDict, total=False):
    category: Required[str]

    resource: Required[str]

    units: Required[Dict[str, Units]]

    end_to_end_latency_ms: Optional[int]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    experience_id: Optional[str]

    experience_name: Optional[str]

    experience_properties: Optional[Dict[str, str]]

    experience_version: Optional[int]

    http_status_code: Optional[int]

    limit_ids: Optional[List[str]]

    properties: Optional[Dict[str, str]]

    provider_request_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]]

    provider_request_json: Optional[str]

    provider_response_headers: Optional[Iterable[PayICommonModelsAPIRouterHeaderInfoParam]]

    provider_response_id: Optional[str]

    provider_response_json: Union[str, List[str], None]

    provider_uri: Optional[str]

    request_tags: Optional[List[str]]

    time_to_first_token_ms: Optional[int]

    use_case_id: Optional[str]

    use_case_name: Optional[str]

    use_case_version: Optional[int]

    use_case_properties: Optional[Dict[str, str]]

    user_id: Optional[str]
