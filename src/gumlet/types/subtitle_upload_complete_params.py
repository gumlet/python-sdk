# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["SubtitleUploadCompleteParams", "UploadResponse"]


class SubtitleUploadCompleteParams(TypedDict, total=False):
    upload_responses: Iterable[UploadResponse]


class UploadResponse(TypedDict, total=False):
    language_code: str
    """Language Code for uploaded .srt or .vtt file."""

    uploaded: bool
    """Status of language uploaded .srt or .vtt file. (If status code was 200, You can mark true else false)"""
