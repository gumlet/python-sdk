# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookEndpointHistoryResponse", "History"]


class History(BaseModel):
    id: str
    """Webhook event ID"""

    status: Literal["success", "retrying", "failed"]
    """Delivery status stored for the event: `success`, `retrying`, or `failed`. `success` means the endpoint returned a 2xx response. `retrying` means that attempt did not."""

    retry_count: int
    """Number of retries needed to deliver the webhook."""

    event: Literal[
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
    """Webhook event name."""

    asset_id: str
    """Asset ID for which the event was fired."""

    created_at: str
    """Event timestamp in ISO 8601 format."""


class WebhookEndpointHistoryResponse(BaseModel):
    history: List[History]
    """Webhook trigger history events for this page."""

    total_count: int
    """Total number of history events."""

    current_offset: Optional[int] = None
    """Offset after this page of results."""

    next_page_token: Optional[str] = None
    """Cursor for the next page when more results exist. Empty string when there is no next page."""

    page_size: Optional[int] = None
    """Page size used for this response when it differs from the default."""
