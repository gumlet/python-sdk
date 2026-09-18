# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ImageSourceCreateParams",
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
    "Webfolder",
]


class ImageSourceCreateParams(TypedDict, total=False):
    namespace: Required[str]
    """unique subdomain associated with the image source"""

    type: Required[
        Literal[
            "proxy",
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

    cloudinary: Cloudinary
    """This is a required field if source type is cloudinary."""

    azure: Azure
    """This is a required field if source type is azure."""

    linode: Linode
    """This is a required field if source type is linode."""

    backblaze: Backblaze
    """This is a required field if source type is backblaze."""

    cloudflare: Cloudflare
    """This is a required field if source type is cloudflare."""

    webfolder: Webfolder


class Webfolder(TypedDict, total=False):
    base_url: str


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
