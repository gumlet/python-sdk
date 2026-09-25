# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MultipartUploadListResponse", "Part"]


class Part(BaseModel):
    part_number: int = FieldInfo(alias="PartNumber")
    """Part number"""

    size: Optional[int] = FieldInfo(alias="Size", default=None)
    """Size of the uploaded part"""

    e_tag: Optional[str] = FieldInfo(alias="ETag", default=None)
    """ETag of the uploaded part"""


class MultipartUploadListResponse(BaseModel):
    parts: List[Part]
