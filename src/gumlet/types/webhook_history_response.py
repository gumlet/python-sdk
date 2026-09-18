# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WebhookHistoryResponse", "WebhookHistoryResponseItem"]


class WebhookHistoryResponseItem(BaseModel):
    id: str
    """Webhook event ID"""

    status: str
    """Status of webhook event"""

    retry_count: int
    """Number of retries it needed to deliver webhook."""

    event: str
    """Name of the webhook event"""

    asset_id: str
    """Asset ID for which the event was fired"""

    created_at: str
    """Event timestamp in ISO 8601 format"""


WebhookHistoryResponse: TypeAlias = List[WebhookHistoryResponseItem]
