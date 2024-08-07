# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BudgetListParams"]


class BudgetListParams(TypedDict, total=False):
    budget_name: str

    page_number: int

    page_size: int

    sort_ascending: bool

    sort_by: str

    tags: str
