# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoWorkspaceCreateResponse", "PlayerConfig", "Zoom", "EmbedDetails", "ChannelSettings"]


class ChannelSettings(BaseModel):
    active: Optional[bool] = None

    privacy_type: Optional[str] = None


class EmbedDetails(BaseModel):
    powered_by_gumlet_overlay: Optional[bool] = None

    allow_drm_protected_videos: Optional[bool] = None

    preload: Optional[bool] = None

    autoplay: Optional[bool] = None

    logo_width: Optional[int] = None

    logo_height: Optional[int] = None

    player_color: Optional[str] = None

    is_seo: Optional[bool] = None

    dynamic_watermark: Optional[bool] = None

    watermark_font_size: Optional[int] = None

    watermark_font_color: Optional[str] = None

    watermark_bg_color: Optional[str] = None

    watermark_interval: Optional[int] = None

    disable_seek: Optional[bool] = None

    disable_player_controls: Optional[bool] = None

    loop: Optional[bool] = None

    subtitle_enabled: Optional[bool] = None


class Zoom(BaseModel):
    secret: Optional[str] = None


class PlayerConfig(BaseModel):
    preload: Optional[bool] = None

    autoplay: Optional[bool] = None

    disable_seek: Optional[bool] = None

    disable_player_controls: Optional[bool] = None

    powered_by_gumlet_overlay: Optional[bool] = None

    allow_drm_protected_videos: Optional[bool] = None

    loop: Optional[bool] = None

    player_color: Optional[str] = None

    include_seo: Optional[bool] = None

    subtitle_enabled: Optional[bool] = None

    pixel_tags: Optional[object] = None

    logo_width: Optional[int] = None

    logo_height: Optional[int] = None

    dynamic_watermark: Optional[bool] = None

    watermark_font_size: Optional[int] = None

    watermark_font_color: Optional[str] = None

    watermark_bg_color: Optional[str] = None

    watermark_interval: Optional[int] = None


class VideoWorkspaceCreateResponse(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    video_protection: Optional[object] = None

    player_config: Optional[PlayerConfig] = None

    default_profile_id: Optional[str] = None

    insight_property_id: Optional[str] = None

    zoom: Optional[Zoom] = None

    embed_details: Optional[EmbedDetails] = None

    folders: Optional[List[str]] = None

    channel_settings: Optional[ChannelSettings] = None
