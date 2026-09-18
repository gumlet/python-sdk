# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "VideoUsageAnalyticRetrieveResponse",
    "DrmRequest",
    "BandwidthConsumption",
    "StorageUnit",
    "AssetDuration",
    "TopAsset",
    "AICreditUsage",
    "ErroredVideo",
]


class ErroredVideo(BaseModel):
    timestamp: int
    """Seconds since epoch for the unit given."""

    units: int
    """Number of errored videos in the timeframe"""


class AICreditUsage(BaseModel):
    timestamp: int
    """Seconds since epoch for the unit given."""


class TopAsset(BaseModel):
    asset_id: str
    """Asset ID"""

    units: str
    """Bandwidth consumption by this asset in bytes."""

    workspace_id: str
    """Workspace ID"""

    duration: str
    """Seconds of streaming minutes consumed by this asset."""

    title: str
    """Asset Title"""

    collection_name: str
    """Workspace Name"""


class AssetDuration(BaseModel):
    units: int
    """Total transcoding duration in seconds."""

    timestamp: int
    """Seconds since epoch for the unit given."""


class StorageUnit(BaseModel):
    units: int
    """The storage data in bytes or seconds."""

    timestamp: int
    """Seconds since epoch for the unit given."""


class BandwidthConsumption(BaseModel):
    units: int
    """The bandwidth consumption data in bytes."""

    timestamp: int
    """Seconds since epoch for the unit given."""


class DrmRequest(BaseModel):
    units: int
    """Number of DRM requests."""

    timestamp: int
    """Seconds since epoch for the unit given."""


class VideoUsageAnalyticRetrieveResponse(BaseModel):
    drm_requests: Optional[List[DrmRequest]] = None

    bandwidth_saving_unit: Optional[Literal[""]] = None
    """The unit for bandwidth saving data."""

    storage_data_unit: Optional[Literal["gb", "min"]] = None
    """The unit for the storage data."""

    bandwidth_consumption: Optional[List[BandwidthConsumption]] = None

    storage_unit: Optional[List[StorageUnit]] = None

    asset_duration: Optional[List[AssetDuration]] = None

    top_assets: Optional[List[TopAsset]] = None

    has_more_top_asset: Optional[bool] = None
    """Indicates whether the list of top assets is exhaustive or if it has more assets."""

    ai_credit_usage: Optional[List[AICreditUsage]] = None

    errored_videos: Optional[List[ErroredVideo]] = None
