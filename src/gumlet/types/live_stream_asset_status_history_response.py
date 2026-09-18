# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LiveStreamAssetStatusHistoryResponse", "Input", "Output"]


class Output(BaseModel):
    playback_url: Optional[str] = None


class Input(BaseModel):
    resolution: Optional[List[str]] = None


class LiveStreamAssetStatusHistoryResponse(BaseModel):
    status: Optional[str] = None

    stream_key: Optional[str] = None

    live_asset_id: Optional[str] = None

    live_video_source_id: Optional[str] = None

    input: Optional[Input] = None

    stream_url: Optional[str] = None

    output: Optional[Output] = None

    created_at: Optional[int] = None

    updated_at: Optional[int] = None
