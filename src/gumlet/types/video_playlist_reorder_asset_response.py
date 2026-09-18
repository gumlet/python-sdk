# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoPlaylistReorderAssetResponse"]


class VideoPlaylistReorderAssetResponse(BaseModel):
    success: Optional[bool] = None

    asset_list: Optional[List[str]] = None
