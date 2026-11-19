# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestLiveStreamAssets:
    @smoke_case("liveStreamAssets.create:required", operation="create", path="/video/live/assets")
    def test_method_create(self) -> None:
        live_stream_asset = client.live_stream_assets.create(
            live_source_id="",
            resolution="",
        )

    @smoke_case("liveStreamAssets.create:all", operation="create", path="/video/live/assets")
    def test_method_create_with_all_params(self) -> None:
        live_stream_asset = client.live_stream_assets.create(
            live_source_id="",
            resolution="",
            title="",
            mp4_access=False,
            orientation="landscape",
            start_at="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("liveStreamAssets.update:required", operation="update", path="/video/live/assets/update")
    def test_method_update(self) -> None:
        live_stream_asset = client.live_stream_assets.update(
            live_asset_id="",
        )

    @smoke_case("liveStreamAssets.update:all", operation="update", path="/video/live/assets/update")
    def test_method_update_with_all_params(self) -> None:
        live_stream_asset = client.live_stream_assets.update(
            live_asset_id="",
            title="",
            start_at="2024-01-01T00:00:00.000Z",
        )

    @smoke_case(
        "liveStreamAssets.retrieveStatus:single", operation="retrieveStatus", path="/video/live/assets/{live_asset_id}"
    )
    def test_method_retrieve_status(self) -> None:
        live_stream_asset = client.live_stream_assets.retrieve_status(
            live_asset_id="liveAssetId",
        )

    @smoke_case("liveStreamAssets.delete:single", operation="delete", path="/video/live/assets/{live_asset_id}")
    def test_method_delete(self) -> None:
        live_stream_asset = client.live_stream_assets.delete(
            live_asset_id="liveAssetId",
        )

    @smoke_case(
        "liveStreamAssets.complete:single", operation="complete", path="/video/live/assets/{live_asset_id}/complete"
    )
    def test_method_complete(self) -> None:
        live_stream_asset = client.live_stream_assets.complete(
            live_asset_id="liveAssetId",
        )

    @smoke_case("liveStreamAssets.filter:required", operation="filter", path="/video/live/assets/list/{live_source_id}")
    def test_method_filter(self) -> None:
        page = client.live_stream_assets.filter(
            live_source_id="liveSourceId",
        )

    @smoke_case("liveStreamAssets.filter:all", operation="filter", path="/video/live/assets/list/{live_source_id}")
    def test_method_filter_with_all_params(self) -> None:
        page = client.live_stream_assets.filter(
            live_source_id="liveSourceId",
            status="status",
            next_page_token="next_page_token",
        )

    @smoke_case("liveStreamAssets.start:single", operation="start", path="/video/live/assets/{live_asset_id}/start")
    def test_method_start(self) -> None:
        client.live_stream_assets.start(
            live_asset_id="liveAssetId",
        )

    @smoke_case("liveStreamAssets.upload:single", operation="upload", path="/video/live/assets/thumbnail/upload")
    def test_method_upload(self) -> None:
        live_stream_asset = client.live_stream_assets.upload(
            live_asset_id="68c406b147f9ad0c0d584ce2",
            statuses="preparing",
        )

    @smoke_case(
        "liveStreamAssets.statusHistory:single",
        operation="statusHistory",
        path="/video/live/assets/{live_asset_id}/history",
    )
    def test_method_status_history(self) -> None:
        live_stream_asset = client.live_stream_assets.status_history(
            live_asset_id="liveAssetId",
        )
