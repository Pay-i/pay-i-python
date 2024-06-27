# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IngestUnitsParams"]


class IngestUnitsParams(TypedDict, total=False):
    category: Required[str]

    input: Required[int]

    output: Required[int]

    resource: Required[str]

    x_proxy_budget_ids: Annotated[str, PropertyInfo(alias="xProxy-Budget-IDs")]

    x_proxy_request_tags: Annotated[str, PropertyInfo(alias="xProxy-Request-Tags")]
