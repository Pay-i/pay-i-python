# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .total_cost_data import TotalCostData

__all__ = ["PagedLimitList", "Item"]


class Item(BaseModel):
    limit_creation_timestamp: datetime

    limit_id: str

    limit_name: str

    limit_type: Literal["block", "allow"]

    limit_update_timestamp: datetime

    max: float

    totals: TotalCostData

    limit_tags: Optional[List[str]] = None

    threshold: Optional[float] = None


class PagedLimitList(BaseModel):
    current_page: Optional[int] = FieldInfo(alias="currentPage", default=None)

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_previous_page: Optional[bool] = FieldInfo(alias="hasPreviousPage", default=None)

    items: Optional[List[Item]] = None

    message: Optional[str] = None

    page_size: Optional[int] = FieldInfo(alias="pageSize", default=None)

    request_id: Optional[str] = None

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
