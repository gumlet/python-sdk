# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    url: str
    """URL from the application you want to send data to."""

    secret_token: str
    """Authentication token to ensure legitimacy of Gumlet Webhook request on your application."""

    triggers: str
    """Triggers for the invocation of webhookos, supported option is `status`."""

    sources: str
    """List of video collection identifiers for which webhooks are needed to be invoked."""
