# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PriceModifierUpdateParams"]


class PriceModifierUpdateParams(TypedDict, total=False):
    billing_model_id: Required[str]

    category: Required[str]

    price_modifier: Required[float]

    resource: Required[str]
