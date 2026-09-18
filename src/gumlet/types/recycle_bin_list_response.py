# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RecycleBinListResponse", "AllAsset"]


class AllAsset(BaseModel):
    asset_id: str
    """Asset ID of the deleted asset."""

    workspace_id: str
    """Workspace ID for the asset."""

    title: str
    """Title of the asset."""

    description: Optional[str] = None
    """Description of the video."""

    tags: List[str]
    """Tags associated with the asset."""

    duration: float
    """Duration of the asset in seconds."""

    deleted_at: float
    """Deleted timestamp of asset in milliseconds since epoch."""

    deleted_by: str
    """User ID of the user who deleted the asset."""


class RecycleBinListResponse(BaseModel):
    total_asset_count: int
    """Number of total assets in recycle bin."""

    current_offset: int
    """Number of total assets in current offset."""

    all_assets: List[AllAsset]
