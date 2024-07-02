# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RequestsData"]


class RequestsData(BaseModel):
    blocked: Optional[int] = None

    error: Optional[int] = None

    exceeded: Optional[int] = None

    failed: Optional[int] = None

    successful: Optional[int] = None

    total: Optional[int] = None
