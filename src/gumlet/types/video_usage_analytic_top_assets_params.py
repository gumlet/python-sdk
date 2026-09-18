# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoUsageAnalyticTopAssetsParams"]


class VideoUsageAnalyticTopAssetsParams(TypedDict, total=False):
    start_at: Required[str]
    """Date string in "yyyy-mm-dd" format"""

    end_at: Required[str]
    """Date string in "yyyy-mm-dd" format"""

    collection_id: str
    """Gumlet workspace ID"""

    page: str
    """Page number of the response."""

    page_size: str
    """Assets to list per page."""
