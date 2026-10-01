# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["AudioUploadUploadResponse", "SignedURL"]


class SignedURL(BaseModel):
    language_code: str
    """Audio language code"""

    upload_url: str
    """Upload URL on which actual audio file should be uploaded using a PUT request"""


class AudioUploadUploadResponse(BaseModel):
    asset_id: str
    """Gumlet Asset ID"""

    signed_urls: List[SignedURL]
    """Details about signed URLs for each language"""
