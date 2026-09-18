# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoAnalyticChartDataResponse", "View", "UniqueView", "AnalyticsData", "AnalyticsDataView"]


class AnalyticsDataView(BaseModel):
    x: Optional[str] = None
    """Date in epoch format"""

    y: Optional[str] = None
    """Value"""

    unit: Optional[str] = None


class AnalyticsData(BaseModel):
    views: Optional[List[AnalyticsDataView]] = None


class UniqueView(BaseModel):
    x: Optional[int] = None

    y: Optional[object] = None

    unit: Optional[str] = None


class View(BaseModel):
    x: Optional[int] = None

    y: Optional[object] = None

    unit: Optional[str] = None


class VideoAnalyticChartDataResponse(BaseModel):
    views: Optional[List[View]] = None

    unique_views: Optional[List[UniqueView]] = None

    analytics_data: Optional[AnalyticsData] = None
