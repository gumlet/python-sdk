# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ImageSourceListResponse",
    "ImageSourceListResponse2",
    "Aws",
    "Webfolder",
    "Wasabi",
    "Gcs",
    "Wordpress",
    "Backblaze",
    "Hetzner",
    "Dostorage",
    "Azure",
    "Linode",
    "Cloudinary",
]


class Cloudinary(BaseModel):
    cloud_name: str


class Linode(BaseModel):
    bucket_name: str

    bucket_region: str


class Azure(BaseModel):
    azure_account_name: str

    azure_container_name: Optional[str] = None

    azure_path: str


class Dostorage(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class Hetzner(BaseModel):
    bucket_name: Optional[str] = None

    base_path: Optional[str] = None


class Backblaze(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class Wordpress(BaseModel):
    website_url: str


class Gcs(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class Wasabi(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class Webfolder(BaseModel):
    base_url: str


class Aws(BaseModel):
    bucket_name: Optional[str] = None

    bucket_region: Optional[str] = None

    access_key: Optional[str] = None

    secret: Optional[str] = None

    base_path: Optional[str] = None


class ImageSourceListResponse2(BaseModel):
    id: str
    """Image source ID"""

    type: Optional[str] = None
    """Source type"""

    created_at: Optional[datetime] = None
    """Created at timestamo in ISO 8601"""

    updated_at: Optional[datetime] = None
    """Updated at timestamo in ISO 8601"""

    aws: Optional[Aws] = None

    namespace: str
    """Source namespace (i.e. subdomain of gumlet.io)"""

    webfolder: Optional[Webfolder] = None

    cname: Optional[List[str]] = None
    """Custom domains assigned to this source."""

    wasabi: Optional[Wasabi] = None

    gcs: Optional[Gcs] = None

    wordpress: Optional[Wordpress] = None

    backblaze: Optional[Backblaze] = None

    hetzner: Optional[Hetzner] = None

    dostorage: Optional[Dostorage] = None

    azure: Optional[Azure] = None

    linode: Optional[Linode] = None

    cloudinary: Optional[Cloudinary] = None


ImageSourceListResponse: TypeAlias = ImageSourceListResponse2
