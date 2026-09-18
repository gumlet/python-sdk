# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LiveStreamWorkspaceCreateParams"]


class LiveStreamWorkspaceCreateParams(TypedDict, total=False):
    name: Required[str]
    """Collection name"""
