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
    """Define the metric you need the data for, currently we only support `bandwidth_consumption`, `asset_duration`, `storage_unit`, `top_assets`, `bandwidth_consumption_by_collection`, `errored_videos` and `widget_data`"""

    date_range: Required[DateRange]
    """The timeframe to get the data for. Currently we only support a maximum of 60 days between `start_at` and `end_at`."""

    filters: Filters

    top_assets_count: str
    """Count of video assets that should be returned. Max assets count is 1000 per page."""

    top_assets_page: str
    """top_assets metric may get paginated response. Iterate this parameter to get more data."""

    group_by: Literal["hourly", "daily", "monthly"]
    """Group by hourly, daily or monthly. If you don't specify anything it's `hourly` by default."""


class Filters(TypedDict, total=False):
    collection_id: str
    """The ID of the `workspace` you want to filter the data for."""

    source_id: str
    """The ID of the `workspace` you want to filter the data for. Deprecated."""


class DateRange(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The starting date to consider"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The ending date to consider"""
