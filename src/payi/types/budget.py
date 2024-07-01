# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Budget"]


class Budget(BaseModel):
    budget: Budget

    request_id: str

    message: Optional[str] = None
