# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["KpiCreateParams"]


class KpiCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    goal: float

    kpi_type: Literal["boolean", "number", "percentage", "likert5", "likert7", "likert10"]
