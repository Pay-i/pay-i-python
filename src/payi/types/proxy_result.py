# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .cost_details import CostDetails

__all__ = ["ProxyResult", "Budgets", "Cost"]


class Budgets(BaseModel):
    state: Optional[Literal["ok", "blocked", "blocked_external", "exceeded", "failed"]] = None


class Cost(BaseModel):
    currency: Optional[Literal["usd"]] = None

    input: Optional[CostDetails] = None

    output: Optional[CostDetails] = None

    total: Optional[CostDetails] = None


class ProxyResult(BaseModel):
    budgets: Optional[Dict[str, Budgets]] = None

    cost: Optional[Cost] = None

    request_id: Optional[str] = None

    request_tags: Optional[List[str]] = None
