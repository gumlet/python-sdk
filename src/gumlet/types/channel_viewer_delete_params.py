# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["ChannelViewerDeleteParams"]


class ChannelViewerDeleteParams(TypedDict, total=False):
    emails: Required[SequenceNotStr[str]]
    """Email addresses of viewers to remove. A maximum of 200 viewers can be removed in one request."""
