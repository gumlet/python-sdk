# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "ImageUsageAnalyticRetrieveResponse",
    "BandwidthConsumption",
    "RequestsCount",
    "Status2xx",
    "Status4xx",
    "Status5xx",
    "AvgResponseTime",
    "CdnHitRate",
    "TransformationsCount",
    "OriginHitRate",
    "AvgTransformationResponseTime",
    "ContentType",
    "BandwidthSaving",
    "BandwidthConsumptionBySource",
    "AICreditUsage",
]


class AICreditUsage(BaseModel):
    timestamp: int
    """Timestamp of data point in seconds since epoch."""

    bg_removal: Optional[int] = None
    """Background removal credits used."""

    shadow_gen: Optional[int] = None
    """Shadow generation credits used."""


class BandwidthConsumptionBySource(BaseModel):
    bytes: float
    """Bandwidth usage by the source."""

    domain: str
    """Domain name of the source."""


class BandwidthSaving(BaseModel):
    units: float
    """Number between 0 and 1 depicting bandwidth savings percentage."""

    timestamp: int
    """Timestamp of data point in seconds since epoch."""


class ContentType(BaseModel):
    avif: int
    """Total count of AVIF images delivered"""

    png: int
    """Total count of PNG images delivered"""

    jpeg: int
    """Total count of JPEG images delivered"""

    gif: int
    """Total count of GIF images delivered"""

    webp: int
    """Total count of WEBP images delivered"""

    jxl: int
    """Total count of JPEG-XL images delivered"""

    mp4: int
    """Total count of MP4 videos delivered"""

    timestamp: int
    """Seconds since epoch."""


class AvgTransformationResponseTime(BaseModel):
    timestamp: float
    """Seconds since epoch for the unit given."""

    fetch_time: float
    """Seconds it took to fetch image from origin"""

    response_time: float
    """Seconds it took to prepare final image and send response."""


class OriginHitRate(BaseModel):
    units: float
    """Number between 0 and 1 depicting Origin Cache hit ratio."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class TransformationsCount(BaseModel):
    units: float
    """Number of transformations"""

    timestamp: float
    """Seconds since epoch for the unit given."""


class CdnHitRate(BaseModel):
    units: float
    """Number between 0 and 1 depicting CDN hit ratio percentage."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class AvgResponseTime(BaseModel):
    units: float
    """Response time in seconds."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class Status5xx(BaseModel):
    units: float
    """Value between 0 and 1 depicting percentage of 5xx requests."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class Status4xx(BaseModel):
    units: float
    """Value between 0 and 1 depicting percentage of 4xx requests."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class Status2xx(BaseModel):
    units: float
    """Value between 0 and 1 depicting percentage of 2xx requests."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class RequestsCount(BaseModel):
    units: float
    """Count of requests."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class BandwidthConsumption(BaseModel):
    units: float
    """Value of bandwidth consumption in bytes."""

    timestamp: float
    """Seconds since epoch for the unit given."""


class ImageUsageAnalyticRetrieveResponse(BaseModel):
    bandwidth_consumption: Optional[List[BandwidthConsumption]] = None

    requests_count: Optional[List[RequestsCount]] = None

    status_2xx: Optional[List[Status2xx]] = None

    status_4xx: Optional[List[Status4xx]] = None

    status_5xx: Optional[List[Status5xx]] = None

    avg_response_time: Optional[List[AvgResponseTime]] = None

    cdn_hit_rate: Optional[List[CdnHitRate]] = None

    transformations_count: Optional[List[TransformationsCount]] = None

    origin_hit_rate: Optional[List[OriginHitRate]] = None

    avg_transformation_response_time: Optional[List[AvgTransformationResponseTime]] = None

    content_type: Optional[List[ContentType]] = None

    bandwidth_savings: Optional[List[BandwidthSaving]] = None

    bandwidth_consumption_by_source: Optional[List[BandwidthConsumptionBySource]] = None

    ai_credit_usage: Optional[List[AICreditUsage]] = None
