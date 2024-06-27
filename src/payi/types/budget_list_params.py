# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetListParams"]


class BudgetListParams(TypedDict, total=False):
    budget_name: Annotated[str, PropertyInfo(alias="BudgetName")]

    page_number: Annotated[int, PropertyInfo(alias="PageNumber")]

    page_size: Annotated[int, PropertyInfo(alias="PageSize")]

    sort_ascending: Annotated[bool, PropertyInfo(alias="SortAscending")]

    sort_by: Annotated[str, PropertyInfo(alias="SortBy")]

    tags: Annotated[str, PropertyInfo(alias="Tags")]
