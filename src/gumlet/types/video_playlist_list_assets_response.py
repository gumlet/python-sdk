# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoPlaylistListAssetsResponse", "AssetList"]


class AssetList(BaseModel):
    id: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    status: Optional[str] = None

    created_at: Optional[str] = None

    duration: Optional[int] = None


class VideoPlaylistListAssetsResponse(BaseModel):
    asset_list: Optional[List[AssetList]] = None

    has_next_page: Optional[bool] = None

    next_page: Optional[int] = None
