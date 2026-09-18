# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MultipartUploadCompleteParams", "Part"]


class MultipartUploadCompleteParams(TypedDict, total=False):
    parts: Iterable[Part]
    """List of object containing part number with ETag received as a response header while uploading each part"""


class Part(TypedDict, total=False):
    part_number: Annotated[int, PropertyInfo(alias="PartNumber")]

    e_tag: Annotated[str, PropertyInfo(alias="ETag")]
    """ETag received while uploading the part using PUT"""
