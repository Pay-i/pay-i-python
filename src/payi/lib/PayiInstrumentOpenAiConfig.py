from __future__ import annotations

from typing import Optional, Sequence, TypedDict

from .PayiInstrumentModelMapping import PayiInstrumentModelMapping
from .PayiInstrumentOpenAiAzureConfig import PayiInstrumentOpenAiAzureConfig


class PayiInstrumentOpenAiConfig(TypedDict, total=False):
    model_mappings: Optional[Sequence[PayiInstrumentModelMapping]]
    # deprecated: use model_mappings instead
    azure: PayiInstrumentOpenAiAzureConfig
