# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAssetAnalyticsParams", "DateRange"]


class VideoAssetAnalyticsParams(TypedDict, total=False):
    group_by: Required[Literal["daily", "monthly", "weekly"]]
    """Group the data by this period."""

    date_range: Required[DateRange]

    metrics: Required[
        List[
            Literal[
                "impressions",
                "views",
                "playing_time",
                "top_countries",
                "top_pages",
                "top_cities",
                "top_device_types",
                "top_browsers",
                "heatmap",
                "widget_data",
            ]
        ]
    ]
    """List of metrics to return in response."""

    page_number: int
    """Page number to fetch. Starting at 1"""

    page_size: int
    """Number of items to return per page"""


class DateRange(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """ISO 8601 start timestamp"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """ISO 8601 end timestamp"""
