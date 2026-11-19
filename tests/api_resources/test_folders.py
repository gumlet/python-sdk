# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestFolders:
    @smoke_case("folders.create:single", operation="create", path="/video/workspaces/{workspace_id}/folders")
    def test_method_create(self) -> None:
        folder = client.folders.create(
            workspace_id="workspaceId",
            name="Course Assets",
            parent_id="",
        )

    @smoke_case("folders.list:required", operation="list", path="/video/workspaces/{workspace_id}/folders")
    def test_method_list(self) -> None:
        folder = client.folders.list(
            workspace_id="workspaceId",
        )

    @smoke_case("folders.list:all", operation="list", path="/video/workspaces/{workspace_id}/folders")
    def test_method_list_with_all_params(self) -> None:
        folder = client.folders.list(
            workspace_id="workspaceId",
            parent_id="parent_id",
        )

    @smoke_case(
        "folders.retrieve:single", operation="retrieve", path="/video/workspaces/{workspace_id}/folders/{folder_id}"
    )
    def test_method_retrieve(self) -> None:
        folder = client.folders.retrieve(
            workspace_id="workspaceId",
            folder_id="folderId",
        )

    @smoke_case(
        "folders.update:required", operation="update", path="/video/workspaces/{workspace_id}/folders/{folder_id}"
    )
    def test_method_update(self) -> None:
        folder = client.folders.update(
            workspace_id="workspaceId",
            folder_id="folderId",
            name="Course Assets Updated",
        )

    @smoke_case("folders.update:all", operation="update", path="/video/workspaces/{workspace_id}/folders/{folder_id}")
    def test_method_update_with_all_params(self) -> None:
        folder = client.folders.update(
            workspace_id="workspaceId",
            folder_id="folderId",
            name="Course Assets Updated",
            parent_id="",
            asset_ids=[""],
        )

    @smoke_case(
        "folders.delete:single", operation="delete", path="/video/workspaces/{workspace_id}/folders/{folder_id}"
    )
    def test_method_delete(self) -> None:
        folder = client.folders.delete(
            workspace_id="workspaceId",
            folder_id="folderId",
        )

    @smoke_case(
        "folders.removeAssets:single",
        operation="removeAssets",
        path="/video/workspaces/{workspace_id}/remove-assets-from-folder",
    )
    def test_method_remove_assets(self) -> None:
        folder = client.folders.remove_assets(
            workspace_id="workspaceId",
            asset_ids=["67e4f2b4403562dbea654301", "67e4f2bb403562dbea654302"],
        )
