# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebhookUpdateResponse"]


class WebhookUpdateResponse(BaseModel):
    id: Optional[str] = None

    url: Optional[str] = None

    triggers: Optional[List[str]] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    sources: Optional[List[str]] = None

    secret_token: Optional[str] = None
