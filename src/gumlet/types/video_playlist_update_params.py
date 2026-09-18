# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoPlaylistUpdateParams", "PlayerConfig"]


class VideoPlaylistUpdateParams(TypedDict, total=False):
    title: str

    description: str

    position: int
    """Playlists have order in which they will be shown on the channel page."""

    player_config: PlayerConfig
    """Configure player settings for this playlist, it overrides the setting set on collection."""

    channel_visibility: bool
    """If true then playlist will be visible on channel page."""


class PlayerConfig(TypedDict, total=False):
    preload: bool

    autoplay: bool

    disable_seek: bool

    disable_player_controls: bool

    powered_by_gumlet_overlay: bool

    allow_drm_protected_videos: bool

    loop: bool

    player_color: str

    include_seo: bool

    subtitle_enabled: bool

    pixel_tags: object

    logo_width: int

    logo_height: int

    dynamic_watermark: bool

    watermark_font_size: int

    watermark_font_color: str

    watermark_bg_color: str

    watermark_interval: int
