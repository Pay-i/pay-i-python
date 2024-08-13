# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IngestEventParam"]


class IngestEventParam(TypedDict, total=False):
    category: Required[str]

    input: Required[int]

    output: Required[int]

    resource: Required[str]

    budget_ids: Optional[List[str]]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    experience_id: Optional[str]

    request_tags: Optional[List[str]]

    user_id: Optional[str]
