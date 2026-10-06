# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    id: Optional[str] = None
    """Webhook ID"""

    url: Optional[str] = None
    """Webhook URL"""

    triggers: Optional[List[str]] = None
    """List of triggers"""

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    sources: Optional[List[str]] = None

    secret_token: Optional[str] = None
