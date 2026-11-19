# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAssetListParams"]


class VideoAssetListParams(TypedDict, total=False):
    status: str
    """Filter assets by status. Single value or comma-separated list (for example `ready` or `ready,errored`)."""

    tag: str
    """Filter by asset tag(s). Use a comma-separated string for multiple tags."""

    title: str
    """Filter assets by title (text search). When `title` is set, `next_page_token` is not supported - use `page_number` / `page_size`."""

    folder_id: str
    """Filter assets by folder id. Send `null` or empty string for assets not in a folder."""

    playlist_id: str
    """Filter assets belonging to a playlist."""

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Asset `created_at` lower bound. Date in `yyyy-MM-dd` format."""

    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Asset `created_at` upper bound. Date in `yyyy-MM-dd` format."""

    min_duration: int
    """Minimum asset duration in seconds."""

    max_duration: int
    """Maximum asset duration in seconds."""

    sort_by: Annotated[
        Literal["title", "duration", "uploaded_at", "created_at", "status"], PropertyInfo(alias="sortBy")
    ]
    """Field to sort by. Default is `created_at`. `next_page_token` is only supported for the default sort or `created_at`."""

    order_by: Annotated[Literal["asc", "desc"], PropertyInfo(alias="orderBy")]
    """Sort direction. Default is `desc`."""

    signed_token: Literal["true", "false"]
    """Whether URLs should be pre-signed in the API response. Possible values: `true` and `false`. Default is `false`."""

    page_number: int
    """Page number to retrieve. Starts at `1`."""

    page_size: int
    """Number of items to return per page. **Default: `20`**. **Maximum: `100`**."""

    next_page_token: str
    """Cursor for the next page. Pass the `next_page_token` value returned in the previous response. Supported only when sorting by default/`created_at` and when `title` is not set. Otherwise the API returns `400`."""
