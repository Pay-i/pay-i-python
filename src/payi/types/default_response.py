# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DefaultResponse"]


class DefaultResponse(BaseModel):
    message: Optional[str] = None

    request_id: Optional[str] = None
