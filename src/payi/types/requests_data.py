# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RequestsData"]


class RequestsData(BaseModel):
    blocked: int

    error: int

    successful: int

    total: Optional[int] = None
