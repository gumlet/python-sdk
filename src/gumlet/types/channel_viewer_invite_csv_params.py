# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from .._types import FileTypes

__all__ = ["ChannelViewerInviteCsvParams"]


class ChannelViewerInviteCsvParams(TypedDict, total=False):
    viewers_csv: Required[FileTypes]
    """CSV file containing viewer rows. Required columns: email, name. Maximum 500 viewers."""
