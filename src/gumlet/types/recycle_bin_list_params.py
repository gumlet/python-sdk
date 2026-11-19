# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RecycleBinListParams"]


class RecycleBinListParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of workspace for which you want to list the recycle bin items."""

    page_number: int
    """Page number to retrieve. Starts at `1`."""

    page_size: int
    """Number of items to return per page. **Default: `20`**. **Maximum: `100`**."""
