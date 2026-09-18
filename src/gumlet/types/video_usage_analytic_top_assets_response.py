# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoUsageAnalyticTopAssetsResponse", "Data"]


class Data(BaseModel):
    asset_id: Optional[str] = None

    units: Optional[int] = None


class VideoUsageAnalyticTopAssetsResponse(BaseModel):
    data: Optional[List[Data]] = None

    has_next_page: Optional[bool] = None
