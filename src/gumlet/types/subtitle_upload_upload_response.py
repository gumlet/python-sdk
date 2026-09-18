# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["SubtitleUploadUploadResponse", "SignedURL"]


class SignedURL(BaseModel):
    language_code: str

    upload_url: str


class SubtitleUploadUploadResponse(BaseModel):
    asset_id: str
    """Asset ID of Gumlet"""

    signed_urls: List[SignedURL]
