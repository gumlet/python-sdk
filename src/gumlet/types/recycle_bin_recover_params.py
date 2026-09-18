# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RecycleBinRecoverParams"]


class RecycleBinRecoverParams(TypedDict, total=False):
    asset_id: Required[str]
    """Gumlet Video Asset Id which needs to be recovered."""
