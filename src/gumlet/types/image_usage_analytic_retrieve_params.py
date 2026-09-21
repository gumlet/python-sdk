# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["ImageUsageAnalyticRetrieveParams", "DateRange", "Filters"]


class ImageUsageAnalyticRetrieveParams(TypedDict, total=False):
    metrics: Required[
        List[
            Literal[
                "bandwidth_consumption",
                "requests_count",
                "transformations_count",
                "bandwidth_savings",
                "origin_hit_rate",
                "avg_transformation_response_time",
                "status_4xx",
                "status_5xx",
                "cdn_hit_rate",
                "content_type",
                "status_2xx",
                "avg_response_time",
                "top_assets",
                "bandwidth_consumption_by_source",
                "ai_credit_usage",
            ]
        ]
    ]
    """Define the metric you need the data for, currently we support "bandwidth_consumption", "requests_count","status_4xx","status_5xx","avg_response_time"\""""

    date_range: Required[DateRange]
    """The timeframe to get the data for. Currently we only support a maximum of 30 days between `start_at` and `end_at`."""

    group_by: Literal["daily", "weekly", "monthly", "hourly"]

    filters: Filters


class Filters(TypedDict, total=False):
    source_id: str
    """Source ID"""


class DateRange(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The starting date to consider"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The ending date to consider"""
