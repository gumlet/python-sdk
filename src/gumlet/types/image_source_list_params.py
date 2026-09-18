# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ImageSourceListParams"]


class ImageSourceListParams(TypedDict, total=False):
    offset: int
    """Skip number of items. Helpful for pagination."""

    size: int
    """Results per page."""
