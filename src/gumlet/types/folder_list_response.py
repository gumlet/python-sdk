# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["FolderListResponse", "FolderListResponseItem"]


class FolderListResponseItem(BaseModel):
    id: Optional[str] = None
    """Folder ID"""

    name: Optional[str] = None
    """Folder name"""

    video_source_id: Optional[str] = None
    """Workspace ID"""

    parent_id: Optional[str] = None
    """Parent folder ID"""

    path: Optional[List[str]] = None
    """Path of the folder"""

    path_names: Optional[List[str]] = None

    depth: Optional[int] = None
    """Depth from root folder"""

    subdirectory_count: Optional[int] = None
    """Number of child folders"""

    asset_count: Optional[int] = None
    """Number of assets inside this folder"""

    created_at: Optional[datetime] = None
    """Folder creation time in ISO 8601 format"""

    updated_at: Optional[datetime] = None
    """Folder update time in ISO 8601 format"""


FolderListResponse: TypeAlias = List[FolderListResponseItem]
