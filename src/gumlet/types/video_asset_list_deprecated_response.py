# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "VideoAssetListDeprecatedResponse",
    "AllAsset",
    "AllAssetInput",
    "AllAssetInputTransformations",
    "AllAssetInputAdditionalTrack",
    "AllAssetOutput",
]


class AllAssetOutput(BaseModel):
    format: Optional[str] = None

    status_url: Optional[str] = None

    playback_url: Optional[str] = None

    thumbnail_url: Optional[List[str]] = None


class AllAssetInputAdditionalTrack(BaseModel):
    url: Optional[str] = None

    type: Optional[str] = None

    language_code: Optional[str] = None

    name: Optional[str] = None


class AllAssetInputTransformations(BaseModel):
    resolution: Optional[str] = None

    format: Optional[str] = None

    audio_codec: Optional[List[str]] = None

    video_codec: Optional[List[str]] = None

    thumbnail: Optional[List[str]] = None

    thumbnail_format: Optional[str] = None

    mp4_access: Optional[bool] = None

    audio_only: Optional[bool] = None

    keep_original: Optional[bool] = None

    per_title_encoding: Optional[bool] = None

    process_low_resolution_input: Optional[bool] = None


class AllAssetInput(BaseModel):
    transformations: Optional[AllAssetInputTransformations] = None

    source_url: Optional[str] = None

    size: Optional[int] = None

    duration: Optional[float] = None

    aspect_ratio: Optional[str] = None

    fps: Optional[int] = None

    width: Optional[int] = None

    height: Optional[int] = None

    additional_tracks: Optional[List[AllAssetInputAdditionalTrack]] = None


class AllAsset(BaseModel):
    asset_id: Optional[str] = None

    progress: Optional[int] = None

    created_at: Optional[int] = None

    status: Optional[str] = None

    tag: Optional[str] = None

    source_id: Optional[str] = None

    input: Optional[AllAssetInput] = None

    output: Optional[AllAssetOutput] = None


class VideoAssetListDeprecatedResponse(BaseModel):
    all_assets: Optional[List[AllAsset]] = None

    total_asset_count: Optional[int] = None

    current_offset: Optional[int] = None

    distinct_tags: Optional[List[str]] = None
