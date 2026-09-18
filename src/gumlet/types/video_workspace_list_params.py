# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoWorkspaceListParams"]


class VideoWorkspaceListParams(TypedDict, total=False):
    offset: str
    """Number of workspaces to skip. For example if you need to list 11 to 20th workspaces, pass offset as 10 and size as 10."""

    size: str
    """Number of workspace to return in single response."""
