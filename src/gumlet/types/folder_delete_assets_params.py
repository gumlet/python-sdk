# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["FolderDeleteAssetsParams"]


class FolderDeleteAssetsParams(TypedDict, total=False):
    asset_ids: Required[SequenceNotStr[str]]
