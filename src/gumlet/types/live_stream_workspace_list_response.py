# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["LiveStreamWorkspaceListResponse", "AllLiveSource"]


class AllLiveSource(BaseModel):
    name: str
    """Live stream workspace name"""

    created_at: datetime
    """Creation time in ISO 8601 timestamp"""

    updated_at: datetime
    """Update time in ISO 8601 timestamp"""

    video_workspace_id: str
    """Video workspace ID that is attached to this collection. Once the live stream completes, the video gets stored in this workspace for long-term storage."""

    id: str
    """Workspace ID"""


class LiveStreamWorkspaceListResponse(BaseModel):
    all_live_sources: List[AllLiveSource]
    """List of all live stream collections"""
