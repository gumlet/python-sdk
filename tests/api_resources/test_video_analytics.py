# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVideoAnalytics:
    @smoke_case("videoAnalytics.viewerData:required", operation="viewerData", path="/insights/viewer-analytics")
    def test_method_viewer_data(self) -> None:
        video_analytic = client.video_analytics.viewer_data(
            metrics=["views"],
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            group_by="daily",
        )

    @smoke_case("videoAnalytics.viewerData:all", operation="viewerData", path="/insights/viewer-analytics")
    def test_method_viewer_data_with_all_params(self) -> None:
        video_analytic = client.video_analytics.viewer_data(
            metrics=["views"],
            workspace_id="",
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            filters=[{"name": "meta_browser", "value": "", "operator": "equals"}],
            group_by="daily",
            chart_dimension={"group_by": [{}]},
            download=False,
        )

    @smoke_case("videoAnalytics.breakdownData:single", operation="breakdownData", path="/insights/breakdown-data")
    def test_method_breakdown_data(self) -> None:
        video_analytic = client.video_analytics.breakdown_data(
            date_range={"start_at": "2026-07-20", "end_at": "2026-08-20"},
            filters=[],
            breakdowns=[
                {"name": "custom_video_id", "metric": "views", "page": 1, "page_size": 10},
                {"name": "custom_video_title", "metric": "completion_percent_by_views", "page": 1, "page_size": 10},
            ],
            workspace_id="6694c405e63913eecf3cf5fb",
        )

    @smoke_case("videoAnalytics.aggregatedData:required", operation="aggregatedData", path="/insights/aggregated-data")
    def test_method_aggregated_data(self) -> None:
        video_analytic = client.video_analytics.aggregated_data(
            aggregate=[{"metric": "views", "function": "sum"}],
            workspace_id="",
            timeframe={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        )

    @smoke_case("videoAnalytics.aggregatedData:all", operation="aggregatedData", path="/insights/aggregated-data")
    def test_method_aggregated_data_with_all_params(self) -> None:
        video_analytic = client.video_analytics.aggregated_data(
            aggregate=[{"metric": "views", "function": "sum"}],
            workspace_id="",
            timeframe={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            filters=[{"name": "meta_browser", "value": "", "operator": "equals"}],
        )
