# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IngestUnitsParams"]


class IngestUnitsParams(TypedDict, total=False):
    category: Required[str]

    input: Required[int]

    output: Required[int]

    resource: Required[str]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    provisioned_resource_name: Optional[str]

    x_proxy_budget_ids: Annotated[str, PropertyInfo(alias="xProxy-Budget-IDs")]

    x_proxy_experience_id: Annotated[str, PropertyInfo(alias="xProxy-Experience-Id")]

    x_proxy_request_tags: Annotated[str, PropertyInfo(alias="xProxy-Request-Tags")]

    x_proxy_user_id: Annotated[str, PropertyInfo(alias="xProxy-User-ID")]
