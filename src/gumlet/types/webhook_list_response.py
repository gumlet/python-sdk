# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    id: str
    """Webhook ID"""

    url: str
    """Webhook URL"""

    triggers: List[
        Literal[
            "status",
            "live-video-status",
            "video.status.created",
            "video.status.downloaded",
            "video.status.optimized",
            "video.status.ready",
            "video.status.errored",
            "video.status.deleted",
            "video.status.repackaged",
            "video.status.stream_ready",
            "live.video.status.created",
            "live.video.status.ready",
            "live.video.status.preparing",
            "live.video.status.connected",
            "live.video.status.active",
            "live.video.status.complete",
            "live.video.status.disconnected",
            "event.embed.viewed",
            "event.embed.cta_clicked",
            "event.video.updated",
            "event.video.uploaded",
            "event.playlist.created",
            "event.playlist.asset",
            "event.playlist.deleted",
            "event.video.analytics",
            "event.image.analytics",
            "event.embed.form_submitted",
            "event.comment.all",
            "event.channel.member_joined",
        ]
    ]
    """Events that invoke this webhook. `status` subscribes to every video asset status event. `live-video-status` subscribes to every live video status event. Any other value subscribes to that event only."""

    created_at: str
    """Creation timestamp in ISO 8601 format"""

    updated_at: str
    """Update timestamp in ISO 8601 format"""

    sources: List[str]
    """List of workspace IDs for which the webhook is enabled."""

    secret_token: Optional[str] = None
    """Secret you supplied when creating the webhook. Gumlet sends this value in the `x-gumlet-token` header of each webhook POST."""
