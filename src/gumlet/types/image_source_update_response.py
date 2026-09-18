# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ImageSourceUpdateResponse",
    "Webfolder",
    "Aws",
    "Proxy",
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
    "Gcs",
    "Dostorage",
    "Wasabi",
    "Linode",
    "Backblaze",
    "Cloudflare",
    "Cloudinary",
    "Azure",
]


class Azure(BaseModel):
    azure_account_name: str

    azure_container_name: str

    azure_shared_token: str

    azure_path: str


class Cloudinary(BaseModel):
    host_name: str

    cloud_name: str


class Cloudflare(BaseModel):
    bucket_name: str

    access_key: str

    account_id: str

    secret: str

    base_path: Optional[str] = None


class Backblaze(BaseModel):
    bucket_name: str

    bucket_region: Optional[str] = None
    """bucket_region or endpoint"""

    endpoint: Optional[str] = None
    """bucket_region or endpoint"""

    access_key: str

    secret: str

    base_path: Optional[str] = None


class Linode(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str


class Wasabi(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str

    base_path: Optional[str] = None


class Dostorage(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str

    base_path: Optional[str] = None


class Gcs(BaseModel):
    bucket_name: str

    service_account_key: str


class FallbackOriginAzure(BaseModel):
    azure_account_name: str

    azure_container_name: str

    azure_shared_token: str

    azure_path: str


class FallbackOriginCloudinary(BaseModel):
    host_name: str

    cloud_name: str


class FallbackOriginCloudflare(BaseModel):
    bucket_name: str

    access_key: str

    account_id: str

    secret: str

    base_path: Optional[str] = None


class FallbackOriginBackblaze(BaseModel):
    bucket_name: str

    bucket_region: Optional[str] = None
    """bucket_region or endpoint"""

    endpoint: Optional[str] = None
    """bucket_region or endpoint"""

    access_key: str

    secret: str

    base_path: Optional[str] = None


class FallbackOriginLinode(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str


class FallbackOriginWasabi(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str

    base_path: Optional[str] = None


class FallbackOriginDostorage(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str

    base_path: Optional[str] = None


class FallbackOriginGcs(BaseModel):
    bucket_name: str

    service_account_key: str


class FallbackOriginProxy(BaseModel):
    whitelisted_domains: str


class FallbackOriginAws(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str

    base_path: Optional[str] = None

    endpoint: Optional[str] = None


class FallbackOriginWebfolder(BaseModel):
    base_url: Optional[str] = None


class FallbackOriginReplaceOperation(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class FallbackOrigin(BaseModel):
    name: str

    type: Literal[
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

    conditions: Optional[List[str]] = None

    replace_operation: Optional[FallbackOriginReplaceOperation] = None

    webfolder: Optional[FallbackOriginWebfolder] = None
    """This is a required field if source type is webfolder."""

    aws: Optional[FallbackOriginAws] = None
    """This is a required field if source type is aws."""

    proxy: Optional[FallbackOriginProxy] = None
    """This is a required field if source type is proxy."""

    gcs: Optional[FallbackOriginGcs] = None
    """This is a required field if source type is gcs."""

    dostorage: Optional[FallbackOriginDostorage] = None
    """This is a required field if source type is dostorage."""

    wasabi: Optional[FallbackOriginWasabi] = None
    """This is a required field if source type is wasabi."""

    linode: Optional[FallbackOriginLinode] = None
    """This is a required field if source type is linode."""

    backblaze: Optional[FallbackOriginBackblaze] = None
    """This is a required field if source type is backblaze."""

    cloudflare: Optional[FallbackOriginCloudflare] = None
    """This is a required field if source type is cloudflare."""

    cloudinary: Optional[FallbackOriginCloudinary] = None
    """This is a required field if source type is cloudinary."""

    azure: Optional[FallbackOriginAzure] = None
    """This is a required field if source type is azure."""

    field_id: Optional[str] = FieldInfo(alias="_id", default=None)

    hetzner: Optional[object] = None

    imgix: Optional[object] = None


class Proxy(BaseModel):
    whitelisted_domains: str


class Aws(BaseModel):
    bucket_name: str

    bucket_region: str

    access_key: str

    secret: str

    base_path: Optional[str] = None

    endpoint: Optional[str] = None


class Webfolder(BaseModel):
    base_url: Optional[str] = None


class ImageSourceUpdateResponse(BaseModel):
    id: Optional[str] = None

    namespace: Optional[str] = None

    type: Literal[
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

    cdn_type: Optional[str] = None

    cdn_cache_time: Optional[int] = None

    canonical_url: Optional[bool] = None

    browser_cache_time: Optional[int] = None

    is_cloudfront: Optional[bool] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    webfolder: Optional[Webfolder] = None
    """This is a required field if source type is webfolder."""

    aws: Optional[Aws] = None
    """This is a required field if source type is aws."""

    proxy: Optional[Proxy] = None
    """This is a required field if source type is proxy."""

    fallback_origins: Optional[List[FallbackOrigin]] = None

    gcs: Optional[Gcs] = None
    """This is a required field if source type is gcs."""

    dostorage: Optional[Dostorage] = None
    """This is a required field if source type is dostorage."""

    wasabi: Optional[Wasabi] = None
    """This is a required field if source type is wasabi."""

    linode: Optional[Linode] = None
    """This is a required field if source type is linode."""

    backblaze: Optional[Backblaze] = None
    """This is a required field if source type is backblaze."""

    cloudflare: Optional[Cloudflare] = None
    """This is a required field if source type is cloudflare."""

    cloudinary: Optional[Cloudinary] = None
    """This is a required field if source type is cloudinary."""

    azure: Optional[Azure] = None
    """This is a required field if source type is azure."""

    default_params: Optional[object] = None

    request_headers: Optional[List[object]] = None

    subdomain: Optional[str] = None

    is_active: Optional[bool] = None

    secure_urls: Optional[bool] = None

    secure_token: Optional[str] = None

    response_headers: Optional[List[object]] = None

    imgix: Optional[object] = None
