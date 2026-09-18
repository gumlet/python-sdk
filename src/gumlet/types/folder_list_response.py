# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["FolderListResponse", "FolderListResponseItem"]


class FolderListResponseItem(BaseModel):
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

    updated_at: Optional[str] = None


FolderListResponse: TypeAlias = List[FolderListResponseItem]
