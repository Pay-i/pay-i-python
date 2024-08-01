# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .total_cost_data import TotalCostData

__all__ = ["BudgetHistoryResponse", "BudgetHistory"]


class BudgetHistory(BaseModel):
    budget_name: Optional[str] = None

    base_cost_estimate: Optional[Literal["max"]] = None

    budget_id: Optional[str] = None

    budget_reset_timestamp: Optional[datetime] = None

    budget_response_type: Optional[Literal["block", "allow"]] = None

    budget_tags: Optional[List[str]] = None

    budget_type: Optional[Literal["conservative", "liberal"]] = None

    max: Optional[float] = None

    totals: Optional[TotalCostData] = None


class BudgetHistoryResponse(BaseModel):
    budget_history: BudgetHistory

    request_id: str

    message: Optional[str] = None
