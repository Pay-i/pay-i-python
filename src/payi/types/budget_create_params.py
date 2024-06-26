# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetCreateParams"]


class BudgetCreateParams(TypedDict, total=False):
    budget_name: Required[str]

    max: Required[float]

    base_cost_estimate: Literal["Max"]

    budget_response_type: Literal["Block", "Allow"]

    budget_tags: Optional[List[str]]

    budget_type: Literal["Conservative", "Liberal"]

    x_proxy_application_key: Annotated[str, PropertyInfo(alias="xProxy-Application-Key")]
