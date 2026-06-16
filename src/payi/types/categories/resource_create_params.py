# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..category_resource_price_units_param import CategoryResourcePriceUnitsParam

__all__ = ["ResourceCreateParams"]


class ResourceCreateParams(TypedDict, total=False):
    category: Required[str]

    units: Required[Dict[str, CategoryResourcePriceUnitsParam]]

    max_input_units: Optional[int]

    max_output_units: Optional[int]

    max_total_units: Optional[int]

    start_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
