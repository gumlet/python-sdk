# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LiveStreamWorkspaceCreateResponse"]


class LiveStreamWorkspaceCreateResponse(BaseModel):
    id: str
    """LIve stream workspace ID"""

    video_workspace_id: Optional[str] = None
    """Video workspace ID attached to this collection."""

    created_at: datetime
    """Creation timestamp in ISO 8601 format"""

    name: str
    """Name of the live stream workspace"""

    updated_at: datetime
    """Update timestamp in ISO 8601 format"""
