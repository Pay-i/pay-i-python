# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .total_cost_data import TotalCostData

__all__ = ["LimitHistoryResponse", "LimitHistory"]


class LimitHistory(BaseModel):
    limit_name: Optional[str] = None

    limit_id: Optional[str] = None

    limit_reset_timestamp: Optional[datetime] = None

    limit_tags: Optional[List[str]] = None

    limit_type: Optional[Literal["block", "allow"]] = None

    max: Optional[float] = None

    totals: Optional[TotalCostData] = None


class LimitHistoryResponse(BaseModel):
    limit_history: LimitHistory

    request_id: str

    message: Optional[str] = None
