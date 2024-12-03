# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ExperienceInstanceResponse"]


class ExperienceInstanceResponse(BaseModel):
    experience_id: str

    properties: Dict[str, str]

    request_id: str
