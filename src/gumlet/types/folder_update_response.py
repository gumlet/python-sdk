# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FolderUpdateResponse", "FolderUpdateResponse2"]


class FolderUpdateResponse2(BaseModel):
    message: Optional[str] = None

    moved_count: Optional[int] = FieldInfo(alias="movedCount", default=None)


class FolderUpdateResponse(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    video_source_id: Optional[str] = None

    parent_id: Optional[str] = None

    path: Optional[List[str]] = None

    path_names: Optional[List[str]] = None

    depth: Optional[int] = None

    subdirectory_count: Optional[int] = None

    asset_count: Optional[int] = None

    created_at: Optional[str] = None
    """ISO Timestamp"""

    updated_at: Optional[str] = None
    """ISO Timestamp"""


FolderUpdateResponse: TypeAlias = Union[FolderUpdateResponse, FolderUpdateResponse2]
