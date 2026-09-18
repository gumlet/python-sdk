# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VideoAssetThumbnailUploadResponse"]


class VideoAssetThumbnailUploadResponse(BaseModel):
    upload_url: Optional[str] = None

    asset_id: Optional[str] = None

    thumbnail_updated_at: Optional[int] = None
    """Thumbnail updated at timestamp in milliseconds since epoch"""
