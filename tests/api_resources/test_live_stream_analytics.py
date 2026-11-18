# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestLiveStreamAnalytics:
    @smoke_case("liveStreamAnalytics.usage:single", operation="usage", path="/video/live/analytics")
    def test_method_usage(self) -> None:
        live_stream_analytic = client.live_stream_analytics.usage(
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            group_by="daily",
            metrics=["bandwidth_consumption"],
        )
