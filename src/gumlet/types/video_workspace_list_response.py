# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "VideoWorkspaceListResponse",
    "AllSource",
    "AllSourceVideoProtection",
    "AllSourcePlayerConfig",
    "AllSourceAws",
    "AllSourceEmbedDetails",
    "AllSourceChannelSettings",
]


class AllSourceChannelSettings(BaseModel):
    title: Optional[str] = None

    active: Optional[bool] = None

    description: Optional[str] = None

    privacy_type: Optional[str] = None

    custom_logo: Optional[bool] = None

    logo_url: Optional[str] = None

    cname: Optional[List[str]] = None

    temp_cname: Optional[List[str]] = None


class AllSourceEmbedDetails(BaseModel):
    pixel_tags: Optional[object] = None

    preload: Optional[bool] = None

    autoplay: Optional[bool] = None

    logo_width: Optional[int] = None

    logo_height: Optional[int] = None

    player_color: Optional[str] = None

    is_seo: Optional[bool] = None

    dynamic_watermark: Optional[bool] = None

    disable_seek: Optional[bool] = None

    disable_player_controls: Optional[bool] = None

    allow_drm_protected_videos: Optional[bool] = None

    powered_by_gumlet_overlay: Optional[bool] = None

    loop: Optional[bool] = None

    subtitle_enabled: Optional[bool] = None

    watermark_bg_color: Optional[str] = None

    watermark_font_color: Optional[str] = None

    watermark_font_size: Optional[int] = None

    watermark_interval: Optional[int] = None


class AllSourceAws(BaseModel):
    bucket_name: Optional[str] = None

    bucket_region: Optional[str] = None

    access_key: Optional[str] = None

    secret: Optional[str] = None


class AllSourcePlayerConfig(BaseModel):
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


class AllSourceVideoProtection(BaseModel):
    signed_url: Optional[bool] = None

    signed_url_secret: Optional[str] = None


class AllSource(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    video_protection: Optional[AllSourceVideoProtection] = None

    player_config: Optional[AllSourcePlayerConfig] = None

    default_profile_id: Optional[str] = None

    insight_property_id: Optional[str] = None

    aws: Optional[AllSourceAws] = None

    embed_details: Optional[AllSourceEmbedDetails] = None

    folders: Optional[List[str]] = None

    channel_settings: Optional[AllSourceChannelSettings] = None

    on_streaming_halt: Optional[bool] = None
    """Whether the workspace is disabled for streaming. `true` means it's disabled."""


class VideoWorkspaceListResponse(BaseModel):
    all_sources: Optional[List[AllSource]] = None
