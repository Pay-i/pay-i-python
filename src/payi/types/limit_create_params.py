# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["LimitCreateParams"]


class LimitCreateParams(TypedDict, total=False):
    limit_name: Required[str]

    max: Required[float]

    limit_id: Optional[str]

    limit_tags: Optional[SequenceNotStr[str]]

    limit_type: Literal["block", "allow"]

    threshold: Optional[float]
