# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LiveVideoStatusWebhookEvent", "Input", "Output", "Error"]


class Error(BaseModel):
    code: str
    """Error code stored on the asset."""

    message: str
    """Error message stored on the asset."""


class Output(BaseModel):
    playback_url: Optional[str] = None
    """Live playback URL. Uses the Mux playback id when one exists (`https://stream.live.gumlet.io/{playback_id}`). Otherwise `https://video.gumlet.io/{live_video_source_id}/{live_asset_id}/master.m3u8`."""

    embed_url: Optional[str] = None
    """Embeddable player URL. Pattern: `https://play.gumlet.io/embed/live/{live_asset_id}`."""

    storage_size: Optional[float] = None
    """Recording size in bytes. Present when the asset status is `complete` and output metadata exists."""

    duration: Optional[float] = None
    """Recording duration in seconds. Present when the asset status is `complete` and output metadata exists."""

    recording_playback_url: Optional[str] = None
    """Playback URL of the completed recording. When a VOD asset was created, this is `https://video.gumlet.io/{vod_collection_id}/{recording_asset_id}/main.m3u8`. Otherwise it uses the Mux VOD playback id."""


class Input(BaseModel):
    live_video_source_id: str
    """Live video workspace id."""

    resolution: Optional[List[str]] = None
    """Renditions configured for the live asset."""

    title: str
    """Live asset title. When the asset has no title, Gumlet generates `Live stream at HH:MM:SS on {ordinal day} {month}` in the organization user's time zone."""

    width: Optional[int] = None
    """Source width in pixels. Present when the asset status is `active` and primary metadata is available."""

    height: Optional[int] = None
    """Source height in pixels. Present when the asset status is `active` and primary metadata is available."""

    aspect_ratio: Optional[str] = None
    """Source aspect ratio. Present when the asset status is `active` and primary metadata is available."""


class LiveVideoStatusWebhookEvent(BaseModel):
    type: Literal[
        "live.video.status.created",
        "live.video.status.ready",
        "live.video.status.preparing",
        "live.video.status.connected",
        "live.video.status.active",
        "live.video.status.complete",
        "live.video.status.disconnected",
    ]
    """Live video status event that triggered this delivery."""

    status: str
    """Current live asset status. `output` is omitted when this is `deleted` or `errored`."""

    live_asset_id: str
    """Live asset id."""

    created_at: int
    """Live asset creation time, in milliseconds since the Unix epoch."""

    updated_at: int
    """Live asset update time, in milliseconds since the Unix epoch."""

    recording_asset_id: Optional[str] = None
    """VOD asset id of the recording. Present when the live asset status is `complete` and a VOD asset exists."""

    vod_collection_id: Optional[str] = None
    """Workspace id of the recording asset. Present together with `recording_asset_id`."""

    deleted_at: Optional[int] = None
    """Deletion time in milliseconds since the Unix epoch. Present when the status is `deleted` or `errored` and a deletion time is stored."""

    input: Input

    output: Optional[Output] = None
    """Omitted when the live asset status is `deleted` or `errored`."""

    error: Optional[Error] = None
    """Present when the asset status is `errored` and the asset has an error."""
