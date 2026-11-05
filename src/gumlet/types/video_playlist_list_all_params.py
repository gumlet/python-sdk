# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoPlaylistListAllParams"]


class VideoPlaylistListAllParams(TypedDict, total=False):
    workspace_id: str
    """Gumlet video workspace ID. Preferred. Provide one of `workspace_id` or the deprecated aliases below (same ID)."""

    collection_id: str
    """Deprecated. Use `workspace_id` instead. Still accepted for backwards compatibility."""
