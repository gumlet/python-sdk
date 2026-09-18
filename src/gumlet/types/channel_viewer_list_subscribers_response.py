# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ChannelViewerListSubscribersResponse", "Subscription"]


class Subscription(BaseModel):
    id: str
    """Subscriber ID"""

    email: str
    """Email ID of the subscriber"""

    name: str
    """Name of the subscriber"""

    status: str
    """Current status of the subscriber"""

    channel_title: str
    """Title of channel"""

    invited_at: Optional[str] = None
    """ISO 8601 timestamp of the invitation time"""

    invited_by: Optional[str] = None
    """User ID of the user who invited this subscriber"""

    invitation_link: Optional[str] = None
    """URL of the invitation from where the person can accept the invite."""


class ChannelViewerListSubscribersResponse(BaseModel):
    subscriptions: List[Subscription]
    """Details about subscribers"""

    total_count: int
    """Number of total subscribers"""
