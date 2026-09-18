# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAnalyticBreakdownDataParams", "DateRange", "Filter", "Breakdown"]


class VideoAnalyticBreakdownDataParams(TypedDict, total=False):
    date_range: Required[DateRange]
    """
    The timeframe to get the data for.
    Currently, we only support a maximum of *60 days* between `start_at` and `end_at`.
    """

    filters: Iterable[Filter]
    """Build *segments* of users using multiple filters on the data, `value` should be an *exact match*"""

    breakdowns: Required[Iterable[Breakdown]]
    """Breakdown fields and metrics to retrieve data for. Supports 1 to 3 breakdowns per request."""

    workspace_id: Required[str]
    """The five to ten character unique identifier of the Gumlet workspace ID available on the Video Workspaces."""


class Breakdown(TypedDict, total=False):
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
    """Name of the field to break down the data by."""

    metric: Required[
        Literal[
            "views",
            "unique_views",
            "impressions",
            "completion_percent_by_views",
            "playing_time",
            "concurrent_users",
            "widget_form_submitted",
            "cta_clicks",
        ]
    ]
    """The metric to retrieve breakdown data for."""

    page: int
    """Page number for paginated results."""

    page_size: int
    """Number of results per page."""


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
