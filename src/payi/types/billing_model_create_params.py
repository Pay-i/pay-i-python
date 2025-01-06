# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingModelCreateParams"]


class BillingModelCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["costplus", "subscription", "hybrid"]]

    default_price_modifier: Optional[float]

    prepaid_amount: Optional[float]

    prepaid_max: Optional[float]

    threshold: Optional[float]
