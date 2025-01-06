# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TypeCreateParams"]


class TypeCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    logging_enabled: Optional[bool]
