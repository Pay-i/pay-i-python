from __future__ import annotations

from typing import Sequence, TypedDict

from .PayiInstrumentModelMapping import PayiInstrumentModelMapping


class PayiInstrumentOpenAiAzureConfig(TypedDict, total=False):
    # map deployment name known model
    model_mappings: Sequence[PayiInstrumentModelMapping]
