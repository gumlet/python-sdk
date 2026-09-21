# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "VideoWorkspaceRetrieveResponse",
    "VideoProtection",
    "PlayerConfig",
    "ChannelSettings",
    "ChannelSettingsVisiblePlaylist",
    "StorageEventListener",
]


class StorageEventListener(BaseModel):
    event_id: str
    """Storage event id"""

    profile_id: str
    """Profile ID associated with storage event"""

    profile_name: Optional[str] = None
    """Profile Name"""

    is_varified: bool
    """If this webhook listener is verified."""

    callback_url: Optional[str] = None
    """Callback URL"""

    status: Optional[str] = None
    """Status"""


class ChannelSettingsVisiblePlaylist(BaseModel):
    field_id: str = FieldInfo(alias="_id")
    """Playlist ID"""

    title: str
    """Playlist Title"""


class ChannelSettings(BaseModel):
    title: str
    """Channel title."""

    active: bool
    """Whether the channel is active."""

    privacy_type: Literal["private", "public", "password", "dashboardOnly"]
    """Privacy type of videos in this workspace"""

    channel_access_control: Literal["private", "public"]
    """Whether channel can be accessed publicly or it's invite only channel."""

    dynamic_watermark_type: str
    """What to show in dynamic watermark."""

    disable_invite_email: bool
    """Enable / disable channel invite email."""

    password: Optional[str] = None
    """Password for the channel."""

    color_scheme: Optional[str] = None
    """Color scheme for the channel UI."""

    description: Optional[str] = None
    """Channel description."""

    theme_preference: Optional[str] = None
    """Dark / light theme preference for the channel."""

    cname: Optional[List[str]] = None
    """Custom domains assigned to this channel."""

    hero_url: Optional[str] = None
    """Hero banner URL"""

    hero_updated_at: Optional[str] = None
    """ISO 8601 hero banner update timestamp."""

    icon_url: Optional[str] = None
    """Channel icon URL"""

    icon_updated_at: Optional[str] = None
    """ISO 8601 channel icon update timestamp."""

    temp_cname: Optional[List[str]] = None
    """Array of custom domains which are not yet verified."""

    logo_url: Optional[str] = None
    """Logo URL"""

    logo_updated_at: str
    """ISO 8601 logo update timestamp."""

    visible_playlists: Optional[List[ChannelSettingsVisiblePlaylist]] = None


class PlayerConfig(BaseModel):
    autoplay: bool
    """Video autoplay enable flag. True means autoplay is enabled."""

    disable_seek: bool
    """Seek bar enable / disable"""

    disable_player_controls: bool
    """Disable / enable all player controls"""

    powered_by_gumlet_overlay: bool
    """Whether Gumlet logo shows on player."""

    loop: bool
    """Whether video should loop once it ends. `true` value means video will loop"""

    player_color: str
    """Hex color string of video player color"""

    enable_download_button: bool
    """Enable / disable download button on player."""

    caption_enabled: bool
    """Enable / disable video captions on player."""

    logo_width: Optional[float] = None
    """Logo display width in pixels."""

    logo_height: Optional[float] = None
    """Logo display height in pixels."""

    dynamic_watermark: bool
    """Flag if dynamic watermark is enabled."""

    watermark_font_size: Optional[float] = None
    """Dynamic watermark font size in pixels."""

    watermark_font_color: Optional[str] = None
    """Hex color code of dynamic watermark text."""

    watermark_bg_color: Optional[str] = None
    """Hex color code of background for dynamic watermark text."""

    watermark_interval: Optional[int] = None
    """Interval in milliseconds between dynamic watermark flashing."""

    watermark_visiblity_duration: Optional[int] = None
    """Duration for which the dynamic watermark will be visible on screen."""

    show_video_title: bool
    """Enable / disable video title on player."""

    cast: bool
    """Enable / disable cast button on player."""

    resume_where_left: bool
    """Enable / disable playback from last viewed position. `true` means the playback will resume from last position."""

    cc_color: Optional[str] = None
    """Closed captions / subtitle color."""

    cc_bg_color: Optional[str] = None
    """Closed captions / subtitle background color."""

    cc_font_size: Optional[Literal["small", "medium", "large"]] = None
    """Font size of closed captions."""


class VideoProtection(BaseModel):
    signed_url_secret: Optional[str] = None
    """Secret that is to be used to sign URLs"""

    blacklisted_countries: Optional[List[str]] = None
    """Blacklist of 2 letter country codes."""

    whitelisted_referrers: Optional[List[str]] = None
    """List of whitelisted domains which allow playback for the videos."""

    whitelisted_countries: Optional[str] = None
    """List of whitelisted of 2 letter country codes."""

    signed_url: Optional[bool] = None
    """Boolean value indicating whether signed URL is enabled."""


class VideoWorkspaceRetrieveResponse(BaseModel):
    id: str
    """Workspace ID"""

    name: str
    """Workspace Name"""

    type: str
    """Workspace Type"""

    created_at: str
    """ISO 8601 formatted creation timestamp of this workspace."""

    updated_at: str
    """ISO 8601 formatted update timestamp of this workspace."""

    default_profile_id: Optional[str] = None
    """Profile ID for the default profile of this workspace"""

    default_profile_updated_at: Optional[str] = None
    """ISO 8601 formatted profile update timestamp"""

    insights_enabled: bool
    """Whether Gumlet video analytics is enabled for video embeds in this workspace."""

    video_protection: Optional[VideoProtection] = None

    player_config: PlayerConfig
    """Video player configuration"""

    folders: List[str]
    """List of folder names in this workspace."""

    channel_settings: ChannelSettings

    distinct_tags: Optional[List[str]] = None
    """List of distinct tags in entire workspace."""

    on_streaming_halt: Optional[bool] = None
    """`true` means the workspace is disabled for streaming. No videos will stream from this workspace."""

    storage_event_listener: Optional[List[StorageEventListener]] = None
