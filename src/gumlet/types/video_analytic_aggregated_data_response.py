# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["VideoAnalyticAggregatedDataResponse", "Views", "ViewsSum"]


class ViewsSum(BaseModel):
    value: Optional[int] = None

    unit: Optional[str] = None


class Views(BaseModel):
    sum: Optional[ViewsSum] = None


class VideoAnalyticAggregatedDataResponse(BaseModel):
    views: Optional[Views] = None
