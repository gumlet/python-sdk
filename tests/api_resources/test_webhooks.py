# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestWebhooks:
    @smoke_case("webhooks.retrieve:single", operation="retrieve", path="/org/webhooks/{webhook_id}")
    def test_method_retrieve(self) -> None:
        webhook = client.webhooks.retrieve(
            webhook_id="webhookId",
        )
