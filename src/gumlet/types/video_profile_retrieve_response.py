# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoProfileRetrieveResponse", "Transformations"]


class Transformations(BaseModel):
    format: Optional[str] = None

    audio_codec: Optional[List[str]] = None

    video_codec: Optional[List[str]] = None

    thumbnail: Optional[List[str]] = None

    thumbnail_format: Optional[str] = None

    mp4_access: Optional[bool] = None

    per_title_encoding: Optional[bool] = None

    resolution: Optional[str] = None

    generate_chapters: Optional[bool] = None
    """Flag that shows if AI generated chapters are enabled"""


class VideoProfileRetrieveResponse(BaseModel):
    profile_id: Optional[str] = None

    name: Optional[str] = None

    transformations: Optional[Transformations] = None

    created_at: Optional[int] = None

    updated_at: Optional[int] = None
