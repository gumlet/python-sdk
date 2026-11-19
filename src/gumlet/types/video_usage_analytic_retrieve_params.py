# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoUsageAnalyticRetrieveParams", "DateRange", "Filters"]


class VideoUsageAnalyticRetrieveParams(TypedDict, total=False):
    metrics: Required[
        List[
            Literal[
                "bandwidth_consumption",
                "asset_duration",
                "storage_unit",
                "top_assets",
                "drm_requests",
                "ai_credit_usage",
                "errored_videos",
            ]
        ]
    ]
    """Define the metric you need the data for. Supported values: `bandwidth_consumption`, `asset_duration`, `storage_unit`, `top_assets`, `widget_data`, `drm_requests`, `ai_credit_usage`, and `errored_videos`."""

    date_range: Required[DateRange]
    """The timeframe to get the data for. Currently we only support a maximum of 60 days between `start_at` and `end_at`."""

    filters: Filters

    top_assets_count: str
    """Deprecated. Use `page_size` instead."""

    top_assets_page: str
    """Deprecated. Use `page_number` instead."""

    group_by: Literal["hourly", "daily", "monthly"]
    """Group by hourly, daily or monthly. If you don't specify anything it's `hourly` by default."""

    page_number: int
    """Page number for paginated metrics. Used by `widget_data`, and by `top_assets` Starts at 1."""

    page_size: int
    """Page size for paginated metrics. Used by `widget_data`, and by `top_assets`"""


class Filters(TypedDict, total=False):
    collection_id: str
    """Deprecated. Use `workspace_id` instead. Still accepted for backwards compatibility."""

    source_id: str
    """Deprecated. Use `workspace_id` instead. Still accepted for backwards compatibility."""

    workspace_id: str
    """Gumlet video workspace ID. Preferred over deprecated `collection_id` / `source_id` (same ID)."""


class DateRange(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date in yyyy-MM-dd format"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date in yyyy-MM-dd format"""
