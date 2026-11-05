# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoUsageAnalyticTopAssetsParams"]


class VideoUsageAnalyticTopAssetsParams(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date in yyyy-MM-dd format"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date in yyyy-MM-dd format"""

    workspace_id: str
    """Gumlet video workspace ID. Preferred. Provide `workspace_id`, or deprecated `collection_id` / `source_id` (same ID)."""

    collection_id: str
    """Deprecated. Use `workspace_id` instead. Still accepted for backwards compatibility."""

    page: str
    """Page number of the response."""

    page_size: str
    """Assets to list per page."""
