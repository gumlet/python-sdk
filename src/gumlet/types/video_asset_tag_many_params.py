# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["VideoAssetTagManyParams"]


class VideoAssetTagManyParams(TypedDict, total=False):
    asset_list: Required[SequenceNotStr[str]]
    """List of asset ids to update the tags for."""

    source_id: Required[str]
    """Workspace ID in which the videos needs the operation"""

    add_tags: Required[SequenceNotStr[str]]
    """List of tags to add to given assets."""

    remove_tags: Required[SequenceNotStr[str]]
    """List of tags to remove from given assets. Pass empty array if nothing is to be removed."""
