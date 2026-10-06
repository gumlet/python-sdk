# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """URL from the application you want to send data to."""

    secret_token: Required[str]
    """Secret sent back in the `x-gumlet-token` header of each webhook POST so you can confirm the request came from Gumlet."""

    triggers: Required[
        List[
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
    ]
    """Events that invoke this webhook. `status` subscribes to every video asset status event. `live-video-status` subscribes to every live video status event. Any other value subscribes to that event only."""

    sources: Required[SequenceNotStr[str]]
    """List of video collection identifiers for which webhooks are needed to be invoked."""
