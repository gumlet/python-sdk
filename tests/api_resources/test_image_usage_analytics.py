# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestImageUsageAnalytics:
    @smoke_case("imageUsageAnalytics.retrieve:required", operation="retrieve", path="/image/analytics")
    def test_method_retrieve(self) -> None:
        image_usage_analytic = client.image_usage_analytics.retrieve(
            metrics=["bandwidth_consumption"],
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            group_by="daily",
        )

    @smoke_case("imageUsageAnalytics.retrieve:all", operation="retrieve", path="/image/analytics")
    def test_method_retrieve_with_all_params(self) -> None:
        image_usage_analytic = client.image_usage_analytics.retrieve(
            metrics=["bandwidth_consumption"],
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            group_by="daily",
            filters={"source_id": ""},
        )
