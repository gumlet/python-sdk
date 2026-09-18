# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["LiveStreamAssetUpdateParams"]


class LiveStreamAssetUpdateParams(TypedDict, total=False):
    live_asset_id: Required[str]
    """Gumlet live video asset id."""

    title: str
    """Your live stream asset title"""

    start_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
