# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CategoryResourceResponse"]


class CategoryResourceResponse(BaseModel):
    category: str

    resource: str

    resource_id: str

    start_timestamp: datetime

    input_price: Optional[float] = None

    max_input_units: Optional[int] = None

    max_output_units: Optional[int] = None

    output_price: Optional[float] = None
