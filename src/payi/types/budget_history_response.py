# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BudgetHistoryResponse",
    "BudgetHistory",
    "BudgetHistoryTotals",
    "BudgetHistoryTotalsCost",
    "BudgetHistoryTotalsCostInput",
    "BudgetHistoryTotalsCostOutput",
    "BudgetHistoryTotalsCostTotal",
    "BudgetHistoryTotalsRequests",
]


class BudgetHistoryTotalsCostInput(BaseModel):
    base: Optional[float] = None

    billed: Optional[float] = None

    overrun_base: Optional[float] = FieldInfo(alias="overrunBase", default=None)

    overrun_billed: Optional[float] = FieldInfo(alias="overrunBilled", default=None)

    revenue: Optional[float] = None


class BudgetHistoryTotalsCostOutput(BaseModel):
    base: Optional[float] = None

    billed: Optional[float] = None

    overrun_base: Optional[float] = FieldInfo(alias="overrunBase", default=None)

    overrun_billed: Optional[float] = FieldInfo(alias="overrunBilled", default=None)

    revenue: Optional[float] = None


class BudgetHistoryTotalsCostTotal(BaseModel):
    base: Optional[float] = None

    billed: Optional[float] = None

    overrun_base: Optional[float] = FieldInfo(alias="overrunBase", default=None)

    overrun_billed: Optional[float] = FieldInfo(alias="overrunBilled", default=None)

    revenue: Optional[float] = None


class BudgetHistoryTotalsCost(BaseModel):
    input: Optional[BudgetHistoryTotalsCostInput] = None

    output: Optional[BudgetHistoryTotalsCostOutput] = None

    total: Optional[BudgetHistoryTotalsCostTotal] = None


class BudgetHistoryTotalsRequests(BaseModel):
    blocked: Optional[int] = None

    exceeded: Optional[int] = None

    failed: Optional[int] = None

    successful: Optional[int] = None

    total: Optional[int] = None


class BudgetHistoryTotals(BaseModel):
    cost: Optional[BudgetHistoryTotalsCost] = None

    requests: Optional[BudgetHistoryTotalsRequests] = None


class BudgetHistory(BaseModel):
    base_cost_estimate: Optional[Literal["max"]] = None

    budget_id: Optional[str] = None

    budget_name: Optional[str] = None

    budget_reset_timestamp: Optional[datetime] = None

    budget_response_type: Optional[Literal["block", "allow"]] = None

    budget_tags: Optional[List[str]] = None

    budget_type: Optional[Literal["conservative", "liberal"]] = None

    max: Optional[float] = None

    totals: Optional[BudgetHistoryTotals] = None


class BudgetHistoryResponse(BaseModel):
    budget_history: BudgetHistory

    request_id: str

    message: Optional[str] = None
