# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoAssetCreateResponse", "Input", "InputTransformations", "InputMetadata", "InputCallToAction", "Output"]


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

    position_from_top: Optional[int] = None

    position_from_right: Optional[int] = None

    border_radius: Optional[int] = None

    font_color: Optional[str] = None

    background_color: Optional[str] = None

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


class Input(BaseModel):
    transformations: Optional[InputTransformations] = None

    profile_id: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    metadata: Optional[InputMetadata] = None

    source_url: Optional[str] = None

    call_to_actions: Optional[List[InputCallToAction]] = None


class VideoAssetCreateResponse(BaseModel):
    asset_id: Optional[str] = None
    """Asset ID of created asset."""

    progress: Optional[int] = None
    """Processing progress percentage showing value between 0 and 100."""

    created_at: Optional[int] = None
    """Created at time in milliseconds since epoch"""

    updated_at: Optional[int] = None
    """Updated at time in milliseconds since epoch"""

    status: Optional[str] = None
    """Status of video"""

    tag: Optional[List[str]] = None
    """List of tags"""

    input: Optional[Input] = None
    """Input parameters"""

    output: Optional[Output] = None
    """Output parameters"""

    playlists: Optional[List[str]] = None

    workspace_id: Optional[str] = None
    """Workdspace ID"""
