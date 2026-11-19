# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVideoAssets:
    @smoke_case("videoAssets.create:required", operation="create", path="/video/assets")
    def test_method_create(self) -> None:
        video_asset = client.video_assets.create(
            input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
            format="ABR",
            title="Example Title",
            workspace_id="<your workspace id>",
        )

    @smoke_case("videoAssets.create:all", operation="create", path="/video/assets")
    def test_method_create_with_all_params(self) -> None:
        video_asset = client.video_assets.create(
            input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
            profile_id="",
            format="ABR",
            tag=[""],
            title="Example Title",
            description="",
            metadata={},
            width="",
            height="",
            resolution="",
            crop={"horizontal_margin": "", "vertical_margin": "", "width": "", "height": ""},
            pad={"top": "", "left": "", "bottom": "", "right": "", "color": ""},
            trim={"start_offset": 0, "end_offset": 0, "duration": 0},
            image_overlay={
                "url": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "horizontal_align": "",
                "vertical_align": "",
                "width": "",
                "height": "",
            },
            text_overlay={
                "text": "",
                "horizontal_align": "",
                "vertical_align": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "color": "",
                "font": "",
                "font_size": "",
                "opacity": "",
                "box": False,
                "box_color": "",
                "box_opacity": "",
                "box_border": "",
            },
            animated_gif={"start_offset": "", "end_offset": "", "width": "", "height": "", "fps": ""},
            additional_tracks=[{"url": "", "type": "", "language_code": ""}],
            generate_subtitles={"audio_language": "", "subtitle_languages": ""},
            mp4_access=False,
            per_title_encoding=False,
            process_low_resolution_input=False,
            audio_only=False,
            enable_drm=False,
            call_to_actions=[{}],
            playlist_id="",
            folder="",
            workspace_id="<your workspace id>",
        )

    @smoke_case("videoAssets.upload:required", operation="upload", path="/video/assets/upload")
    def test_method_upload(self) -> None:
        video_asset = client.video_assets.upload(
            collection_id="646df1c9173a4a2fcac180b4",
            profile_id="646df1c9173a4a2fcac180b7",
            format="ABR",
            tag=["ball"],
            description="some description",
            metadata={"headermeta": "metavalue"},
            call_to_actions=[
                {
                    "start_time": 1,
                    "end_time": 90,
                    "text": "some test",
                    "url": "https://some-url.com",
                    "position_from_top": 11,
                    "position_from_right": 23,
                    "border_radius": "11",
                    "font_color": "#000001",
                    "background_color": "#ffffff",
                }
            ],
            playlist_id="6597acd5ed6f26a9c5ca9633",
            folder="697375fbfa2d1037283140e4",
            workspace_id="646df1c9173a4a2fcac180b4",
        )

    @smoke_case("videoAssets.upload:all", operation="upload", path="/video/assets/upload")
    def test_method_upload_with_all_params(self) -> None:
        video_asset = client.video_assets.upload(
            collection_id="646df1c9173a4a2fcac180b4",
            profile_id="646df1c9173a4a2fcac180b7",
            format="ABR",
            tag=["ball"],
            title="",
            description="some description",
            metadata={"headermeta": "metavalue"},
            width="",
            height="",
            resolution="",
            crop={"horizontal_margin": "", "vertical_margin": "", "width": "", "height": ""},
            pad={"top": "", "left": "", "bottom": "", "right": "", "color": ""},
            trim={"start_offset": 0, "end_offset": 0, "duration": 0},
            image_overlay={
                "url": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "horizontal_align": "",
                "vertical_align": "",
                "width": "",
                "height": "",
            },
            text_overlay={
                "text": "",
                "horizontal_align": "",
                "vertical_align": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "color": "",
                "font": "",
                "font_size": "",
                "opacity": "",
                "box": False,
                "box_color": "",
                "box_opacity": "",
                "box_border": "",
            },
            animated_gif={"start_offset": "", "end_offset": "", "width": "", "height": "", "fps": ""},
            additional_tracks=[{"url": "", "type": "", "language_code": ""}],
            generate_subtitles={"audio_language": "", "subtitle_languages": ""},
            mp4_access=False,
            per_title_encoding=False,
            process_low_resolution_input=False,
            audio_only=False,
            enable_drm=False,
            call_to_actions=[
                {
                    "start_time": 1,
                    "end_time": 90,
                    "text": "some test",
                    "url": "https://some-url.com",
                    "position_from_top": 11,
                    "position_from_right": 23,
                    "border_radius": "11",
                    "font_color": "#000001",
                    "background_color": "#ffffff",
                }
            ],
            playlist_id="6597acd5ed6f26a9c5ca9633",
            folder="697375fbfa2d1037283140e4",
            workspace_id="646df1c9173a4a2fcac180b4",
        )

    @smoke_case("videoAssets.retrieveDetails:single", operation="retrieveDetails", path="/video/assets/{asset_id}")
    def test_method_retrieve_details(self) -> None:
        video_asset = client.video_assets.retrieve_details(
            asset_id="assetId",
        )

    @smoke_case("videoAssets.delete:single", operation="delete", path="/video/assets/{asset_id}")
    def test_method_delete(self) -> None:
        client.video_assets.delete(
            asset_id="assetId",
        )

    @smoke_case("videoAssets.update:required", operation="update", path="/video/assets/update")
    def test_method_update(self) -> None:
        video_asset = client.video_assets.update(
            asset_id="<YOUR_ASSET_ID>",
            title="Updated Title",
        )

    @smoke_case("videoAssets.update:all", operation="update", path="/video/assets/update")
    def test_method_update_with_all_params(self) -> None:
        video_asset = client.video_assets.update(
            asset_id="<YOUR_ASSET_ID>",
            title="Updated Title",
            description="",
            tag="",
            call_to_actions=[{}],
            metadata="",
            remove_subtitles=[""],
            input="",
            reprocess=False,
        )

    @smoke_case(
        "videoAssets.thumbnailSelect:single",
        operation="thumbnailSelect",
        path="/video/assets/{asset_id}/thumbnail-select",
    )
    def test_method_thumbnail_select(self) -> None:
        video_asset = client.video_assets.thumbnail_select(
            asset_id="assetId",
            frame_at_second=2,
        )

    @smoke_case(
        "videoAssets.thumbnailUpload:single", operation="thumbnailUpload", path="/video/assets/{asset_ID}/thumbnail"
    )
    def test_method_thumbnail_upload(self) -> None:
        video_asset = client.video_assets.thumbnail_upload(
            asset_id="assetId",
        )

    @smoke_case(
        "videoAssets.createUpdateChapter:single",
        operation="createUpdateChapter",
        path="/video/assets/{asset_id}/chapters",
    )
    def test_method_create_update_chapter(self) -> None:
        video_asset = client.video_assets.create_update_chapter(
            asset_id="assetId",
            chapters=[{"label": "Chapter 1", "startTime": 0}, {"label": "Chapter 2", "startTime": 10}],
        )

    @smoke_case(
        "videoAssets.listWorkspaceFoldersAndDeprecated:required",
        operation="listWorkspaceFoldersAndDeprecated",
        path="/video/workspaces/{workspace_id}/list",
    )
    def test_method_list_workspace_folders_and_deprecated(self) -> None:
        video_asset = client.video_assets.list_workspace_folders_and_deprecated(
            workspace_id="workspaceId",
            type="all",
            offset=0,
            size=20,
            signed_token="false",
        )

    @smoke_case(
        "videoAssets.listWorkspaceFoldersAndDeprecated:all",
        operation="listWorkspaceFoldersAndDeprecated",
        path="/video/workspaces/{workspace_id}/list",
    )
    def test_method_list_workspace_folders_and_deprecated_with_all_params(self) -> None:
        video_asset = client.video_assets.list_workspace_folders_and_deprecated(
            workspace_id="workspaceId",
            type="all",
            parent_id="parent_id",
            title="title",
            status="status",
            tag="tag",
            playlist_id="playlist_id",
            start_date="2024-01-01",
            end_date="2024-01-01",
            min_duration=1,
            max_duration=1,
            sort_by="title",
            order_by="asc",
            search_index="search_index_for_asset_list",
            offset=0,
            size=20,
            signed_token="false",
        )

    @smoke_case("videoAssets.list:required", operation="list", path="/video/assets/list/{workspace_id}")
    def test_method_list(self) -> None:
        video_asset = client.video_assets.list(
            workspace_id="workspaceId",
            sort_by="created_at",
            order_by="desc",
            signed_token="false",
            page_number=1,
            page_size=20,
        )

    @smoke_case("videoAssets.list:all", operation="list", path="/video/assets/list/{workspace_id}")
    def test_method_list_with_all_params(self) -> None:
        video_asset = client.video_assets.list(
            workspace_id="workspaceId",
            status="status",
            tag="tag",
            title="title",
            folder_id="folder_id",
            playlist_id="playlist_id",
            start_date="2024-01-01",
            end_date="2024-01-01",
            min_duration=1,
            max_duration=1,
            sort_by="created_at",
            order_by="desc",
            signed_token="false",
            page_number=1,
            page_size=20,
            next_page_token="next_page_token",
        )

    @smoke_case("videoAssets.deleteMany:single", operation="deleteMany", path="/video/assets/bulk/delete")
    def test_method_delete_many(self) -> None:
        video_asset = client.video_assets.delete_many(
            asset_list=["64249a8858fd3a208b987702", "64784bae843b155b829bbf84"],
            source_id="60bd2ba353ff754d28179ee6",
            workspace_id="60bd2ba353ff754d28179ee6",
        )

    @smoke_case("videoAssets.tagMany:single", operation="tagMany", path="/video/assets/bulk/tag")
    def test_method_tag_many(self) -> None:
        video_asset = client.video_assets.tag_many(
            asset_list=["6221db301c8b821b0519fba0", "61e8f2726ec832ab2ac4fa6e"],
            source_id="60bd2ba353ff754d28179ee6",
            add_tags=["tag-1"],
            remove_tags=["playlist-1"],
            workspace_id="60bd2ba353ff754d28179ee6",
        )

    @smoke_case("videoAssets.analytics:required", operation="analytics", path="/video/assets/{asset_id}/analytics")
    def test_method_analytics(self) -> None:
        video_asset = client.video_assets.analytics(
            asset_id="assetId",
            group_by="daily",
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            metrics=["impressions"],
        )

    @smoke_case("videoAssets.analytics:all", operation="analytics", path="/video/assets/{asset_id}/analytics")
    def test_method_analytics_with_all_params(self) -> None:
        video_asset = client.video_assets.analytics(
            asset_id="assetId",
            group_by="daily",
            date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
            metrics=["impressions"],
            page_number=0,
            page_size=0,
        )
