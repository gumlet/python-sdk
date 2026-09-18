# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    name: Required[str]
    """Folder name."""

    parent_id: Optional[str]
    """Parent folder id. Send `null` or omit it to create a root-level folder."""
