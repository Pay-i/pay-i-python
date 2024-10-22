# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .price_modifier import PriceModifier

__all__ = ["PriceModifierRetrieveResponse"]

PriceModifierRetrieveResponse: TypeAlias = List[PriceModifier]
