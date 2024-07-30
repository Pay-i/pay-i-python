# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResourceCreateParams"]


class ResourceCreateParams(TypedDict, total=False):
    category: Required[str]

    start_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    input_price: float

    max_input_units: int

    max_output_units: int

    output_price: float
