# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["CategoryResponse"]


class CategoryResponse(BaseModel):
    category: str

    resource_count: int

    start_timestamp: datetime
