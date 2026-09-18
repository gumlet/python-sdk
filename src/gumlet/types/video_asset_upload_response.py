# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoAssetUploadResponse", "Input", "InputTransformations", "InputMetadata", "InputCallToAction", "Output"]


class Output(BaseModel):
    format: Optional[str] = None

    status_url: Optional[str] = None

    playback_url: Optional[str] = None

    thumbnail_url: Optional[List[str]] = None


class InputCallToAction(BaseModel):
    start_time: Optional[int] = None

    end_time: Optional[int] = None

    text: Optional[str] = None

    url: Optional[str] = None

    html_target: Optional[str] = None


class InputMetadata(BaseModel):
    headermeta: Optional[str] = None


class InputTransformations(BaseModel):
    format: Optional[str] = None

    resolution: Optional[List[str]] = None

    audio_codec: Optional[List[str]] = None

    video_codec: Optional[List[str]] = None

    thumbnail: Optional[List[str]] = None

    thumbnail_format: Optional[str] = None

    mp4_access: Optional[bool] = None

    per_title_encoding: Optional[bool] = None

    original_deleted: Optional[bool] = None


class Input(BaseModel):
    transformations: Optional[InputTransformations] = None

    profile_id: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    metadata: Optional[InputMetadata] = None

    source_url: Optional[str] = None

    call_to_actions: Optional[List[InputCallToAction]] = None


class VideoAssetUploadResponse(BaseModel):
    asset_id: Optional[str] = None

    progress: Optional[int] = None

    created_at: Optional[int] = None

    updated_at: Optional[int] = None

    status: Optional[str] = None

    tag: Optional[List[str]] = None

    source_id: Optional[str] = None

    collection_id: Optional[str] = None

    input: Optional[Input] = None

    output: Optional[Output] = None

    upload_url: Optional[str] = None

    playlists: Optional[List[str]] = None
