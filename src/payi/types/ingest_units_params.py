# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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

    budget_ids: Annotated[Union[list[str], None], PropertyInfo(alias="xProxy-Budget-IDs")]

    request_tags: Annotated[Union[list[str], None], PropertyInfo(alias="xProxy-Request-Tags")]

    experience_id: Annotated[Union[str, None], PropertyInfo(alias="xProxy-Experience-Id")]

    user_id: Annotated[Union[str, None], PropertyInfo(alias="xProxy-User-ID")]
