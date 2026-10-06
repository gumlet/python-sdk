# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VideoAssetStatusWebhookEvent", "Input", "InputTransformations", "Output", "Error", "Warning"]


class Warning(BaseModel):
    code: Literal["WRN_LOW_FRAME_SIZE"]

    message: Literal[
        "Video Asset dimensions are lower than minimum supported frame size (240 pixels for HLS/DASH and 145 pixels for mp4). Any types transformation (resize, crop, pad, overlay etc.) specified would not be applied."
    ]


class Error(BaseModel):
    code: str
    """Error code stored on the asset."""

    message: str
    """Error message stored on the asset."""


class Output(BaseModel):
    format: Optional[str] = None
    """Output format from the asset transformations."""

    status_url: str
    """Asset status URL. Pattern: `https://api.gumlet.com/video/v1/status/{asset_id}`."""

    playback_url: str
    """For `abr`, `main.m3u8`. For every other format, `main.{target_extension}`."""

    dash_playback_url: Optional[str] = None
    """DASH manifest (`main.mpd`). Present when the format is `abr`."""

    thumbnail_url: List[str]
    """One URL per configured thumbnail: `thumbnail-{index}-{format_code}.{thumbnail_format}`. Format codes are png `0`, jpeg `1`, jpg `2`, and webp `3`. Index starts at 1."""

    storage_bytes: Optional[float] = None
    """Processed output size in bytes. Present when the asset output has a size."""

    download_url: Optional[str] = None
    """MP4 download URL (`download.mp4`). Present when `mp4_access` is enabled."""

    animated_gif_url: Optional[str] = None
    """Animated GIF URL (`animation.gif`). Present when an animated GIF was requested."""

    preview_thumbnails_url: Optional[str] = None
    """Preview thumbnail WebVTT (`preview_thumbnails.vtt`). Present when preview thumbnails were requested and the asset is not audio-only."""


class InputTransformations(BaseModel):
    format: Optional[str] = None
    """Output format, such as `abr`, `hls`, `dash`, or `mp4`."""

    width: Optional[str] = None

    height: Optional[str] = None

    resolution: Optional[List[str]] = None

    audio_codec: Optional[List[str]] = None

    video_codec: Optional[List[str]] = None

    secondary_video_codec: Optional[str] = None

    thumbnail: Optional[List[object]] = None
    """Thumbnail selectors from the asset. Entries are strings such as `auto`, or objects of thumbnail options."""

    thumbnail_format: Optional[str] = None
    """Thumbnail image format, such as `png`, `jpg`, `jpeg`, or `webp`."""

    audio_only: Optional[bool] = None

    mp4_access: Optional[bool] = None

    keep_original: Optional[bool] = None

    per_title_encoding: Optional[bool] = None

    process_low_resolution_input: Optional[bool] = None

    pad: Optional[Dict[str, object]] = None

    crop: Optional[Dict[str, object]] = None

    trim: Optional[Dict[str, object]] = None

    text_overlay: Optional[Dict[str, object]] = None

    image_overlay: Optional[Dict[str, object]] = None

    animated_gif: Optional[object] = None

    generate_subtitles: Optional[object] = None

    preview_thumbnails: Optional[object] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class Input(BaseModel):
    source_url: Optional[str] = None
    """URL of the source media."""

    transformations: InputTransformations
    """Asset transformations copied onto the webhook. Keys are converted from camelCase to snake_case. Nested object keys are converted the same way."""

    fps: Optional[float] = None
    """Source frame rate."""

    size: Optional[float] = None
    """Source file size in bytes."""

    width: Optional[int] = None
    """Source width in pixels."""

    height: Optional[int] = None
    """Source height in pixels."""

    duration: Optional[float] = None
    """Source duration in seconds."""

    aspect_ratio: Optional[str] = None
    """Source aspect ratio, such as `16:9`."""

    metadata: Optional[object] = None
    """Custom metadata supplied when the asset was created."""

    profile_id: Optional[str] = None
    """Encoding profile id used for the asset."""

    vimeo_id: Optional[str] = None
    """Vimeo id, when the asset was imported from Vimeo."""


class VideoAssetStatusWebhookEvent(BaseModel):
    type: Literal[
        "video.status.created",
        "video.status.downloaded",
        "video.status.optimized",
        "video.status.ready",
        "video.status.errored",
        "video.status.deleted",
        "video.status.repackaged",
        "video.status.stream_ready",
    ]
    """Video status event that triggered this delivery."""

    status: str
    """Current asset status. `output` is omitted when this is `deleted` or `errored`."""

    asset_id: str
    """Video asset id."""

    created_at: int
    """Asset creation time, in milliseconds since the Unix epoch."""

    tag: Optional[List[str]] = None
    """Tags stored on the asset."""

    title: Optional[str] = None
    """Asset title."""

    description: Optional[str] = None
    """Asset description."""

    input: Input

    output: Optional[Output] = None
    """Omitted when the asset status is `deleted` or `errored`. Playback URLs use `https://video.gumlet.io/{workspace_id}/{asset_id}/`."""

    error: Optional[Error] = None
    """Present when the asset status is `errored` and the asset has an error."""

    warning: Optional[Warning] = None
    """Included when `process_low_resolution_input` is enabled and the smaller frame dimension is below the minimum for the output format: 240 pixels for `hls`, `dash`, or `abr`, and 145 pixels for `mp4`. Transformations such as resize, crop, pad, and overlay are not applied."""
