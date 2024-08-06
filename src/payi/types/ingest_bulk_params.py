# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .ingest_units_param import IngestUnitsParam

__all__ = ["IngestBulkParams"]


class IngestBulkParams(TypedDict, total=False):
    items: Required[Iterable[IngestUnitsParam]]
