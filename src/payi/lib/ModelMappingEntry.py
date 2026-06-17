from __future__ import annotations

from typing import Optional
from dataclasses import dataclass

__all__ = ["_ModelMappingEntry"]


@dataclass
class _ModelMappingEntry:
    model: str
    host: Optional[str]
    price_as_category: Optional[str]
    price_as_resource: Optional[str]
    resource_scope: Optional[str]
