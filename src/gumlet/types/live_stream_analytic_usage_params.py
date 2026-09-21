# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["LiveStreamAnalyticUsageParams", "DateRange"]


class LiveStreamAnalyticUsageParams(TypedDict, total=False):
    date_range: Required[DateRange]

    group_by: Required[Literal["daily", "weekly", "monthly"]]
    """Group the data either weekly, daily or monthly"""

    metrics: Required[List[Literal["bandwidth_consumption", "asset_duration", "storage_unit"]]]
    """List of metrics required in response"""


class DateRange(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Start date in ISO 8601 date format (YYYY-MM-DD)"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """End date in ISO 8601 date format (YYYY-MM-DD)"""
