# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LiveStreamAssetFilterParams"]


class LiveStreamAssetFilterParams(TypedDict, total=False):
    status: str
    """To filter live assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `created`, `active`, `complete`, `disconnected`, `errored`, and `deleted`."""

    page_number: int
    """Page number to retrieve. Starts at `1`."""

    page_size: int
    """Number of items to return per page. **Default: `20`**. **Maximum: `100`**."""

    next_page_token: str
    """Cursor for the next page. Pass the `next_page_token` value returned in the previous response."""
