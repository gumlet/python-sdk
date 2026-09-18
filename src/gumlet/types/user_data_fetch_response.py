# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["UserDataFetchResponse", "Metadata"]


class Metadata(BaseModel):
    theme: str
    """Dashboard theme."""


class UserDataFetchResponse(BaseModel):
    id: str
    """User ID"""

    email: str
    """User Email"""

    name: str
    """Full name of user"""

    creation_date: int
    """User creation date. Milliseconds since epoch."""

    last_login_date: int
    """Last login date. Milliseconds since epoch."""

    last_login_ip: str
    """IP address of last login."""

    roles: List[str]
    """Roles assigned to the user."""

    timezone: str
    """Timezone selected by user."""

    metadata: Metadata
