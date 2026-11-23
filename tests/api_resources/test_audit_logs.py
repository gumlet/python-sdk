# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAuditLogs:
    @smoke_case("auditLogs.fetch:required", operation="fetch", path="/user/audit-log")
    def test_method_fetch(self) -> None:
        audit_log = client.audit_logs.fetch(
            date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
            page_number=1,
            page_size=100,
            idempotency_key="",
        )

    @smoke_case("auditLogs.fetch:all", operation="fetch", path="/user/audit-log")
    def test_method_fetch_with_all_params(self) -> None:
        audit_log = client.audit_logs.fetch(
            date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
            page_number=1,
            page_size=100,
            user_email=["user@example.com"],
            activity_type=["workspace_created"],
            idempotency_key="",
        )
