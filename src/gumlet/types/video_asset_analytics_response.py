# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "VideoAssetAnalyticsResponse",
    "Heatmap",
    "View",
    "PlayingTime",
    "Impression",
    "TopCountry",
    "TopCity",
    "TopBrowser",
    "TopDeviceType",
    "WidgetData",
    "WidgetDataWidgetData",
]


class WidgetDataWidgetData(BaseModel):
    asset_id: str
    """Asset ID"""

    page_url: str
    """Page URL where lead was captured"""

    playback_time_instant_milli: str
    """Video time in milliseconds when the lead was captured"""

    workspace_id: str
    """Workspace ID"""

    timestamp: str
    """Lead capture time in seconds since epoch"""

    email: str
    """Email id submitted"""

    name: str
    """Name submitted"""


class WidgetData(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """If there are more items apart from the response given."""

    widget_data: List[WidgetDataWidgetData] = FieldInfo(alias="widgetData")
    """Data about the lead form submission"""


class TopDeviceType(BaseModel):
    key: str
    """Name of the platform"""

    views: str
    """Number of views from a given platform"""

    impressions: str
    """Number of impressions from a given platform"""


class TopBrowser(BaseModel):
    key: str
    """Name of the browser"""

    views: str
    """Number of views from a given browser"""

    impressions: str
    """Number of impressions from a given browser"""


class TopCity(BaseModel):
    key: str
    """Name of the city"""

    views: str
    """Number of views from a given city"""

    impressions: str
    """Number of impressions from a given city"""


class TopCountry(BaseModel):
    key: str
    """Name of the country"""

    views: str
    """Number of views from a given country"""

    impressions: str
    """Number of impressions from a given country"""


class Impression(BaseModel):
    date: int
    """Milliseconds since epoch timestamp for the data point"""

    value: int
    """Number of impressions"""


class PlayingTime(BaseModel):
    date: int
    """Milliseconds since epoch timestamp for the data point"""

    value: int
    """Milliseconds of watch time for the timestamp above. A value of 10000 means 10 seconds of watch time."""


class View(BaseModel):
    date: int
    """Milliseconds since epoch timestamp for the data point"""

    value: int
    """Count of views for the given timestamp"""


class Heatmap(BaseModel):
    bucket: str
    """Buckets of seconds of video. E.g. '0-10', '10-20' etc."""

    count: int
    """Percent of viewers who viewed that portion of video"""


class VideoAssetAnalyticsResponse(BaseModel):
    heatmap: Optional[List[Heatmap]] = None
    """Heatmap data"""

    views: Optional[List[View]] = None
    """Views data"""

    playing_time: List[PlayingTime]

    field_01_m2_qp6_ks1_hm1_je912_s8_k9_dj2_n: Optional[object] = FieldInfo(
        alias="01M2QP6KS1HM1JE912S8K9DJ2N", default=None
    )

    impressions: Optional[List[Impression]] = None

    top_countries: Optional[List[TopCountry]] = None
    """Data for top countries"""

    top_pages: Optional[List[object]] = None
    """Data for top pages"""

    top_cities: Optional[List[TopCity]] = None
    """Data for top cities"""

    top_browsers: Optional[List[TopBrowser]] = None
    """Data for top browsers"""

    top_device_types: Optional[List[TopDeviceType]] = None
    """Data for top device types"""

    widget_data: Optional[WidgetData] = None
