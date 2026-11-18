# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVideoUsageAnalytics:
    @smoke_case("videoUsageAnalytics.retrieve:required", operation="retrieve", path="/video/analytics")
    def test_method_retrieve(self) -> None:
        video_usage_analytic = client.video_usage_analytics.retrieve(
            metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
            date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
            top_assets_count="5",
            top_assets_page="0",
            group_by="hourly",
        )

    @smoke_case("videoUsageAnalytics.retrieve:all", operation="retrieve", path="/video/analytics")
    def test_method_retrieve_with_all_params(self) -> None:
        video_usage_analytic = client.video_usage_analytics.retrieve(
            metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
            date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
            filters={"collection_id": "", "source_id": "", "workspace_id": "646df1c9173a4a2fcac180b4"},
            top_assets_count="5",
            top_assets_page="0",
            group_by="hourly",
        )

    @smoke_case("videoUsageAnalytics.topAssets:required", operation="topAssets", path="/video/streaming-duration")
    def test_method_top_assets(self) -> None:
        video_usage_analytic = client.video_usage_analytics.top_assets(
            start_at="2026-06-21",
            end_at="2026-06-30",
            page="1",
            page_size="1000",
        )

    @smoke_case("videoUsageAnalytics.topAssets:all", operation="topAssets", path="/video/streaming-duration")
    def test_method_top_assets_with_all_params(self) -> None:
        video_usage_analytic = client.video_usage_analytics.top_assets(
            start_at="2026-06-21",
            end_at="2026-06-30",
            workspace_id="workspace_id",
            collection_id="collection_id",
            page="1",
            page_size="1000",
        )
