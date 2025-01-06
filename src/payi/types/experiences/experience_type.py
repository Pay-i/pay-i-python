# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExperienceType"]


class ExperienceType(BaseModel):
    description: str

    name: str

    request_id: str

    logging_enabled: Optional[bool] = None
