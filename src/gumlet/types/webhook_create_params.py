# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """URL from the application you want to send data to."""

    secret_token: Required[str]
    """Authentication token to ensure legitimacy of Gumlet Webhook request on your application."""

    triggers: Required[SequenceNotStr[str]]
    """Triggers for the invocation of webhookos, supported option is `status`."""

    sources: Required[SequenceNotStr[str]]
    """List of video collection identifiers for which webhooks are needed to be invoked."""
