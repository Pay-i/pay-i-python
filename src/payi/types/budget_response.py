# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BudgetResponse",
    "Budget",
    "BudgetTotals",
    "BudgetTotalsCost",
    "BudgetTotalsCostInputCost",
    "BudgetTotalsCostOutputCost",
    "BudgetTotalsCostTotalCost",
    "BudgetTotalsRequests",
]


class BudgetTotalsCostInputCost(BaseModel):
    base: float

    overrun_base: float


class BudgetTotalsCostOutputCost(BaseModel):
    base: float

    overrun_base: float


class BudgetTotalsCostTotalCost(BaseModel):
    base: float

    overrun_base: float


class BudgetTotalsCost(BaseModel):
    input_cost: BudgetTotalsCostInputCost = FieldInfo(alias="inputCost")

    output_cost: BudgetTotalsCostOutputCost = FieldInfo(alias="outputCost")

    total_cost: BudgetTotalsCostTotalCost = FieldInfo(alias="totalCost")


class BudgetTotalsRequests(BaseModel):
    blocked: int

    exceeded: int

    failed: int

    successful: int

    total: int

    error: Optional[int] = None


class BudgetTotals(BaseModel):
    cost: BudgetTotalsCost

    requests: BudgetTotalsRequests


class Budget(BaseModel):
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

    totals: Optional[BudgetTotals] = None


class BudgetResponse(BaseModel):
    budget: Budget

    message: Optional[str] = None

    request_id: Optional[str] = None
