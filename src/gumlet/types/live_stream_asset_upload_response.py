# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["LiveStreamAssetUploadResponse", "PresignedUploadURLs"]


class PresignedUploadURLs(BaseModel):
    preparing: Optional[str] = None

    disconnected: Optional[str] = None

    end: Optional[str] = None


class LiveStreamAssetUploadResponse(BaseModel):
    message: Optional[str] = None

    presigned_upload_urls: Optional[PresignedUploadURLs] = None
