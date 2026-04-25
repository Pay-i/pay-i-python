from __future__ import annotations

from typing import Optional, Sequence, TypedDict

from .PayiInstrumentModelMapping import PayiInstrumentModelMapping


class PayiInstrumentAnthropicConfig(TypedDict, total=False):
    model_mappings: Optional[Sequence[PayiInstrumentModelMapping]]

