# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VideoAssetThumbnailSelectResponse"]


class VideoAssetThumbnailSelectResponse(BaseModel):
    success: Optional[bool] = None

    asset_id: Optional[str] = None

    thumbnail_updated_at: Optional[int] = None
    """Milliseconds since epoch for the updated time."""
