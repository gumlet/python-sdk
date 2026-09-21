# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict
from .._types import SequenceNotStr

__all__ = ["SubtitleUploadUploadParams"]


class SubtitleUploadUploadParams(TypedDict, total=False):
    language_codes: SequenceNotStr[str]
    """List of language codes to upload subtitle file (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)"""
