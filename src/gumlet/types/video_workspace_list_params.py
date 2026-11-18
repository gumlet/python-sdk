# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoWorkspaceListParams"]


class VideoWorkspaceListParams(TypedDict, total=False):
    page_number: int
    """Page number to retrieve. Starts at `1`."""

    page_size: int
    """Number of items to return per page. **Default: `20`**. **Maximum: `200`**."""

    next_page_token: str
    """Cursor for the next page. Pass the `next_page_token` value returned in the previous response."""
