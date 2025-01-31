# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExperienceInstanceResponse"]


class ExperienceInstanceResponse(BaseModel):
    experience_id: str

    limit_id: Optional[str] = None
