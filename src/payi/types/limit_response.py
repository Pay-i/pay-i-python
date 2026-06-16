# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .limit import Limit
from .._models import BaseModel

__all__ = ["LimitResponse"]


class LimitResponse(BaseModel):
    limit: Limit

    request_id: str

    message: Optional[str] = None
