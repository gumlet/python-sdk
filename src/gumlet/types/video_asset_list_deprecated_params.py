# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAssetListDeprecatedParams"]


class VideoAssetListDeprecatedParams(TypedDict, total=False):
    status: Literal["queued", "processing", "ready", "errored", "deleted"]
    """To filter assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `queued`, `processing`, `ready`, `errored`, and `deleted`."""

    tag: str
    """Input tag on the basis of which assets need to be filtered. To filter on multiple tags use comma-separated string."""

    title: str
    """Title on the basis of which assets need to be filtered."""

    folder: str
    """Folder name on the basis of which assets need to be filtered."""

    offset: str
    """Offset value for a paginated list of assets."""

    size: str
    """Page size for the paginated list. **Default: `10`** **Max Size: `100`**"""

    playlist_id: str
    """filter assets from a playlist."""

    sort_by: Annotated[Literal["title", "duration", "uploaded_at", "created_at"], PropertyInfo(alias="sortBy")]
    """assets will be sorted based on the provided field."""

    order_by: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderBy")]
    """assets will be sorted in the specified order based on provided sortBy field or by default createAt field."""

    type: str
    """Search for folders, videos, or both. For videos, use `videos`. For folders, use `folders`. If you do not send this parameter, it will search for both."""
