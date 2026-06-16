# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CategoryResourceMappedResource"]


class CategoryResourceMappedResource(BaseModel):
    category: Optional[str] = None

    resource: Optional[str] = None

    scope: Optional[Literal["global", "datazone", "region"]] = None

    sub_scope: Optional[str] = None
