# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LiveStreamWorkspaceUpdateParams"]


class LiveStreamWorkspaceUpdateParams(TypedDict, total=False):
    name: str
    """Live stream collection name"""

    video_source_id: str
    """Video on demand workspace ID"""
