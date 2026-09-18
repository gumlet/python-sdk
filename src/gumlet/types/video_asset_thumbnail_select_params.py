# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoAssetThumbnailSelectParams"]


class VideoAssetThumbnailSelectParams(TypedDict, total=False):
    frame_at_second: Required[int]
    """Frame secound"""
