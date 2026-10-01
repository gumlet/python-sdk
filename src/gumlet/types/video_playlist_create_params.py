# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoPlaylistCreateParams"]


class VideoPlaylistCreateParams(TypedDict, total=False):
    collection_id: Required[str]
    """Workspace ID in which the playlist should be created"""

    title: Required[str]
    """Playlist title"""

    description: str
    """Playlist description"""
