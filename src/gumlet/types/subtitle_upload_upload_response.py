# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["SubtitleUploadUploadResponse", "SignedURL"]


class SignedURL(BaseModel):
    language_code: str
    """Language code"""

    upload_url: str
    """Upload URL on which PUT request should be fired to upload the subtitle"""


class SubtitleUploadUploadResponse(BaseModel):
    asset_id: str
    """Asset ID of Gumlet"""

    signed_urls: List[SignedURL]
    """List of objects with signed URLs for each language"""
