# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BudgetUpdateParams"]


class BudgetUpdateParams(TypedDict, total=False):
    budget_name: Optional[str]

    max: Optional[float]
