# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BulkIngestResponse", "Error", "ErrorXproxyResult", "ErrorXproxyResultXproxyError"]


class ErrorXproxyResultXproxyError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None


class ErrorXproxyResult(BaseModel):
    message: str

    status_code: int = FieldInfo(alias="statusCode")

    xproxy_error: Optional[ErrorXproxyResultXproxyError] = None


class Error(BaseModel):
    item_index: Optional[int] = None

    xproxy_result: Optional[ErrorXproxyResult] = None


class BulkIngestResponse(BaseModel):
    ingest_count: int

    ingest_timestamp: datetime

    request_id: str

    error_count: Optional[int] = None

    errors: Optional[List[Error]] = None

    total_count: Optional[int] = None
