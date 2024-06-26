# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TagUpdateParams"]


class TagUpdateParams(TypedDict, total=False):
    budget_tags: Required[List[str]]

    x_proxy_application_key: Annotated[str, PropertyInfo(alias="xProxy-Application-Key")]
