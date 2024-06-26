# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BudgetTagsResponse"]


class BudgetTagsResponse(BaseModel):
    created_on: Optional[datetime] = FieldInfo(alias="createdOn", default=None)

    tag_id: Optional[int] = FieldInfo(alias="tagId", default=None)

    tag_name: Optional[str] = FieldInfo(alias="tagName", default=None)
