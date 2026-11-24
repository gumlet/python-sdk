# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VideoAssetThumbnailUploadResponse"]


class VideoAssetThumbnailUploadResponse(BaseModel):
    upload_url: Optional[str] = None
    """Upload URL on which new thumbnail must be uploaded using a PUT request"""

    asset_id: Optional[str] = None
    """Asset ID"""

    thumbnail_updated_at: Optional[int] = None
    """Thumbnail updated at timestamp in milliseconds since epoch"""
