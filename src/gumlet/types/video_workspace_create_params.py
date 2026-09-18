# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr

__all__ = [
    "VideoWorkspaceCreateParams",
    "VideoProtection",
    "Aws",
    "Proxy",
    "Gcs",
    "Dostorage",
    "Wasabi",
    "Cloudinary",
    "Azure",
    "Linode",
    "Backblaze",
    "Cloudflare",
    "Zoom",
]


class VideoWorkspaceCreateParams(TypedDict, total=False):
    name: Required[str]
    """Specify a text string or identifier for the workspace."""

    type: Required[
        Literal[
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
    ]
    """Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases."""

    default_profile_id: str
    """Gumlet provides the functionality of creating multiple video assets using the same set of parameters."""

    insight_property_id: str
    """The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard."""

    video_protection: VideoProtection
    """Gumlet provides multiple options for securing your video playback."""

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

    cloudinary: Cloudinary
    """This is a required field if workspace type is cloudinary."""

    azure: Azure
    """This is a required field if workspace type is azure."""

    linode: Linode
    """This is a required field if workspace type is linode."""

    backblaze: Backblaze
    """This is a required field if workspace type is backblaze."""

    cloudflare: Cloudflare
    """This is a required field if workspace type is cloudflare."""

    zoom: Zoom
    """This is a required field if workspace type is zoom."""


class Zoom(TypedDict, total=False):
    secret: Required[str]


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


class Azure(TypedDict, total=False):
    azure_account_name: Required[str]

    azure_container_name: Required[str]

    azure_shared_token: Required[str]

    azure_path: Required[str]


class Cloudinary(TypedDict, total=False):
    host_name: Required[str]

    cloud_name: Required[str]


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


class VideoProtection(TypedDict, total=False):
    signed_url: bool

    signed_url_secret: str

    blacklisted_countries: SequenceNotStr[str]
    """Example: ["IN","USA"]"""

    whitelisted_referrers: str
