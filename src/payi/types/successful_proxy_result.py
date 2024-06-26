# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["SuccessfulProxyResult", "Budgets", "Cost", "CostInput", "CostOutput", "CostTotal"]


class Budgets(BaseModel):
    state: Optional[str] = None


class CostInput(BaseModel):
    base: Optional[float] = None


class CostOutput(BaseModel):
    base: Optional[float] = None


class CostTotal(BaseModel):
    base: Optional[float] = None


class Cost(BaseModel):
    currency: Optional[str] = None

    input: Optional[CostInput] = None

    output: Optional[CostOutput] = None

    total: Optional[CostTotal] = None


class SuccessfulProxyResult(BaseModel):
    budgets: Optional[Dict[str, Budgets]] = None

    cost: Optional[Cost] = None

    request_id: Optional[str] = None

    request_tags: Optional[List[str]] = None
