# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAnalyticAggregatedDataParams", "Aggregate", "Timeframe", "Filter"]


class VideoAnalyticAggregatedDataParams(TypedDict, total=False):
    aggregate: Required[Iterable[Aggregate]]
    """Aggregate multiple metrics at the same time"""

    workspace_id: Required[str]
    """The unique identifier of the Gumlet workspace ID available on the Video Workspaces."""

    timeframe: Required[Timeframe]
    """The timeframe to get the data for. Currently we only support maximum difference between `start_at` and `end_at` to be *60 days*"""

    filters: Iterable[Filter]
    """Get aggregations for metrics with multiple filters, `value` should be an exact match"""


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
            "player_height_pixels",
            "player_width_pixels",
            "player_language_code",
            "meta_page_url",
            "meta_asn",
            "custom_user_id",
            "user_name",
            "user_email",
            "custom_video_id",
            "custom_video_title",
            "video_source_url",
            "video_source_hostname",
            "video_source_format",
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


class Timeframe(TypedDict, total=False):
    start_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Use <b>yyyy-MM-dd</b> format"""

    end_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Use <b>yyyy-MM-dd</b> format"""


class Aggregate(TypedDict, total=False):
    metric: Required[
        Literal[
            "views",
            "unique_views",
            "completion_percent_by_views",
            "playing_time",
            "concurrent_users",
            "impressions",
            "widget_form_submitted",
            "cta_clicks",
        ]
    ]
    """The metric to be aggregated for this request."""

    function: Required[Literal["sum", "average"]]
    """Aggregation function which is to be used."""
