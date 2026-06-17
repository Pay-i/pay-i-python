from __future__ import annotations

from typing import Union, Optional, TypedDict

import httpx


class PayiInstrumentModelMapping(TypedDict, total=False):
    model: str
    host: Optional[Union[str, httpx.URL]]
    price_as_category: Optional[str]
    price_as_resource: Optional[str]
    # "global", "datazone", "region", "region.<region_name>"
    resource_scope: Optional[str]
