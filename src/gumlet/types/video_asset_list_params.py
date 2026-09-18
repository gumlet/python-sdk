# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAssetListParams"]


class VideoAssetListParams(TypedDict, total=False):
    type: Literal["folders", "videos", "all"]
    """Return `folders`, `videos`, or `all`. Default is `all`."""

    parent_id: str
    """Parent folder id. Send `null` to browse the root level."""

    title: str
    """Search folders or assets by title or description."""

    status: str
    """Comma-separated asset status values."""

    tag: str
    """Comma-separated asset tags."""

    playlist_id: str
    """Filter assets to a playlist."""

    start_date: str
    """Asset created_at lower bound."""

    end_date: str
    """Asset created_at upper bound."""

    min_duration: float
    """Minimum asset duration in seconds."""

    max_duration: float
    """Maximum asset duration in seconds."""

    sort_by: Annotated[Literal["title", "duration", "uploaded_at", "created_at"], PropertyInfo(alias="sortBy")]
    """Sort assets by a supported field."""

    order_by: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderBy")]
    """Asset sort order."""

    search_index: Annotated[
        Literal["search_index_for_asset_list", "cms-search", "cms-search-v2"], PropertyInfo(alias="searchIndex")
    ]
    """Search index used for asset title search."""

    offset: int
    """Offset for paginated results."""

    size: int
    """Page size. Maximum 100."""

    signed_token: Literal["true", "false"]
    """Whether URLs should be pre-signed in the API response. Possible values: `true` and `false`. Default is `false`."""
