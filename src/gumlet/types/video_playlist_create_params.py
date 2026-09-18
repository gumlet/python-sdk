# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoPlaylistCreateParams"]


class VideoPlaylistCreateParams(TypedDict, total=False):
    collection_id: Required[str]

    title: Required[str]

    description: str
