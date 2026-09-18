# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RecycleBinListParams"]


class RecycleBinListParams(TypedDict, total=False):
    offset: int
    """Number of items to skip from start of page response."""

    size: int
    """Number of items to return for a single page."""

    workspace_id: Required[str]
    """ID of workspace for which you want to list the recycle bin items."""
