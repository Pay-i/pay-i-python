# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KpiCreateParams"]


class KpiCreateParams(TypedDict, total=False):
    use_case_id: Required[str]

    score: float
