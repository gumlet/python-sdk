# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["WebhookHistoryResponse", "WebhookHistoryResponseItem"]


class WebhookHistoryResponseItem(BaseModel):
    id: str
    """Webhook event ID"""

    status: str
    """Delivery status stored for the event: `success`, `retrying`, or `failed`. `success` means the endpoint returned a 2xx response. `retrying` means that attempt did not."""

    retry_count: int
    """Number of retries it needed to deliver webhook."""

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
    """Webhook event name. One of the video status, live video status, or product events."""

    asset_id: str
    """Asset ID for which the event was fired"""

    created_at: str
    """Event timestamp in ISO 8601 format"""


WebhookHistoryResponse: TypeAlias = List[WebhookHistoryResponseItem]
