# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict
from .._types import SequenceNotStr

__all__ = ["ImageSourcePurgeCacheParams"]


class ImageSourcePurgeCacheParams(TypedDict, total=False):
    paths: SequenceNotStr[str]
    """An array of path of images to purge. It should be provided without any query parameters."""
