# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PriceModifier"]


class PriceModifier(BaseModel):
    billing_model_id: Optional[str] = None

    category: Optional[str] = None

    create_timestamp: datetime

    price_modifier: float

    price_modifier_id: Optional[str] = None

    resource: Optional[str] = None

    resource_id: Optional[str] = None

    update_timestamp: datetime
