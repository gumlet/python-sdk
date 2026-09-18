# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr

__all__ = [
    "VideoWorkspaceUpdateParams",
    "PlayerConfig",
    "VideoProtection",
    "ChannelSettings",
    "Webfolder",
    "Aws",
    "Proxy",
    "Gcs",
    "Dostorage",
    "Wasabi",
    "Linode",
    "Backblaze",
    "Cloudflare",
    "Cloudinary",
    "Azure",
    "Zoom",
]


class VideoWorkspaceUpdateParams(TypedDict, total=False):
    name: str
    """video workspace name"""

    default_profile_id: str
    """Gumlet provides the functionality of creating multiple video assets using the same set of parameters."""

    temp_cname: SequenceNotStr[str]
    """cname for channel"""

    insight_property_id: str
    """The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard."""

    player_config: PlayerConfig
    """Configure player settings for this playlist, it overrides the setting set on workspace."""

    video_protection: VideoProtection
    """Gumlet provides multiple options for securing your video playback."""

    channel_settings: ChannelSettings
    """Configurations to set various channel settings."""

    type: Literal[
        "proxy",
        "direct-upload",
        "webfolder",
        "aws",
        "gcs",
        "dostorage",
        "wasabi",
        "cloudinary",
        "azure",
        "linode",
        "backblaze",
        "cloudflare",
        "zoom",
    ]
    """Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases."""

    webfolder: Webfolder
    """This is a required field if workspace type is webfolder."""

    aws: Aws
    """This is a required field if workspace type is aws."""

    proxy: Proxy
    """This is a required field if workspace type is proxy."""

    gcs: Gcs
    """This is a required field if workspace type is gcs."""

    dostorage: Dostorage
    """This is a required field if workspace type is dostorage."""

    wasabi: Wasabi
    """This is a required field if workspace type is wasabi."""

    linode: Linode
    """This is a required field if workspace type is linode."""

    backblaze: Backblaze
    """This is a required field if workspace type is backblaze."""

    cloudflare: Cloudflare
    """This is a required field if workspace type is cloudflare."""

    cloudinary: Cloudinary
    """This is a required field if workspace type is cloudinary."""

    azure: Azure
    """This is a required field if workspace type is azure."""

    zoom: Zoom
    """This is a required field if workspace type is zoom."""


class Zoom(TypedDict, total=False):
    secret: Required[str]


class Azure(TypedDict, total=False):
    azure_account_name: Required[str]

    azure_container_name: Required[str]

    azure_shared_token: Required[str]

    azure_path: Required[str]


class Cloudinary(TypedDict, total=False):
    host_name: Required[str]

    cloud_name: Required[str]


class Cloudflare(TypedDict, total=False):
    bucket_name: Required[str]

    access_key: Required[str]

    account_id: Required[str]

    secret: Required[str]

    base_path: str


class Backblaze(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: str
    """bucket_region or endpoint"""

    endpoint: str
    """bucket_region or endpoint"""

    access_key: Required[str]

    secret: Required[str]

    base_path: str


class Linode(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]


class Wasabi(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]

    base_path: str


class Dostorage(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]

    base_path: str


class Gcs(TypedDict, total=False):
    bucket_name: Required[str]

    service_account_key: Required[str]


class Proxy(TypedDict, total=False):
    whitelisted_domains: Required[str]


class Aws(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]

    base_path: str

    endpoint: str


class Webfolder(TypedDict, total=False):
    base_url: str


class ChannelSettings(TypedDict, total=False):
    active: bool

    description: str

    title: str

    privacy_type: Literal['"public"', '"private"', '"password-protected"']

    featured_video: str
    """Video asset id, the asset should be in the same workspace as channel"""

    password: str
    """under channel_settings privacy_type must be "password-protected". Password length should be greater than 5 and lesser than 100 characters."""


class VideoProtection(TypedDict, total=False):
    signed_url: bool

    signed_url_secret: str

    blacklisted_countries: SequenceNotStr[str]
    """Example: ["IN","USA"]"""

    whitelisted_referrers: SequenceNotStr[str]


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

    cast: bool

    show_video_title: bool
