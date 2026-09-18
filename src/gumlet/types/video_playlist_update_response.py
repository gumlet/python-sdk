# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["VideoPlaylistUpdateResponse", "PlayerConfig"]


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


class VideoPlaylistUpdateResponse(BaseModel):
    id: Optional[str] = None

    collection_id: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    player_config: Optional[PlayerConfig] = None
