# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PropertyCreateResponse"]


class PropertyCreateResponse(BaseModel):
    use_case_id: str

    limit_id: Optional[str] = None

    type_version: Optional[int] = None
