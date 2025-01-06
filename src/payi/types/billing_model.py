# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingModel"]


class BillingModel(BaseModel):
    billing_model_id: Optional[str] = None

    created_on: datetime

    default: bool

    name: str

    type: Literal["costplus", "subscription", "hybrid"]

    updated_on: datetime

    default_price_modifier: Optional[float] = None

    prepaid_amount: Optional[float] = None

    prepaid_max: Optional[float] = None

    threshold: Optional[float] = None
