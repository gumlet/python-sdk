# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LiveStreamAnalyticUsageResponse", "BandwidthConsumption", "AssetDuration", "StorageUnit"]


class StorageUnit(BaseModel):
    units: int
    """Storage unit in either bytes or seconds. You can get the information from `storage_data_unit` field."""

    timestamp: int
    """Milliseconds since epoch timestamp for the data point"""


class AssetDuration(BaseModel):
    units: int
    """Input asset seconds"""

    timestamp: int
    """Milliseconds since epoch timestamp for the data point"""


class BandwidthConsumption(BaseModel):
    units: int
    """Bandwidth consumption data in bytes"""

    timestamp: int
    """Milliseconds since epoch timestamp for the data point"""


class LiveStreamAnalyticUsageResponse(BaseModel):
    bandwidth_consumption: Optional[List[BandwidthConsumption]] = None
    """Data about bandwidth consumption"""

    asset_duration: Optional[List[AssetDuration]] = None
    """Data about input seconds processed"""

    storage_unit: Optional[List[StorageUnit]] = None
    """Bytes or seconds of storage used"""

    storage_data_unit: Literal["min", "gb"]
    """Storage data unit information"""
