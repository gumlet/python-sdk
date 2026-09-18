# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoAnalyticBreakdownDataResponse", "Views", "ViewsData"]


class ViewsData(BaseModel):
    key: Optional[str] = None
    """Breakdown field value"""

    value: Optional[float] = None
    """Metric value for the breakdown key"""

    unit: Optional[str] = None


class Views(BaseModel):
    data: Optional[List[ViewsData]] = None

    has_next_page: Optional[bool] = None
    """Whether there is another page of results"""

    current_page: Optional[int] = None
    """Current page number"""


class VideoAnalyticBreakdownDataResponse(BaseModel):
    views: Optional[Views] = None
