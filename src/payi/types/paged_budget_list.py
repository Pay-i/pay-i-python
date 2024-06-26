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
    base: float

    overrun_base: float


class ItemTotalsCostOutputCost(BaseModel):
    base: float

    overrun_base: float


class ItemTotalsCostTotalCost(BaseModel):
    base: float

    overrun_base: float


class ItemTotalsCost(BaseModel):
    input_cost: ItemTotalsCostInputCost = FieldInfo(alias="inputCost")

    output_cost: ItemTotalsCostOutputCost = FieldInfo(alias="outputCost")

    total_cost: ItemTotalsCostTotalCost = FieldInfo(alias="totalCost")


class ItemTotalsRequests(BaseModel):
    blocked: int

    exceeded: int

    failed: int

    successful: int

    total: int

    error: Optional[int] = None


class ItemTotals(BaseModel):
    cost: ItemTotalsCost

    requests: ItemTotalsRequests


class Item(BaseModel):
    budget_name: Optional[str] = None

    base_cost_estimate: Optional[Literal["Max"]] = None

    budget_creation_timestamp: Optional[datetime] = None

    budget_id: Optional[str] = None

    budget_response_type: Optional[Literal["Block", "Allow"]] = None

    budget_tags: Optional[List[str]] = None

    budget_type: Optional[Literal["Conservative", "Liberal"]] = None

    budget_update_timestamp: Optional[datetime] = None

    currency: Optional[str] = None

    max: Optional[float] = None

    totals: Optional[ItemTotals] = None


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
