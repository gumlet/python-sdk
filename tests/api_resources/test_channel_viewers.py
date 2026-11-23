# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestChannelViewers:
    @smoke_case("channelViewers.invite:single", operation="invite", path="/channel/{video_workspace_id}/viewers/invite")
    def test_method_invite(self) -> None:
        channel_viewer = client.channel_viewers.invite(
            video_workspace_id="videoWorkspaceId",
            users=[
                {"email": "test@gumlet.com", "name": "Test User-0"},
                {"email": "test+1@gumlet.com", "name": "Test User-1"},
                {"email": "test+2@gumlet.com", "name": "Test User-2"},
            ],
            idempotency_key="",
        )

    @smoke_case("channelViewers.remove:single", operation="remove", path="/channel/{video_workspace_id}/viewers/remove")
    def test_method_remove(self) -> None:
        channel_viewer = client.channel_viewers.remove(
            video_workspace_id="videoWorkspaceId",
            emails=["test@gumlet.com", "test+2@gumlet.com"],
            idempotency_key="",
        )

    @smoke_case(
        "channelViewers.inviteCsv:single",
        operation="inviteCsv",
        path="/channel/{video_workspace_id}/viewers/invite/csv",
    )
    def test_method_invite_csv(self) -> None:
        channel_viewer = client.channel_viewers.invite_csv(
            video_workspace_id="videoWorkspaceId",
            viewers_csv=b"viewers.csv",
            idempotency_key="",
        )

    @smoke_case(
        "channelViewers.listSubscribers:required", operation="listSubscribers", path="/channel/{workspace_id}/viewers"
    )
    def test_method_list_subscribers(self) -> None:
        channel_viewer = client.channel_viewers.list_subscribers(
            workspace_id="workspaceId",
            page_number=1,
            page_size=20,
        )

    @smoke_case(
        "channelViewers.listSubscribers:all", operation="listSubscribers", path="/channel/{workspace_id}/viewers"
    )
    def test_method_list_subscribers_with_all_params(self) -> None:
        channel_viewer = client.channel_viewers.list_subscribers(
            workspace_id="workspaceId",
            page_number=1,
            page_size=20,
            next_page_token="next_page_token",
        )
