# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PagedBudgetList",
    "Item",
    "ItemTotals",
    "ItemTotalsCost",
    "ItemTotalsCostInputCost",
    "ItemTotalsCostOutputCost",
    "ItemTotalsCostTotalCost",
    "ItemTotalsRequests",
]


class ItemTotalsCostInputCost(BaseModel):
    base: Optional[float] = None

    overrun_base: Optional[float] = None


class ItemTotalsCostOutputCost(BaseModel):
    base: Optional[float] = None

    overrun_base: Optional[float] = None


class ItemTotalsCostTotalCost(BaseModel):
    base: Optional[float] = None

    overrun_base: Optional[float] = None


class ItemTotalsCost(BaseModel):
    input_cost: Optional[ItemTotalsCostInputCost] = FieldInfo(alias="inputCost", default=None)

    output_cost: Optional[ItemTotalsCostOutputCost] = FieldInfo(alias="outputCost", default=None)

    total_cost: Optional[ItemTotalsCostTotalCost] = FieldInfo(alias="totalCost", default=None)


class ItemTotalsRequests(BaseModel):
    blocked: Optional[int] = None

    error: Optional[int] = None

    exceeded: Optional[int] = None

    failed: Optional[int] = None

    successful: Optional[int] = None

    total: Optional[int] = None


class ItemTotals(BaseModel):
    cost: Optional[ItemTotalsCost] = None

    requests: Optional[ItemTotalsRequests] = None


class Item(BaseModel):
    base_cost_estimate: Literal["Max"]

    budget_creation_timestamp: datetime

    budget_id: str

    budget_name: str

    budget_response_type: Literal["Block", "Allow"]

    budget_type: Literal["Conservative", "Liberal"]

    budget_update_timestamp: datetime

    currency: str

    max: float

    totals: ItemTotals

    budget_tags: Optional[List[str]] = None


class PagedBudgetList(BaseModel):
    current_page: Optional[int] = FieldInfo(alias="currentPage", default=None)

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_previous_page: Optional[bool] = FieldInfo(alias="hasPreviousPage", default=None)

    items: Optional[List[Item]] = None

    message: Optional[str] = None

    page_size: Optional[int] = FieldInfo(alias="pageSize", default=None)

    request_id: Optional[str] = None

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
