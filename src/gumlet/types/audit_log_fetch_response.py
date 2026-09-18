# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["AuditLogFetchResponse", "Pagination", "Data", "DataSource"]


class DataSource(BaseModel):
    id: str
    """ID of the resource."""

    type: str
    """What kind of ID is there? For example, if the activity happened on a video workspace, the type would be `workspace`"""


class Data(BaseModel):
    activity: str
    """User friendly name of the activity"""

    ip: str
    """IP address from where the activity happened."""

    action_user: str
    """Email id of the user who performed the activity."""

    status_code: int
    """API status code for the event"""

    response_time: float
    """Total response time in milliseconds for the event."""

    timestamp: float
    """Milliseconds since epoch marking the exact timestamp for the activity."""

    source: DataSource
    """Details about affected resource"""


class Pagination(BaseModel):
    page: int
    """Current page."""

    page_size: int
    """Items returned in current page"""

    total_pages: int
    """Total available pages."""

    total: int
    """Total available audit log items."""


class AuditLogFetchResponse(BaseModel):
    pagination: Pagination
    """Details about pagination of the audit logs."""

    data: List[Data]
