# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr

__all__ = [
    "ImageSourceUpdateParams",
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
    "FallbackOrigin",
    "FallbackOriginReplaceOperation",
    "FallbackOriginWebfolder",
    "FallbackOriginAws",
    "FallbackOriginProxy",
    "FallbackOriginGcs",
    "FallbackOriginDostorage",
    "FallbackOriginWasabi",
    "FallbackOriginLinode",
    "FallbackOriginBackblaze",
    "FallbackOriginCloudflare",
    "FallbackOriginCloudinary",
    "FallbackOriginAzure",
]


class ImageSourceUpdateParams(TypedDict, total=False):
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
    ]

    webfolder: Webfolder
    """This is a required field if source type is webfolder."""

    aws: Aws
    """This is a required field if source type is aws."""

    proxy: Proxy
    """This is a required field if source type is proxy."""

    gcs: Gcs
    """This is a required field if source type is gcs."""

    dostorage: Dostorage
    """This is a required field if source type is dostorage."""

    wasabi: Wasabi
    """This is a required field if source type is wasabi."""

    linode: Linode
    """This is a required field if source type is linode."""

    backblaze: Backblaze
    """This is a required field if source type is backblaze."""

    cloudflare: Cloudflare
    """This is a required field if source type is cloudflare."""

    cloudinary: Cloudinary
    """This is a required field if source type is cloudinary."""

    azure: Azure
    """This is a required field if source type is azure."""

    default_params: object

    error_image: str
    """URL for error image to display when we get broken image from your origin."""

    request_headers: Iterable[object]

    response_headers: Iterable[object]

    temp_cname: SequenceNotStr[str]

    browser_cache_time: int
    """Browser cache time in seconds. For example setting this to 3600 caches the image in browser for 3600 seconds (1 hour)"""

    cdn_cache_time: int
    """CDN cache time in seconds."""

    is_active: bool
    """Enable / disable source."""

    cname: SequenceNotStr[str]
    """List of verified CNAMEs"""

    fallback_origins: Iterable[FallbackOrigin]
    """List of fallback origins"""


class FallbackOriginAzure(TypedDict, total=False):
    azure_account_name: Required[str]

    azure_container_name: Required[str]

    azure_shared_token: Required[str]

    azure_path: Required[str]


class FallbackOriginCloudinary(TypedDict, total=False):
    host_name: Required[str]

    cloud_name: Required[str]


class FallbackOriginCloudflare(TypedDict, total=False):
    bucket_name: Required[str]

    access_key: Required[str]

    account_id: Required[str]

    secret: Required[str]

    base_path: str


class FallbackOriginBackblaze(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: str
    """bucket_region or endpoint"""

    endpoint: str
    """bucket_region or endpoint"""

    access_key: Required[str]

    secret: Required[str]

    base_path: str


class FallbackOriginLinode(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]


class FallbackOriginWasabi(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]

    base_path: str


class FallbackOriginDostorage(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]

    base_path: str


class FallbackOriginGcs(TypedDict, total=False):
    bucket_name: Required[str]

    service_account_key: Required[str]


class FallbackOriginProxy(TypedDict, total=False):
    whitelisted_domains: Required[str]


class FallbackOriginAws(TypedDict, total=False):
    bucket_name: Required[str]

    bucket_region: Required[str]

    access_key: Required[str]

    secret: Required[str]

    base_path: str

    endpoint: str


class FallbackOriginWebfolder(TypedDict, total=False):
    base_url: str


_FallbackOriginReplaceOperationReservedKeywords = TypedDict(
    "_FallbackOriginReplaceOperationReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class FallbackOriginReplaceOperation(_FallbackOriginReplaceOperationReservedKeywords, total=False):
    to: str


class FallbackOrigin(TypedDict, total=False):
    conditions: Required[SequenceNotStr[str]]

    name: Required[str]
    """Name of fallback"""

    type: Required[
        Literal[
            "dostorage",
            "aws",
            "wasabi",
            "hetzner",
            "backblaze",
            "webfolder",
            "gcs",
            "azure",
            "cloudflare",
            "imgix",
            "cloudinary",
            "proxy",
            "wordpress",
            "linode",
        ]
    ]
    """Type of fallback origin"""

    replace_operation: Required[FallbackOriginReplaceOperation]

    webfolder: FallbackOriginWebfolder
    """This is a required field if source type is webfolder."""

    aws: FallbackOriginAws
    """This is a required field if source type is aws."""

    proxy: FallbackOriginProxy
    """This is a required field if source type is proxy."""

    gcs: FallbackOriginGcs
    """This is a required field if source type is gcs."""

    dostorage: FallbackOriginDostorage
    """This is a required field if source type is dostorage."""

    wasabi: FallbackOriginWasabi
    """This is a required field if source type is wasabi."""

    linode: FallbackOriginLinode
    """This is a required field if source type is linode."""

    backblaze: FallbackOriginBackblaze
    """This is a required field if source type is backblaze."""

    cloudflare: FallbackOriginCloudflare
    """This is a required field if source type is cloudflare."""

    cloudinary: FallbackOriginCloudinary
    """This is a required field if source type is cloudinary."""

    azure: FallbackOriginAzure
    """This is a required field if source type is azure."""


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
