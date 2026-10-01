# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "ImageSourceListResponse",
    "AllSource",
    "AllSourceAws",
    "AllSourceWebfolder",
    "AllSourceWasabi",
    "AllSourceGcs",
    "AllSourceWordpress",
    "AllSourceBackblaze",
    "AllSourceHetzner",
    "AllSourceDostorage",
    "AllSourceAzure",
    "AllSourceLinode",
    "AllSourceCloudinary",
]


class AllSourceCloudinary(BaseModel):
    cloud_name: str


class AllSourceLinode(BaseModel):
    bucket_name: str

    bucket_region: str


class AllSourceAzure(BaseModel):
    azure_account_name: str

    azure_container_name: Optional[str] = None

    azure_path: str


class AllSourceDostorage(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class AllSourceHetzner(BaseModel):
    bucket_name: Optional[str] = None

    base_path: Optional[str] = None


class AllSourceBackblaze(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class AllSourceWordpress(BaseModel):
    website_url: str


class AllSourceGcs(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class AllSourceWasabi(BaseModel):
    bucket_name: str

    base_path: Optional[str] = None


class AllSourceWebfolder(BaseModel):
    base_url: str


class AllSourceAws(BaseModel):
    bucket_name: Optional[str] = None

    bucket_region: Optional[str] = None

    access_key: Optional[str] = None

    secret: Optional[str] = None

    base_path: Optional[str] = None


class AllSource(BaseModel):
    id: str
    """Image source ID"""

    type: Optional[str] = None
    """Source type"""

    created_at: Optional[datetime] = None
    """Created at timestamo in ISO 8601"""

    updated_at: Optional[datetime] = None
    """Updated at timestamo in ISO 8601"""

    aws: Optional[AllSourceAws] = None

    namespace: str
    """Source namespace (i.e. subdomain of gumlet.io)"""

    webfolder: Optional[AllSourceWebfolder] = None

    cname: Optional[List[str]] = None
    """Custom domains assigned to this source."""

    wasabi: Optional[AllSourceWasabi] = None

    gcs: Optional[AllSourceGcs] = None

    wordpress: Optional[AllSourceWordpress] = None

    backblaze: Optional[AllSourceBackblaze] = None

    hetzner: Optional[AllSourceHetzner] = None

    dostorage: Optional[AllSourceDostorage] = None

    azure: Optional[AllSourceAzure] = None

    linode: Optional[AllSourceLinode] = None

    cloudinary: Optional[AllSourceCloudinary] = None


class ImageSourceListResponse(BaseModel):
    all_sources: Optional[List[AllSource]] = None
