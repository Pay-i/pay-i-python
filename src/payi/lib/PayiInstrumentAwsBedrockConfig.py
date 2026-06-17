from __future__ import annotations

from typing import Optional, Sequence, TypedDict

from .PayiInstrumentModelConfig import PayiInstrumentModelConfig
from .PayiInstrumentModelMapping import PayiInstrumentModelMapping


class PayiInstrumentAwsBedrockConfig(TypedDict, total=False):
    guardrail_trace: Optional[bool]
    add_streaming_xproxy_result: Optional[bool]
    model_mappings: Optional[Sequence[PayiInstrumentModelMapping]]
    model_config: Optional[dict[str, PayiInstrumentModelConfig]]
