# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    id: str
    """Webhook ID"""

    url: str
    """Webhook URL"""

    triggers: List[str]
    """List of triggers configured for this webhook"""

    created_at: str
    """Creation timestamp in ISO 8601 format"""

    updated_at: str
    """Update timestamp in ISO 8601 format"""

    sources: List[str]
    """List of workspace IDs for which the webhook is enabled."""

    secret_token: Optional[str] = None
    """The token which you must validate when you receive the webhook. It's given by you when you create the webhook."""
