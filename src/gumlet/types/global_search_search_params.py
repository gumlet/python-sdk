# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GlobalSearchSearchParams"]


class GlobalSearchSearchParams(TypedDict, total=False):
    search_query: Required[str]
    """Search query term"""

    workspace_id: str
    """Gumlet video workspace ID. Preferred. Provide `workspace_id`, or deprecated `collection_id` / `source_id` (same ID)."""

    collection_id: str
    """Deprecated. Use `workspace_id` instead. Still accepted for backwards compatibility."""

    size: int
    """Number of results to return"""

    assets_offset: int
    """Offset for assets"""

    folders_offset: int
    """Offset for folders"""

    playlists_offset: int
    """Offset for playlists"""

    channels_offset: int
    """Offset for channels"""
