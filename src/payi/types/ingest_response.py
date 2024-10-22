# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .cost_details import CostDetails

__all__ = ["IngestResponse", "XproxyResult", "XproxyResultBudgets", "XproxyResultCost"]


class XproxyResultBudgets(BaseModel):
    state: Optional[Literal["ok", "blocked", "blocked_external", "exceeded", "overrun", "failed"]] = None


class XproxyResultCost(BaseModel):
    currency: Optional[Literal["usd"]] = None

    input: Optional[CostDetails] = None

    output: Optional[CostDetails] = None

    total: Optional[CostDetails] = None


class XproxyResult(BaseModel):
    budgets: Optional[Dict[str, XproxyResultBudgets]] = None

    cost: Optional[XproxyResultCost] = None

    experience_id: Optional[str] = None

    request_id: Optional[str] = None

    request_tags: Optional[List[str]] = None

    resource_id: Optional[str] = None

    user_id: Optional[str] = None


class IngestResponse(BaseModel):
    event_timestamp: datetime

    ingest_timestamp: datetime

    request_id: str

    xproxy_result: XproxyResult
