# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["LiveStreamAssetCreateParams"]


class LiveStreamAssetCreateParams(TypedDict, total=False):
    live_source_id: Required[str]
    """Gumlet live video source/collection id."""

    resolution: Required[str]
    """Required resolutions in HLS delivery format for live stream. Can be an array of string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio."""

    title: str
    """Your live stream asset title"""

    mp4_access: bool
    """Creates <code>MP4</code> version for download purpose."""

    orientation: Literal["landscape", "potrait"]

    start_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
