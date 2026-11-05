# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoPlaylistCreateParams"]


class VideoPlaylistCreateParams(TypedDict, total=False):
    collection_id: str
    """Deprecated. Use `workspace_id` instead. Still accepted for backwards compatibility."""

    title: Required[str]
    """Playlist title"""

    description: str
    """Playlist description"""

    workspace_id: Required[str]
    """Gumlet video workspace ID. Preferred over deprecated `collection_id` / `source_id` (same ID)."""
