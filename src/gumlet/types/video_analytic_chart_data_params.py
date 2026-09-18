# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["VideoAnalyticChartDataParams", "DateRange", "Filter", "ChartDimension", "ChartDimensionGroupBy"]


class VideoAnalyticChartDataParams(TypedDict, total=False):
    metrics: Required[SequenceNotStr[str]]
    """Get data for one or more `metrics` in the same request. Please add any of these metrics. `views`, `unique_views`, `impressions`. `completion_percent_by_views`, `playing_time`, `concurrent_users`, `widget_form_submitted`, `cta_clicks`"""

    workspace_id: Required[str]
    """The five to ten character unique identifier of the Gumlet workspace ID available on the Video Workspaces."""

    date_range: Required[DateRange]
    """
    The timeframe to get the data for.
    Currently, we only support a maximum of *60 days* between `start_at` and `end_at`.
    """

    filters: Iterable[Filter]
    """Build *segments* of users using multiple filters on the data, `value` should be an *exact match*"""

    group_by: Literal["daily", "weekly", "monthly"]
    """Data can be grouped by `daily`, `weekly` or `monthly`."""

    chart_dimension: ChartDimension
    """Metrics result Group by selected dimension, You can select upto 3 dimensions to get nested category result. result will follow selection orders."""


class ChartDimensionGroupBy(TypedDict, total=False):
    name: Literal[
        "custom_video_title",
        "custom_video_id",
        "custom_workspace_id",
        "video_source_url",
        "video_source_format",
        "player_software_version",
        "player_software",
        "meta_page_url",
        "audio_language",
        "subtitle_language",
        "video_width_pixels",
        "video_height_pixels",
        "meta_country",
        "meta_city",
        "meta_device_category",
        "meta_device_manufacturer",
        "meta_browser",
        "meta_browser_version",
        "meta_browser_language",
        "meta_operating_system",
        "meta_operating_system_version",
        "meta_device_name",
        "meta_asn",
    ]


class ChartDimension(TypedDict, total=False):
    group_by: Iterable[ChartDimensionGroupBy]


class Filter(TypedDict, total=False):
    name: Required[
        Literal[
            "meta_browser",
            "meta_operating_system",
            "meta_operating_system_version",
            "meta_device_category",
            "meta_device_manufacturer",
            "meta_device_name",
            "meta_device_display_width",
            "meta_device_display_height",
            "meta_country",
            "meta_city",
            "meta_region",
            "player_software",
            "player_software_version",
            "player_language_code",
            "player_name",
            "meta_page_url",
            "meta_asn",
            "custom_user_id",
            "custom_user_email",
            "custom_video_id",
            "custom_video_title",
            "video_source_url",
            "custom_video_variant_name",
            "custom_video_language",
            "custom_video_variant",
            "custom_data_1",
            "custom_data_2",
            "custom_data_3",
            "custom_data_4",
            "custom_data_5",
        ]
    ]
    """Name of the breakdown to filter data on."""

    value: Required[str]
    """Value to be matched for the given filter name. Currently we support exact matches."""

    operator: Literal["equals", "does not equal", "contains", "does not contain", "is set", "is not set"]
    """Operator to be used while filtering the data"""


class DateRange(TypedDict, total=False):
    start_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Use <b>yyyy-MM-dd</b> format"""

    end_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Use <b>yyyy-MM-dd</b> format"""
