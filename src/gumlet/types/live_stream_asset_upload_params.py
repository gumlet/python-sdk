# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LiveStreamAssetUploadParams"]


class LiveStreamAssetUploadParams(TypedDict, total=False):
    live_asset_id: Required[str]
    """Gumlet live video asset id."""

    statuses: Required[Union[List[Literal["preparing", "disconnected", "end"]], str]]
    """Thumbnail states to upload. You can send an array or a comma-separated string."""
