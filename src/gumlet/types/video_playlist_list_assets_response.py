# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoPlaylistListAssetsResponse", "AssetList"]


class AssetList(BaseModel):
    id: Optional[str] = None
    """Asset ID"""

    title: Optional[str] = None
    """Asset title"""

    description: Optional[str] = None
    """Asset description"""

    status: Optional[str] = None
    """Status"""

    created_at: Optional[str] = None

    duration: Optional[int] = None
    """Asset duration"""


class VideoPlaylistListAssetsResponse(BaseModel):
    asset_list: Optional[List[AssetList]] = None
    """List of assets inside playlist"""

    has_next_page: Optional[bool] = None

    next_page: Optional[int] = None
