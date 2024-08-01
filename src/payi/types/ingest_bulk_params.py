# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .ingest_units_param import IngestUnitsParam

__all__ = ["IngestBulkParams"]


class IngestBulkParams(TypedDict, total=False):
    items: Required[Iterable[IngestUnitsParam]]

    x_proxy_budget_ids: Annotated[str, PropertyInfo(alias="xProxy-Budget-IDs")]

    x_proxy_request_tags: Annotated[str, PropertyInfo(alias="xProxy-Request-Tags")]
