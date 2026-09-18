# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict
from .._types import SequenceNotStr

__all__ = ["AudioUploadUploadParams"]


class AudioUploadUploadParams(TypedDict, total=False):
    language_codes: SequenceNotStr[str]
    """List of language Code to upload audio file  (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)"""
