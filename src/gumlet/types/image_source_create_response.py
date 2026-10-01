# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ImageSourceCreateResponse", "Webfolder", "DefaultParams"]


class DefaultParams(BaseModel):
    format: Optional[str] = None

    compress: Optional[str] = None


class Webfolder(BaseModel):
    base_url: Optional[str] = None


class ImageSourceCreateResponse(BaseModel):
    id: Optional[str] = None
    """Image source ID"""

    namespace: Optional[str] = None
    """Souce namespace"""

    type: Optional[str] = None
    """Source type"""

    cdn_cache_time: Optional[int] = None
    """CDN cache time in seconds"""

    canonical_url: Optional[bool] = None

    browser_cache_time: Optional[int] = None
    """Browser cache time in seconds"""

    is_cloudfront: Optional[bool] = None

    created_at: Optional[datetime] = None
    """Source created timestamp in ISO 8601"""

    updated_at: Optional[datetime] = None
    """Source updated timestamp in ISO 8601"""

    webfolder: Optional[Webfolder] = None

    default_params: Optional[DefaultParams] = None

    subdomain: Optional[str] = None

    is_active: Optional[bool] = None
    """Boolean flag indicating if source is active"""
