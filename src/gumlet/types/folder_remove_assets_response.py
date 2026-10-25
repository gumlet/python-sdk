# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FolderRemoveAssetsResponse"]


class FolderRemoveAssetsResponse(BaseModel):
    message: Optional[str] = None

    removed_count: Optional[int] = FieldInfo(alias="removedCount", default=None)
