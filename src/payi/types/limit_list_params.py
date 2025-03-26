# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LimitListParams"]


class LimitListParams(TypedDict, total=False):
    limit_name: str

    page_number: int

    page_size: int

    sort_ascending: bool

    sort_by: str

    tag_list: Annotated[List[str], PropertyInfo(alias="TagList")]

    tags: str
