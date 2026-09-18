# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LiveStreamAssetFilterParams"]


class LiveStreamAssetFilterParams(TypedDict, total=False):
    status: str
    """To filter live assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `created`, `active`, `complete`, `disconnected`, `errored`, and `deleted`."""

    offset: int
    """Offset value for a paginated list of assets."""

    size: int
    """Page size for the paginated list."""
