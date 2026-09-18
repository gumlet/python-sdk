# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ChannelViewerInviteParams", "User"]


class ChannelViewerInviteParams(TypedDict, total=False):
    users: Required[Iterable[User]]
    """List of viewers to invite. A maximum of 200 viewers can be invited in one request."""


class User(TypedDict, total=False):
    email: Required[str]
    """Viewer email address."""

    name: Required[str]
    """Viewer display name."""
