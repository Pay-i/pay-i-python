# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "BudgetResponse",
    "Budget",
    "BudgetTotals",
    "BudgetTotalsCost",
    "BudgetTotalsCostInput",
    "BudgetTotalsCostOutput",
    "BudgetTotalsCostTotal",
    "BudgetTotalsRequests",
]


class BudgetTotalsCostInput(BaseModel):
    base: Optional[float] = None

    overrun_base: Optional[float] = None


class BudgetTotalsCostOutput(BaseModel):
    base: Optional[float] = None

    overrun_base: Optional[float] = None


class BudgetTotalsCostTotal(BaseModel):
    base: Optional[float] = None

    overrun_base: Optional[float] = None


class BudgetTotalsCost(BaseModel):
    input: BudgetTotalsCostInput

    output: BudgetTotalsCostOutput

    total: BudgetTotalsCostTotal


class BudgetTotalsRequests(BaseModel):
    blocked: Optional[int] = None

    error: Optional[int] = None

    exceeded: Optional[int] = None

    failed: Optional[int] = None

    successful: Optional[int] = None

    total: Optional[int] = None


class BudgetTotals(BaseModel):
    cost: Optional[BudgetTotalsCost] = None

    requests: Optional[BudgetTotalsRequests] = None


class Budget(BaseModel):
    base_cost_estimate: Literal["Max"]

    budget_creation_timestamp: datetime

    budget_id: str

    budget_name: str

    budget_response_type: Literal["Block", "Allow"]

    budget_type: Literal["Conservative", "Liberal"]

    budget_update_timestamp: datetime

    currency: str

    max: float

    totals: BudgetTotals

    budget_tags: Optional[List[str]] = None


class BudgetResponse(BaseModel):
    budget: Budget

    request_id: str

    message: Optional[str] = None
