# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoAssetCreateUpdateChapterParams", "Chapter"]


class VideoAssetCreateUpdateChapterParams(TypedDict, total=False):
    chapters: Required[Iterable[Chapter]]


class Chapter(TypedDict, total=False):
    label: Required[str]
    """Label for the chapter."""

    start_time: Required[Annotated[int, PropertyInfo(alias="startTime")]]
    """Start time of chapter in seconds. 0 means chapter is put as the video starts."""
