# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .ingest_units_param import IngestUnitsParam

__all__ = ["IngestBulkParams"]


class IngestBulkParams(TypedDict, total=False):
    items: Required[Iterable[IngestUnitsParam]]

    budget_ids: Annotated[Union[list[str], None], PropertyInfo(alias="xProxy-Budget-IDs")]

    request_tags: Annotated[Union[list[str], None], PropertyInfo(alias="xProxy-Request-Tags")]
