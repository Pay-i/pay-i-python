from __future__ import annotations

from typing import TypedDict

from .PayiInstrumentAnthropicAzureConfig import PayiInstrumentAnthropicAzureConfig


class PayiInstrumentAnthropicConfig(TypedDict, total=False):
    # map deployment name known model
    azure: PayiInstrumentAnthropicAzureConfig
