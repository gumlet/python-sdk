# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVideoPlaylists:
    @smoke_case("videoPlaylists.create:single", operation="create", path="/video/playlist")
    def test_method_create(self) -> None:
        video_playlist = client.video_playlists.create(
            collection_id="{{video-source-id}}",
            title="Playlist-Title",
            description="This is description for playlist.",
            workspace_id="{{video-source-id}}",
        )

    @smoke_case("videoPlaylists.listAll:required", operation="listAll", path="/video/playlist")
    def test_method_list_all(self) -> None:
        video_playlist = client.video_playlists.list_all()

    @smoke_case("videoPlaylists.listAll:all", operation="listAll", path="/video/playlist")
    def test_method_list_all_with_all_params(self) -> None:
        video_playlist = client.video_playlists.list_all(
            workspace_id="workspace_id",
            collection_id="collection_id",
        )

    @smoke_case(
        "videoPlaylists.createAsset:single", operation="createAsset", path="/video/playlist/{playlist_id}/asset"
    )
    def test_method_create_asset(self) -> None:
        video_playlist = client.video_playlists.create_asset(
            playlist_id="playlistId",
            asset_list=[
                {"asset_id": "6508790283e4d60611846790"},
                {"position": 1, "asset_id": "650878f883e4d6061184677d"},
                {"asset_id": "650878de83e4d6061184676a"},
                {"position": 2, "asset_id": "650878d883e4d60611846757"},
                {"position": 3, "asset_id": "65578dd87eebc22dcdd549a2"},
            ],
        )

    @smoke_case(
        "videoPlaylists.deleteAsset:single", operation="deleteAsset", path="/video/playlist/{playlist_id}/asset"
    )
    def test_method_delete_asset(self) -> None:
        video_playlist = client.video_playlists.delete_asset(
            playlist_id="playlistId",
            delete_list=["6508790783e4d606118467a3"],
        )

    @smoke_case("videoPlaylists.update:single", operation="update", path="/video/playlist/{playlist_id}")
    def test_method_update(self) -> None:
        video_playlist = client.video_playlists.update(
            playlist_id="playlistId",
            title="Playlist-Title-Updated",
            description="This is updated description",
            position=6,
            player_config={
                "preload": True,
                "autoplay": False,
                "disable_seek": True,
                "disable_player_controls": False,
                "powered_by_gumlet_overlay": False,
                "allow_drm_protected_videos": False,
                "loop": False,
                "player_color": "#6658ea",
                "include_seo": True,
                "subtitle_enabled": True,
                "pixel_tags": {},
                "logo_width": 51,
                "logo_height": 100,
                "dynamic_watermark": False,
                "watermark_font_size": 1,
                "watermark_font_color": "#ff0000",
                "watermark_bg_color": "transparent",
                "watermark_interval": 1000,
            },
            channel_visibility=False,
        )

    @smoke_case("videoPlaylists.delete:single", operation="delete", path="/video/playlist/{playlist_id}")
    def test_method_delete(self) -> None:
        client.video_playlists.delete(
            playlist_id="playlistId",
        )

    @smoke_case(
        "videoPlaylists.listAssets:required", operation="listAssets", path="/video/playlist/{playlist_id}/assets"
    )
    def test_method_list_assets(self) -> None:
        video_playlist = client.video_playlists.list_assets(
            playlist_id="playlistId",
            sort_order=1,
            page_number=1,
            page_size="10",
        )

    @smoke_case("videoPlaylists.listAssets:all", operation="listAssets", path="/video/playlist/{playlist_id}/assets")
    def test_method_list_assets_with_all_params(self) -> None:
        video_playlist = client.video_playlists.list_assets(
            playlist_id="playlistId",
            sort_by="sort_by",
            sort_order=1,
            page_number=1,
            page_size="10",
        )

    @smoke_case(
        "videoPlaylists.reorderAsset:single", operation="reorderAsset", path="/video/playlists/{playlist_id}/reorder"
    )
    def test_method_reorder_asset(self) -> None:
        video_playlist = client.video_playlists.reorder_asset(
            playlist_id="playlistId",
            asset_id="6e82bf783e88be000ab45ed2",
            page_number=1,
            page_size=10,
            asset_position=0,
        )
