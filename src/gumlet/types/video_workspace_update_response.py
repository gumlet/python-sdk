# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoWorkspaceUpdateResponse", "VideoProtection", "PlayerConfig", "Aws", "EmbedDetails", "ChannelSettings"]


class ChannelSettings(BaseModel):
    title: Optional[str] = None

    active: Optional[bool] = None

    description: Optional[str] = None

    privacy_type: Optional[str] = None

    custom_logo: Optional[bool] = None

    logo_url: Optional[str] = None

    cname: Optional[List[str]] = None

    temp_cname: Optional[List[str]] = None


class EmbedDetails(BaseModel):
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

    powered_by_gumlet_overlay: Optional[bool] = None

    allow_drm_protected_videos: Optional[bool] = None

    pixel_tags: Optional[object] = None

    loop: Optional[bool] = None

    subtitle_enabled: Optional[bool] = None


class Aws(BaseModel):
    bucket_name: Optional[str] = None

    bucket_region: Optional[str] = None

    access_key: Optional[str] = None

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


class VideoProtection(BaseModel):
    signed_url: Optional[bool] = None

    signed_url_secret: Optional[str] = None


class VideoWorkspaceUpdateResponse(BaseModel):
    id: str

    name: str

    type: str

    created_at: str

    updated_at: str

    video_protection: Optional[VideoProtection] = None

    player_config: PlayerConfig

    default_profile_id: Optional[str] = None

    insight_property_id: Optional[str] = None

    aws: Optional[Aws] = None

    embed_details: Optional[EmbedDetails] = None

    folders: List[str]

    channel_settings: ChannelSettings

    insights_enabled: bool
    """Whether Gumlet video analytics is enabled for this workspace."""
