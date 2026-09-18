# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["ImageSourceCreateResponse", "Webfolder", "DefaultParams"]


class DefaultParams(BaseModel):
    format: Optional[str] = None

    compress: Optional[str] = None


class Webfolder(BaseModel):
    base_url: Optional[str] = None


class ImageSourceCreateResponse(BaseModel):
    id: Optional[str] = None

    namespace: Optional[str] = None

    type: Optional[str] = None

    cdn_type: Optional[str] = None

    cdn_cache_time: Optional[int] = None

    canonical_url: Optional[bool] = None

    browser_cache_time: Optional[int] = None

    is_cloudfront: Optional[bool] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    webfolder: Optional[Webfolder] = None

    default_params: Optional[DefaultParams] = None

    subdomain: Optional[str] = None

    is_active: Optional[bool] = None
