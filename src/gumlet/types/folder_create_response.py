# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FolderCreateResponse"]


class FolderCreateResponse(BaseModel):
    id: Optional[str] = None
    """Folder ID"""

    name: Optional[str] = None
    """Folder name"""

    video_source_id: Optional[str] = None
    """Workspace ID"""

    parent_id: Optional[str] = None
    """Parent folder ID"""

    path: Optional[List[str]] = None
    """Path details"""

    path_names: Optional[List[str]] = None

    depth: Optional[int] = None
    """Depth of this folder from root"""

    subdirectory_count: Optional[int] = None
    """Number of subfolders inside this folder"""

    asset_count: Optional[int] = None
    """Number of assets inside this folder"""

    created_at: Optional[datetime] = None
    """Folder creation time in ISO 8601 format"""

    updated_at: Optional[datetime] = None
    """Folder update time in ISO 8601 format"""
