# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .cost_data import CostData
from .requests_data import RequestsData

__all__ = ["BudgetHistoryResponse", "BudgetHistory", "BudgetHistoryTotals", "BudgetHistoryTotalsBudgetTransactions"]


class BudgetHistoryTotalsBudgetTransactions(BaseModel):
    blocked: int

    blocked_external: int

    exceeded: int

    successful: int

    error: Optional[int] = None

    total: Optional[int] = None


class BudgetHistoryTotals(BaseModel):
    cost: CostData

    requests: RequestsData

    budget_transactions: Optional[BudgetHistoryTotalsBudgetTransactions] = None


class BudgetHistory(BaseModel):
    budget_name: Optional[str] = None

    base_cost_estimate: Optional[Literal["max"]] = None

    budget_id: Optional[str] = None

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
