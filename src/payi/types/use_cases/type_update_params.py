# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TypeUpdateParams"]


class TypeUpdateParams(TypedDict, total=False):
    description: Optional[str]

    logging_enabled: Optional[bool]
