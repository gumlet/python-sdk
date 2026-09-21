# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoPlaylistListAssetsParams"]


class VideoPlaylistListAssetsParams(TypedDict, total=False):
    sort_by: str
    """Optional, if sort_by is set to asset_title it will sorted by title name. Otherwise order in which user added the assets in playlist."""

    sort_order: int
    """-1 or 1"""

    page_number: int
    """Optional. Minimum: 1"""

    page_size: str
    """Optional. Minimum: 10"""
