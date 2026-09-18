# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["VideoPlaylistReorderAssetParams", "Variant", "Variant2"]


class Variant2(TypedDict, total=False):
    sort_by: Required[Literal["title", "created_at"]]

    sort_order: Required[Literal["asc", "desc"]]


class Variant(TypedDict, total=False):
    asset_id: Required[str]
    """Asset id to move."""

    page_number: Required[int]
    """Current playlist page number."""

    page_size: Required[int]
    """Playlist page size used by the caller."""

    asset_position: Required[int]
    """Zero-based position inside the provided page."""


VideoPlaylistReorderAssetParams: TypeAlias = Union[Variant, Variant2]
