# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["VideoAssetDeleteManyParams"]


class VideoAssetDeleteManyParams(TypedDict, total=False):
    asset_list: Required[SequenceNotStr[str]]
    """LIst of asset ids to delete"""

    source_id: Required[str]
    """Workspace ID from which assets needs to be deleted."""
