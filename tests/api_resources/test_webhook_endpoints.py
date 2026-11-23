# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestWebhookEndpoints:
    @smoke_case("webhookEndpoints.create:single", operation="create", path="/org/webhooks")
    def test_method_create(self) -> None:
        webhook_endpoint = client.webhook_endpoints.create(
            url="",
            secret_token="",
            triggers=["status"],
            sources=[""],
            idempotency_key="",
        )

    @smoke_case("webhookEndpoints.list:single", operation="list", path="/org/webhooks")
    def test_method_list(self) -> None:
        webhook_endpoint = client.webhook_endpoints.list()

    @smoke_case("webhookEndpoints.update:required", operation="update", path="/org/webhooks/{webhook_id}")
    def test_method_update(self) -> None:
        webhook_endpoint = client.webhook_endpoints.update(
            webhook_id="webhookId",
            idempotency_key="",
        )

    @smoke_case("webhookEndpoints.update:all", operation="update", path="/org/webhooks/{webhook_id}")
    def test_method_update_with_all_params(self) -> None:
        webhook_endpoint = client.webhook_endpoints.update(
            webhook_id="webhookId",
            url="",
            secret_token="",
            triggers=["status"],
            sources=[""],
            idempotency_key="",
        )

    @smoke_case("webhookEndpoints.delete:single", operation="delete", path="/org/webhooks/{webhook_id}")
    def test_method_delete(self) -> None:
        webhook_endpoint = client.webhook_endpoints.delete(
            webhook_id="webhookId",
            idempotency_key="",
        )

    @smoke_case("webhookEndpoints.history:required", operation="history", path="/org/webhook/{webhook_id}/history")
    def test_method_history(self) -> None:
        webhook_endpoint = client.webhook_endpoints.history(
            webhook_id="webhookId",
            page_number=1,
            page_size=20,
        )

    @smoke_case("webhookEndpoints.history:all", operation="history", path="/org/webhook/{webhook_id}/history")
    def test_method_history_with_all_params(self) -> None:
        webhook_endpoint = client.webhook_endpoints.history(
            webhook_id="webhookId",
            page_number=1,
            page_size=20,
            next_page_token="next_page_token",
        )
