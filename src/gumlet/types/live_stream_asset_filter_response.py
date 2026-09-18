# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "LiveStreamAssetFilterResponse",
    "AllLiveAsset",
    "AllLiveAssetInput",
    "AllLiveAssetOutput",
    "AllLiveAssetThumbnail",
]


class AllLiveAssetThumbnail(BaseModel):
    preparing: Optional[str] = None

    disconnected: Optional[str] = None

    end: Optional[str] = None


class AllLiveAssetOutput(BaseModel):
    playback_url: Optional[str] = None

    recording_playback_url: Optional[str] = None

    recording_dash_playback_url: Optional[str] = None


class AllLiveAssetInput(BaseModel):
    resolution: Optional[List[str]] = None

    title: Optional[str] = None


class AllLiveAsset(BaseModel):
    status: Optional[str] = None

    stream_key: Optional[str] = None

    live_asset_id: Optional[str] = None

    live_video_source_id: Optional[str] = None

    input: Optional[AllLiveAssetInput] = None

    stream_url: Optional[str] = None

    output: Optional[AllLiveAssetOutput] = None

    thumbnail: Optional[AllLiveAssetThumbnail] = None

    created_at: Optional[int] = None

    updated_at: Optional[int] = None

    deleted_at: Optional[int] = None


class LiveStreamAssetFilterResponse(BaseModel):
    all_live_assets: Optional[List[AllLiveAsset]] = None

    total_live_asset_count: Optional[int] = None

    current_offset: Optional[int] = None
