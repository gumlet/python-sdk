# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoProfileListParams"]


class VideoProfileListParams(TypedDict, total=False):
    offset: int
    """Offset value for a paginated list of profiles. Can be zero for the first time and `current_offset` value received from the last request afterwards."""

    size: int
    """Page size for the paginated list. **Default: `10`**"""
