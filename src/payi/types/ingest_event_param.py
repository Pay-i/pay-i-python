# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IngestEventParam", "Units"]


class Units(TypedDict, total=False):
    input: int

    output: int


class IngestEventParam(TypedDict, total=False):
    category: Required[str]

    resource: Required[str]

    units: Required[Dict[str, Units]]

    budget_ids: Optional[List[str]]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    experience_id: Optional[str]

    experience_name: Optional[str]

    provisioned_resource_name: Optional[str]

    request_tags: Optional[List[str]]

    user_id: Optional[str]
