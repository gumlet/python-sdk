# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LiveStreamAssetRetrieveStatusResponse", "Input", "Output", "Thumbnail"]


class Thumbnail(BaseModel):
    preparing: Optional[str] = None

    disconnected: Optional[str] = None

    end: Optional[str] = None


class Output(BaseModel):
    playback_url: Optional[str] = None

    recording_playback_url: Optional[str] = None

    recording_dash_playback_url: Optional[str] = None


class Input(BaseModel):
    resolution: Optional[List[str]] = None

    title: Optional[str] = None


class LiveStreamAssetRetrieveStatusResponse(BaseModel):
    status: Optional[str] = None

    stream_key: Optional[str] = None

    live_asset_id: Optional[str] = None

    live_video_source_id: Optional[str] = None

    input: Optional[Input] = None

    stream_url: Optional[str] = None

    output: Optional[Output] = None

    thumbnail: Optional[Thumbnail] = None

    created_at: Optional[int] = None

    updated_at: Optional[int] = None

    vod_asset_id: Optional[str] = None
