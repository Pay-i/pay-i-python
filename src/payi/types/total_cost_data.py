# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .cost_data import CostData
from .requests_data import RequestsData

__all__ = ["TotalCostData", "BudgetTransactions"]


class BudgetTransactions(BaseModel):
    blocked: int

    blocked_external: int

    exceeded: int

    successful: int

    error: Optional[int] = None

    total: Optional[int] = None


class TotalCostData(BaseModel):
    cost: CostData

    requests: RequestsData

    budget_transactions: Optional[BudgetTransactions] = None
