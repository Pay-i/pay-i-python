# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IngestUnitsParams", "Units"]


class IngestUnitsParams(TypedDict, total=False):
    category: Required[str]

    resource: Required[str]

    units: Required[Dict[str, Units]]

    end_to_end_latency_ms: Optional[int]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    http_status_code: Optional[int]

    provisioned_resource_name: Optional[str]

    time_to_first_token_ms: Optional[int]

    x_proxy_budget_ids: Annotated[str, PropertyInfo(alias="xProxy-Budget-IDs")]

    x_proxy_experience_id: Annotated[str, PropertyInfo(alias="xProxy-Experience-Id")]

    x_proxy_experience_name: Annotated[str, PropertyInfo(alias="xProxy-Experience-Name")]

    x_proxy_request_tags: Annotated[str, PropertyInfo(alias="xProxy-Request-Tags")]

    x_proxy_user_id: Annotated[str, PropertyInfo(alias="xProxy-User-ID")]


class Units(TypedDict, total=False):
    input: int

    output: int
