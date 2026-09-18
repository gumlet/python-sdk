# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

__all__ = ["FolderUpdateParams", "Variant", "Variant2"]


class Variant2(TypedDict, total=False):
    name: str
    """New folder name."""

    parent_id: str
    """Parent folder id in which we need to move assets."""

    asset_ids: Required[SequenceNotStr[str]]


class Variant(TypedDict, total=False):
    name: Required[str]
    """New folder name."""

    parent_id: Optional[str]
    """New parent folder id. Send `null` to move the folder to the root level."""

    asset_ids: SequenceNotStr[str]
    """Asset ids to move into this folder."""


FolderUpdateParams: TypeAlias = Union[Variant, Variant2]
