# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["VideoPlaylistCreateAssetParams", "AssetList"]


class VideoPlaylistCreateAssetParams(TypedDict, total=False):
    asset_list: Required[Iterable[AssetList]]


class AssetList(TypedDict, total=False):
    asset_id: str

    position: int
    """Optional, if not provided asset will added at the back/last of playlist"""
