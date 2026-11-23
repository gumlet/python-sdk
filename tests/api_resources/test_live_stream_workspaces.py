# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestLiveStreamWorkspaces:
    @smoke_case("liveStreamWorkspaces.list:single", operation="list", path="/video/sources/live")
    def test_method_list(self) -> None:
        live_stream_workspace = client.live_stream_workspaces.list()

    @smoke_case("liveStreamWorkspaces.create:single", operation="create", path="/video/sources/live")
    def test_method_create(self) -> None:
        live_stream_workspace = client.live_stream_workspaces.create(
            name="",
            idempotency_key="",
        )

    @smoke_case(
        "liveStreamWorkspaces.update:single", operation="update", path="/video/sources/live/{live_workspace_id}"
    )
    def test_method_update(self) -> None:
        live_stream_workspace = client.live_stream_workspaces.update(
            live_workspace_id="liveWorkspaceId",
            name="live-stream-collections",
            video_source_id="67bea1d66ca0059a95bf7de9",
            idempotency_key="",
        )

    @smoke_case(
        "liveStreamWorkspaces.delete:single", operation="delete", path="/video/sources/live/{live_workspace_id}"
    )
    def test_method_delete(self) -> None:
        live_stream_workspace = client.live_stream_workspaces.delete(
            live_workspace_id="liveWorkspaceId",
            idempotency_key="",
        )
