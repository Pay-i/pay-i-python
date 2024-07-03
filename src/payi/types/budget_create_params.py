# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BudgetCreateParams"]


class BudgetCreateParams(TypedDict, total=False):
    budget_name: Required[str]

    max: Required[float]

    base_cost_estimate: Literal["max"]

    budget_response_type: Literal["block", "allow"]

    budget_tags: Optional[List[str]]

    budget_type: Literal["conservative", "liberal"]

    currency: Literal["usd"]
