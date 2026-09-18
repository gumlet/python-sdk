# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FolderListParams"]


class FolderListParams(TypedDict, total=False):
    parent_id: str
    """Parent folder id. Send `null` to list root folders."""
