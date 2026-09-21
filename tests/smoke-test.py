# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from gumlet import Gumlet

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Gumlet(max_retries=2, timeout=10)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    video_asset = client.video_assets.create(
        input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        collection_id="<your workspace id>",
        format="ABR",
        title="Example Title",
    )


def _smoke_case_1() -> None:
    video_asset = client.video_assets.create(
        input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        collection_id="<your workspace id>",
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
    )


def _smoke_case_2() -> None:
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
    )


def _smoke_case_3() -> None:
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
    )


def _smoke_case_4() -> None:
    video_asset = client.video_assets.retrieve_details(
        asset_id="assetId",
    )


def _smoke_case_5() -> None:
    client.video_assets.delete(
        asset_id="assetId",
    )


def _smoke_case_6() -> None:
    video_asset = client.video_assets.update(
        asset_id="<YOUR_ASSET_ID>",
        title="Updated Title",
    )


def _smoke_case_7() -> None:
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


def _smoke_case_8() -> None:
    video_asset = client.video_assets.thumbnail_select(
        asset_id="assetId",
        frame_at_second=2,
    )


def _smoke_case_9() -> None:
    video_asset = client.video_assets.thumbnail_upload(
        asset_id="assetId",
    )


def _smoke_case_10() -> None:
    video_asset = client.video_assets.create_update_chapter(
        asset_id="assetId",
        chapters=[{"label": "Chapter 1", "startTime": 0}, {"label": "Chapter 2", "startTime": 10}],
    )


def _smoke_case_11() -> None:
    video_asset = client.video_assets.list(
        workspace_id="workspaceId",
        type="all",
        offset=0,
        size=20,
        signed_token="false",
    )


def _smoke_case_12() -> None:
    video_asset = client.video_assets.list(
        workspace_id="workspaceId",
        type="all",
        parent_id="parent_id",
        title="title",
        status="status",
        tag="tag",
        playlist_id="playlist_id",
        start_date="start_date",
        end_date="end_date",
        min_duration=1,
        max_duration=1,
        sort_by="title",
        order_by="asc",
        search_index="search_index_for_asset_list",
        offset=0,
        size=20,
        signed_token="false",
    )


def _smoke_case_13() -> None:
    video_asset = client.video_assets.list_deprecated(
        workspace_id="workspaceId",
        sort_by="created_at",
        order_by="desc",
    )


def _smoke_case_14() -> None:
    video_asset = client.video_assets.list_deprecated(
        workspace_id="workspaceId",
        status="queued",
        tag="tag",
        title="title",
        folder="folder",
        offset="offset",
        size="size",
        playlist_id="playlist_id",
        sort_by="created_at",
        order_by="desc",
        type="type",
    )


def _smoke_case_15() -> None:
    video_asset = client.video_assets.delete_many(
        asset_list=["64249a8858fd3a208b987702", "64784bae843b155b829bbf84"],
        source_id="60bd2ba353ff754d28179ee6",
    )


def _smoke_case_16() -> None:
    video_asset = client.video_assets.tag_many(
        asset_list=["6221db301c8b821b0519fba0", "61e8f2726ec832ab2ac4fa6e"],
        source_id="60bd2ba353ff754d28179ee6",
        add_tags=["tag-1"],
        remove_tags=["playlist-1"],
    )


def _smoke_case_17() -> None:
    video_asset = client.video_assets.analytics(
        asset_id="assetId",
        group_by="daily",
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        metrics=["impressions"],
    )


def _smoke_case_18() -> None:
    video_asset = client.video_assets.analytics(
        asset_id="assetId",
        group_by="daily",
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        metrics=["impressions"],
        page_number=0,
        page_size=0,
    )


def _smoke_case_19() -> None:
    subtitle_upload = client.subtitle_upload.upload(
        asset_id="assetId",
        language_codes=["en"],
    )


def _smoke_case_20() -> None:
    subtitle_upload = client.subtitle_upload.complete(
        asset_id="assetId",
        upload_responses=[{"language_code": "en", "uploaded": True}],
    )


def _smoke_case_21() -> None:
    audio_upload = client.audio_upload.upload(
        asset_id="assetId",
        language_codes=["en"],
    )


def _smoke_case_22() -> None:
    audio_upload = client.audio_upload.complete(
        asset_id="assetId",
        upload_responses=[{"language_codes": ["en"], "uploaded": True}],
    )


def _smoke_case_23() -> None:
    video_usage_analytic = client.video_usage_analytics.retrieve(
        metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
        date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
        top_assets_count="5",
        top_assets_page="0",
        group_by="hourly",
    )


def _smoke_case_24() -> None:
    video_usage_analytic = client.video_usage_analytics.retrieve(
        metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
        date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
        filters={"collection_id": "", "source_id": ""},
        top_assets_count="5",
        top_assets_page="0",
        group_by="hourly",
    )


def _smoke_case_25() -> None:
    video_usage_analytic = client.video_usage_analytics.top_assets(
        start_at="2026-06-21",
        end_at="2026-06-30",
        page="1",
        page_size="1000",
    )


def _smoke_case_26() -> None:
    video_usage_analytic = client.video_usage_analytics.top_assets(
        start_at="2026-06-21",
        end_at="2026-06-30",
        collection_id="collection_id",
        page="1",
        page_size="1000",
    )


def _smoke_case_27() -> None:
    multipart_upload = client.multipart_upload.retrieve_part_url(
        asset_id="assetId",
        part_number="partNumber",
    )


def _smoke_case_28() -> None:
    multipart_upload = client.multipart_upload.complete(
        asset_id="assetId",
    )


def _smoke_case_29() -> None:
    multipart_upload = client.multipart_upload.complete(
        asset_id="assetId",
        parts=[{}],
    )


def _smoke_case_30() -> None:
    video_profile = client.video_profiles.create(
        name="Gumlet-Profile-1",
        format="ABR",
    )


def _smoke_case_31() -> None:
    video_profile = client.video_profiles.create(
        name="Gumlet-Profile-1",
        format="ABR",
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
        generate_subtitles={"transcribe": True, "subtitle_languages": ""},
        mp4_access=False,
        per_title_encoding=False,
        process_low_resolution_input=False,
        audio_only=False,
        enable_drm=False,
    )


def _smoke_case_32() -> None:
    video_profile = client.video_profiles.list()


def _smoke_case_33() -> None:
    video_profile = client.video_profiles.list(
        offset=1,
        size=1,
    )


def _smoke_case_34() -> None:
    video_profile = client.video_profiles.update(
        path_profile_id="profileId",
        body_profile_id="",
        format="ABR",
    )


def _smoke_case_35() -> None:
    video_profile = client.video_profiles.update(
        path_profile_id="profileId",
        body_profile_id="",
        name="",
        format="ABR",
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
        generate_subtitles={"subtitle_languages": [""], "transcribe": True},
        mp4_access=False,
        per_title_encoding=False,
        process_low_resolution_input=False,
        audio_only=False,
        enable_drm=False,
        vc=[""],
        generate_chapters=False,
        generate_description=False,
    )


def _smoke_case_36() -> None:
    video_profile = client.video_profiles.retrieve(
        profile_id="profileId",
    )


def _smoke_case_37() -> None:
    video_profile = client.video_profiles.delete(
        profile_id="profileId",
    )


def _smoke_case_38() -> None:
    video_playlist = client.video_playlists.create(
        collection_id="{{video-source-id}}",
        title="Playlist-Title",
        description="This is description for playlist.",
    )


def _smoke_case_39() -> None:
    video_playlist = client.video_playlists.list_all()


def _smoke_case_40() -> None:
    video_playlist = client.video_playlists.list_all(
        collection_id="collection_id",
    )


def _smoke_case_41() -> None:
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


def _smoke_case_42() -> None:
    video_playlist = client.video_playlists.delete_asset(
        playlist_id="playlistId",
        delete_list=["6508790783e4d606118467a3"],
    )


def _smoke_case_43() -> None:
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


def _smoke_case_44() -> None:
    client.video_playlists.delete(
        playlist_id="playlistId",
    )


def _smoke_case_45() -> None:
    video_playlist = client.video_playlists.list_assets(
        playlist_id="playlistId",
        sort_order=1,
        page_number=1,
        page_size="10",
    )


def _smoke_case_46() -> None:
    video_playlist = client.video_playlists.list_assets(
        playlist_id="playlistId",
        sort_by="sort_by",
        sort_order=1,
        page_number=1,
        page_size="10",
    )


def _smoke_case_47() -> None:
    video_playlist = client.video_playlists.reorder_asset(
        playlist_id="playlistId",
        asset_id="6e82bf783e88be000ab45ed2",
        page_number=1,
        page_size=10,
        asset_position=0,
    )


def _smoke_case_48() -> None:
    webhook = client.webhooks.create(
        url="",
        secret_token="",
        triggers=[""],
        sources=[""],
    )


def _smoke_case_49() -> None:
    webhook = client.webhooks.list()


def _smoke_case_50() -> None:
    webhook = client.webhooks.update(
        webhook_id="webhookId",
    )


def _smoke_case_51() -> None:
    webhook = client.webhooks.update(
        webhook_id="webhookId",
        url="",
        secret_token="",
        triggers="",
        sources="",
    )


def _smoke_case_52() -> None:
    webhook = client.webhooks.delete(
        webhook_id="webhookId",
    )


def _smoke_case_53() -> None:
    webhook = client.webhooks.history(
        webhook_id="webhookId",
    )


def _smoke_case_54() -> None:
    image_source = client.image_sources.create(
        namespace="google-demo",
        type="webfolder",
        webfolder={"base_url": "https://www.google.com"},
    )


def _smoke_case_55() -> None:
    image_source = client.image_sources.create(
        namespace="google-demo",
        type="webfolder",
        aws={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": "", "endpoint": ""},
        proxy={"whitelisted_domains": ""},
        gcs={"bucket_name": "", "service_account_key": ""},
        dostorage={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        wasabi={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        cloudinary={"host_name": "", "cloud_name": ""},
        azure={"azure_account_name": "", "azure_container_name": "", "azure_shared_token": "", "azure_path": ""},
        linode={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": ""},
        backblaze={
            "bucket_name": "",
            "bucket_region": "",
            "endpoint": "",
            "access_key": "",
            "secret": "",
            "base_path": "",
        },
        cloudflare={"bucket_name": "", "access_key": "", "account_id": "", "secret": "", "base_path": ""},
        webfolder={"base_url": "https://www.google.com"},
    )


def _smoke_case_56() -> None:
    image_source = client.image_sources.list(
        offset=0,
        size=20,
    )


def _smoke_case_57() -> None:
    image_source = client.image_sources.retrieve(
        image_source_id="imageSourceId",
    )


def _smoke_case_58() -> None:
    image_source = client.image_sources.update(
        image_source_id="imageSourceId",
        type="aws",
        aws={
            "bucket_name": "my-bucket-test",
            "bucket_region": "ap-southeast-1",
            "access_key": "BQUA6QFXVWHAAB6IO2X1",
            "secret": "aws_secret",
        },
    )


def _smoke_case_59() -> None:
    image_source = client.image_sources.update(
        image_source_id="imageSourceId",
        type="aws",
        webfolder={"base_url": ""},
        aws={
            "bucket_name": "my-bucket-test",
            "bucket_region": "ap-southeast-1",
            "access_key": "BQUA6QFXVWHAAB6IO2X1",
            "secret": "aws_secret",
        },
        proxy={"whitelisted_domains": ""},
        gcs={"bucket_name": "", "service_account_key": ""},
        dostorage={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        wasabi={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        linode={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": ""},
        backblaze={
            "bucket_name": "",
            "bucket_region": "",
            "endpoint": "",
            "access_key": "",
            "secret": "",
            "base_path": "",
        },
        cloudflare={"bucket_name": "", "access_key": "", "account_id": "", "secret": "", "base_path": ""},
        cloudinary={"host_name": "", "cloud_name": ""},
        azure={"azure_account_name": "", "azure_container_name": "", "azure_shared_token": "", "azure_path": ""},
        default_params={},
        error_image="",
        request_headers=[{}],
        response_headers=[{}],
        temp_cname=[""],
        browser_cache_time=0,
        cdn_cache_time=0,
        is_active=False,
        cname=[""],
        fallback_origins=[{"conditions": [""], "name": "", "type": "dostorage", "replace_operation": {}}],
    )


def _smoke_case_60() -> None:
    image_source = client.image_sources.delete(
        image_source_id="imageSourceId",
    )


def _smoke_case_61() -> None:
    image_source = client.image_sources.purge_cache(
        subdomain="subdomain",
        paths=["image.jpeg", "image2.png"],
    )


def _smoke_case_62() -> None:
    image_source = client.image_sources.purge(
        source_id="sourceId",
        paths=["image.jpeg", "image2.png"],
    )


def _smoke_case_63() -> None:
    image_usage_analytic = client.image_usage_analytics.retrieve(
        metrics=["bandwidth_consumption"],
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        group_by="daily",
    )


def _smoke_case_64() -> None:
    image_usage_analytic = client.image_usage_analytics.retrieve(
        metrics=["bandwidth_consumption"],
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        group_by="daily",
        filters={"source_id": ""},
    )


def _smoke_case_65() -> None:
    live_stream_asset = client.live_stream_assets.create(
        live_source_id="",
        resolution="",
    )


def _smoke_case_66() -> None:
    live_stream_asset = client.live_stream_assets.create(
        live_source_id="",
        resolution="",
        title="",
        mp4_access=False,
        orientation="landscape",
        start_at="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_67() -> None:
    live_stream_asset = client.live_stream_assets.update(
        live_asset_id="",
    )


def _smoke_case_68() -> None:
    live_stream_asset = client.live_stream_assets.update(
        live_asset_id="",
        title="",
        start_at="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_69() -> None:
    live_stream_asset = client.live_stream_assets.retrieve_status(
        live_asset_id="liveAssetId",
    )


def _smoke_case_70() -> None:
    live_stream_asset = client.live_stream_assets.delete(
        live_asset_id="liveAssetId",
    )


def _smoke_case_71() -> None:
    live_stream_asset = client.live_stream_assets.complete(
        live_asset_id="liveAssetId",
    )


def _smoke_case_72() -> None:
    live_stream_asset = client.live_stream_assets.filter(
        live_source_id="liveSourceId",
    )


def _smoke_case_73() -> None:
    live_stream_asset = client.live_stream_assets.filter(
        live_source_id="liveSourceId",
        status="status",
        offset=1,
        size=1,
    )


def _smoke_case_74() -> None:
    client.live_stream_assets.start(
        live_asset_id="liveAssetId",
    )


def _smoke_case_75() -> None:
    live_stream_asset = client.live_stream_assets.upload(
        live_asset_id="68c406b147f9ad0c0d584ce2",
        statuses="preparing",
    )


def _smoke_case_76() -> None:
    live_stream_asset = client.live_stream_assets.status_history(
        live_asset_id="liveAssetId",
    )


def _smoke_case_77() -> None:
    client.recycle_bin.recover(
        asset_id="",
    )


def _smoke_case_78() -> None:
    recycle_bin = client.recycle_bin.list(
        size=20,
        workspace_id="workspace_id",
    )


def _smoke_case_79() -> None:
    recycle_bin = client.recycle_bin.list(
        offset=1,
        size=20,
        workspace_id="workspace_id",
    )


def _smoke_case_80() -> None:
    video_workspace = client.video_workspaces.list(
        offset="0",
        size="10",
    )


def _smoke_case_81() -> None:
    video_workspace = client.video_workspaces.create(
        name="zoom-workspace",
        type="direct-upload",
        zoom={"secret": "yourSecret"},
    )


def _smoke_case_82() -> None:
    video_workspace = client.video_workspaces.create(
        name="zoom-workspace",
        type="direct-upload",
        default_profile_id="",
        insight_property_id="",
        video_protection={
            "signed_url": False,
            "signed_url_secret": "",
            "blacklisted_countries": [""],
            "whitelisted_referrers": "",
        },
        aws={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": "", "endpoint": ""},
        proxy={"whitelisted_domains": ""},
        gcs={"bucket_name": "", "service_account_key": ""},
        dostorage={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        wasabi={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        cloudinary={"host_name": "", "cloud_name": ""},
        azure={"azure_account_name": "", "azure_container_name": "", "azure_shared_token": "", "azure_path": ""},
        linode={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": ""},
        backblaze={
            "bucket_name": "",
            "bucket_region": "",
            "endpoint": "",
            "access_key": "",
            "secret": "",
            "base_path": "",
        },
        cloudflare={"bucket_name": "", "access_key": "", "account_id": "", "secret": "", "base_path": ""},
        zoom={"secret": "yourSecret"},
    )


def _smoke_case_83() -> None:
    video_workspace = client.video_workspaces.update(
        workspace_id="workspaceId",
        name="awsrename",
        default_profile_id="646df1c9173a4a2fcac180b7",
        type="aws",
        aws={
            "bucket_name": "my-bucket-test",
            "bucket_region": "ap-southeast-1",
            "access_key": "BQUA6QFXVWHAAB6IO2X1",
            "secret": "aws_secret",
        },
    )


def _smoke_case_84() -> None:
    video_workspace = client.video_workspaces.update(
        workspace_id="workspaceId",
        name="awsrename",
        default_profile_id="646df1c9173a4a2fcac180b7",
        temp_cname=[""],
        insight_property_id="",
        player_config={
            "preload": False,
            "autoplay": False,
            "disable_seek": False,
            "disable_player_controls": False,
            "powered_by_gumlet_overlay": False,
            "allow_drm_protected_videos": False,
            "loop": False,
            "player_color": "",
            "include_seo": False,
            "subtitle_enabled": False,
            "pixel_tags": {},
            "logo_width": 0,
            "logo_height": 0,
            "dynamic_watermark": False,
            "watermark_font_size": 0,
            "watermark_font_color": "",
            "watermark_bg_color": "",
            "watermark_interval": 0,
            "cast": False,
            "show_video_title": False,
        },
        video_protection={
            "signed_url": False,
            "signed_url_secret": "",
            "blacklisted_countries": [""],
            "whitelisted_referrers": [""],
        },
        channel_settings={
            "active": False,
            "description": "",
            "title": "",
            "privacy_type": '"public"',
            "featured_video": "",
            "password": "",
        },
        type="aws",
        webfolder={"base_url": ""},
        aws={
            "bucket_name": "my-bucket-test",
            "bucket_region": "ap-southeast-1",
            "access_key": "BQUA6QFXVWHAAB6IO2X1",
            "secret": "aws_secret",
        },
        proxy={"whitelisted_domains": ""},
        gcs={"bucket_name": "", "service_account_key": ""},
        dostorage={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        wasabi={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": "", "base_path": ""},
        linode={"bucket_name": "", "bucket_region": "", "access_key": "", "secret": ""},
        backblaze={
            "bucket_name": "",
            "bucket_region": "",
            "endpoint": "",
            "access_key": "",
            "secret": "",
            "base_path": "",
        },
        cloudflare={"bucket_name": "", "access_key": "", "account_id": "", "secret": "", "base_path": ""},
        cloudinary={"host_name": "", "cloud_name": ""},
        azure={"azure_account_name": "", "azure_container_name": "", "azure_shared_token": "", "azure_path": ""},
        zoom={"secret": ""},
    )


def _smoke_case_85() -> None:
    video_workspace = client.video_workspaces.retrieve(
        workspace_id="workspaceId",
    )


def _smoke_case_86() -> None:
    video_workspace = client.video_workspaces.delete(
        workspace_id="workspaceId",
    )


def _smoke_case_87() -> None:
    folder = client.folders.create(
        workspace_id="workspaceId",
        name="Course Assets",
        parent_id="",
    )


def _smoke_case_88() -> None:
    folder = client.folders.list(
        workspace_id="workspaceId",
    )


def _smoke_case_89() -> None:
    folder = client.folders.list(
        workspace_id="workspaceId",
        parent_id="parent_id",
    )


def _smoke_case_90() -> None:
    folder = client.folders.retrieve(
        workspace_id="workspaceId",
        folder_id="folderId",
    )


def _smoke_case_91() -> None:
    folder = client.folders.update(
        workspace_id="workspaceId",
        folder_id="folderId",
        name="Course Assets Updated",
    )


def _smoke_case_92() -> None:
    folder = client.folders.update(
        workspace_id="workspaceId",
        folder_id="folderId",
        name="Course Assets Updated",
        parent_id="",
        asset_ids=[""],
    )


def _smoke_case_93() -> None:
    folder = client.folders.delete(
        workspace_id="workspaceId",
        folder_id="folderId",
    )


def _smoke_case_94() -> None:
    folder = client.folders.delete_assets(
        workspace_id="workspaceId",
        asset_ids=["67e4f2b4403562dbea654301", "67e4f2bb403562dbea654302"],
    )


def _smoke_case_95() -> None:
    channel_viewer = client.channel_viewers.invite(
        video_workspace_id="videoWorkspaceId",
        users=[
            {"email": "test@gumlet.com", "name": "Test User-0"},
            {"email": "test+1@gumlet.com", "name": "Test User-1"},
            {"email": "test+2@gumlet.com", "name": "Test User-2"},
        ],
    )


def _smoke_case_96() -> None:
    channel_viewer = client.channel_viewers.delete(
        video_workspace_id="videoWorkspaceId",
        emails=["test@gumlet.com", "test+2@gumlet.com"],
    )


def _smoke_case_97() -> None:
    channel_viewer = client.channel_viewers.invite_csv(
        video_workspace_id="videoWorkspaceId",
        viewers_csv=b"viewers.csv",
    )


def _smoke_case_98() -> None:
    channel_viewer = client.channel_viewers.list_subscribers(
        workspace_id="workspaceId",
        page_number=1,
        page_size=10,
    )


def _smoke_case_99() -> None:
    video_analytic = client.video_analytics.chart_data(
        metrics=[""],
        workspace_id="",
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        group_by="daily",
    )


def _smoke_case_100() -> None:
    video_analytic = client.video_analytics.chart_data(
        metrics=[""],
        workspace_id="",
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        filters=[{"name": "meta_browser", "value": "", "operator": "equals"}],
        group_by="daily",
        chart_dimension={"group_by": [{}]},
    )


def _smoke_case_101() -> None:
    video_analytic = client.video_analytics.breakdown_data(
        date_range={"start_at": "2026-07-20", "end_at": "2026-08-20"},
        filters=[],
        breakdowns=[
            {"name": "custom_video_id", "metric": "views", "page": 1, "page_size": 10},
            {"name": "custom_video_title", "metric": "completion_percent_by_views", "page": 1, "page_size": 10},
        ],
        workspace_id="6694c405e63913eecf3cf5fb",
    )


def _smoke_case_102() -> None:
    video_analytic = client.video_analytics.aggregated_data(
        aggregate=[{"metric": "views", "function": "sum"}],
        workspace_id="",
        timeframe={},
    )


def _smoke_case_103() -> None:
    video_analytic = client.video_analytics.aggregated_data(
        aggregate=[{"metric": "views", "function": "sum"}],
        workspace_id="",
        timeframe={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        filters=[{"name": "meta_browser", "value": "", "operator": "equals"}],
    )


def _smoke_case_104() -> None:
    organization_data = client.organization_data.fetch_org()


def _smoke_case_105() -> None:
    user_data = client.user_data.fetch()


def _smoke_case_106() -> None:
    audit_log = client.audit_logs.fetch(
        date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
        page_number=1,
        page_size=100,
    )


def _smoke_case_107() -> None:
    audit_log = client.audit_logs.fetch(
        date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
        page_number=1,
        page_size=100,
        user_email=["user@example.com"],
        activity_type=["workspace_created"],
    )


def _smoke_case_108() -> None:
    billing = client.billing.list_invoices()


def _smoke_case_109() -> None:
    billing = client.billing.fetch_details()


def _smoke_case_110() -> None:
    billing = client.billing.update_details(
        address_line="",
        city="",
        company_name="",
        country_code="",
        gst_number="",
        postal="",
        state_code="",
    )


def _smoke_case_111() -> None:
    billing = client.billing.fetch_upcoming_invoice()


def _smoke_case_112() -> None:
    live_stream_workspace = client.live_stream_workspaces.list()


def _smoke_case_113() -> None:
    live_stream_workspace = client.live_stream_workspaces.create(
        name="",
    )


def _smoke_case_114() -> None:
    live_stream_workspace = client.live_stream_workspaces.update(
        live_workspace_id="liveWorkspaceId",
        name="live-stream-collections",
        video_source_id="67bea1d66ca0059a95bf7de9",
    )


def _smoke_case_115() -> None:
    live_stream_workspace = client.live_stream_workspaces.delete(
        live_workspace_id="liveWorkspaceId",
    )


def _smoke_case_116() -> None:
    live_stream_analytic = client.live_stream_analytics.usage(
        date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
        group_by="daily",
        metrics=["bandwidth_consumption"],
    )


def _smoke_case_117() -> None:
    global_search = client.global_search.search(
        search_query="search_query",
        size=20,
        assets_offset=0,
        folders_offset=0,
        playlists_offset=0,
        channels_offset=0,
    )


def _smoke_case_118() -> None:
    global_search = client.global_search.search(
        search_query="search_query",
        collection_id="collection_id",
        size=20,
        assets_offset=0,
        folders_offset=0,
        playlists_offset=0,
        channels_offset=0,
    )


cases: list[SmokeCase] = [
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/assets",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/assets",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "upload",
        "method": "POST",
        "path": "/video/assets/upload",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "upload",
        "method": "POST",
        "path": "/video/assets/upload",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "retrieveDetails",
        "method": "GET",
        "path": "/video/assets/{asset_id}",
        "run": _smoke_case_4,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/assets/{asset_id}",
        "run": _smoke_case_5,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/assets/update",
        "label": "required params",
        "run": _smoke_case_6,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/assets/update",
        "label": "all params",
        "run": _smoke_case_7,
    },
    {
        "operation": "thumbnailSelect",
        "method": "POST",
        "path": "/video/assets/{asset_id}/thumbnail-select",
        "run": _smoke_case_8,
    },
    {
        "operation": "thumbnailUpload",
        "method": "POST",
        "path": "/video/assets/{asset_ID}/thumbnail",
        "run": _smoke_case_9,
    },
    {
        "operation": "createUpdateChapter",
        "method": "POST",
        "path": "/video/assets/{asset_id}/chapters",
        "run": _smoke_case_10,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/workspaces/{workspace_id}/list",
        "label": "required params",
        "run": _smoke_case_11,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/workspaces/{workspace_id}/list",
        "label": "all params",
        "run": _smoke_case_12,
    },
    {
        "operation": "listDeprecated",
        "method": "GET",
        "path": "/video/assets/list/{workspace_id}",
        "label": "required params",
        "run": _smoke_case_13,
    },
    {
        "operation": "listDeprecated",
        "method": "GET",
        "path": "/video/assets/list/{workspace_id}",
        "label": "all params",
        "run": _smoke_case_14,
    },
    {
        "operation": "deleteMany",
        "method": "DELETE",
        "path": "/video/assets/bulk/delete",
        "run": _smoke_case_15,
    },
    {
        "operation": "tagMany",
        "method": "POST",
        "path": "/video/assets/bulk/tag",
        "run": _smoke_case_16,
    },
    {
        "operation": "analytics",
        "method": "POST",
        "path": "/video/assets/{asset_id}/analytics",
        "label": "required params",
        "run": _smoke_case_17,
    },
    {
        "operation": "analytics",
        "method": "POST",
        "path": "/video/assets/{asset_id}/analytics",
        "label": "all params",
        "run": _smoke_case_18,
    },
    {
        "operation": "upload",
        "method": "POST",
        "path": "/video/assets/{asset_ID}/subtitle/upload",
        "run": _smoke_case_19,
    },
    {
        "operation": "complete",
        "method": "POST",
        "path": "/video/assets/{asset_ID}/subtitle/upload/event",
        "run": _smoke_case_20,
    },
    {
        "operation": "upload",
        "method": "POST",
        "path": "/video/assets/{asset_ID}/audio/upload",
        "run": _smoke_case_21,
    },
    {
        "operation": "complete",
        "method": "POST",
        "path": "/video/assets/{asset_ID}/audio/upload/event",
        "run": _smoke_case_22,
    },
    {
        "operation": "retrieve",
        "method": "POST",
        "path": "/video/analytics",
        "label": "required params",
        "run": _smoke_case_23,
    },
    {
        "operation": "retrieve",
        "method": "POST",
        "path": "/video/analytics",
        "label": "all params",
        "run": _smoke_case_24,
    },
    {
        "operation": "topAssets",
        "method": "GET",
        "path": "/video/streaming-duration",
        "label": "required params",
        "run": _smoke_case_25,
    },
    {
        "operation": "topAssets",
        "method": "GET",
        "path": "/video/streaming-duration",
        "label": "all params",
        "run": _smoke_case_26,
    },
    {
        "operation": "retrievePartUrl",
        "method": "GET",
        "path": "/video/assets/{asset_id}/multipartupload/{part_number}/sign",
        "run": _smoke_case_27,
    },
    {
        "operation": "complete",
        "method": "POST",
        "path": "/video/assets/{asset_id}/multipartupload/complete",
        "label": "required params",
        "run": _smoke_case_28,
    },
    {
        "operation": "complete",
        "method": "POST",
        "path": "/video/assets/{asset_id}/multipartupload/complete",
        "label": "all params",
        "run": _smoke_case_29,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/profiles",
        "label": "required params",
        "run": _smoke_case_30,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/profiles",
        "label": "all params",
        "run": _smoke_case_31,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/profiles",
        "label": "required params",
        "run": _smoke_case_32,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/profiles",
        "label": "all params",
        "run": _smoke_case_33,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/profiles/{profile_id}",
        "label": "required params",
        "run": _smoke_case_34,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/profiles/{profile_id}",
        "label": "all params",
        "run": _smoke_case_35,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/video/profiles/{profile_id}",
        "run": _smoke_case_36,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/profiles/{profile_id}",
        "run": _smoke_case_37,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/playlist",
        "run": _smoke_case_38,
    },
    {
        "operation": "listAll",
        "method": "GET",
        "path": "/video/playlist",
        "label": "required params",
        "run": _smoke_case_39,
    },
    {
        "operation": "listAll",
        "method": "GET",
        "path": "/video/playlist",
        "label": "all params",
        "run": _smoke_case_40,
    },
    {
        "operation": "createAsset",
        "method": "POST",
        "path": "/video/playlist/{playlist_id}/asset",
        "run": _smoke_case_41,
    },
    {
        "operation": "deleteAsset",
        "method": "DELETE",
        "path": "/video/playlist/{playlist_id}/asset",
        "run": _smoke_case_42,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/playlist/{playlist_id}",
        "run": _smoke_case_43,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/playlist/{playlist_id}",
        "run": _smoke_case_44,
    },
    {
        "operation": "listAssets",
        "method": "GET",
        "path": "/video/playlist/{playlist_id}/assets",
        "label": "required params",
        "run": _smoke_case_45,
    },
    {
        "operation": "listAssets",
        "method": "GET",
        "path": "/video/playlist/{playlist_id}/assets",
        "label": "all params",
        "run": _smoke_case_46,
    },
    {
        "operation": "reorderAsset",
        "method": "POST",
        "path": "/video/playlists/{playlist_id}/reorder",
        "run": _smoke_case_47,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/org/webhooks",
        "run": _smoke_case_48,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/org/webhooks",
        "run": _smoke_case_49,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/org/webhooks/{webhook_id}",
        "label": "required params",
        "run": _smoke_case_50,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/org/webhooks/{webhook_id}",
        "label": "all params",
        "run": _smoke_case_51,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/org/webhooks/{webhook_id}",
        "run": _smoke_case_52,
    },
    {
        "operation": "history",
        "method": "GET",
        "path": "/org/webhook/{webhook_id}/history",
        "run": _smoke_case_53,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/image/sources",
        "label": "required params",
        "run": _smoke_case_54,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/image/sources",
        "label": "all params",
        "run": _smoke_case_55,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/image/sources",
        "run": _smoke_case_56,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/image/sources/{image_source_id}",
        "run": _smoke_case_57,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/image/sources/{image_source_id}",
        "label": "required params",
        "run": _smoke_case_58,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/image/sources/{image_source_id}",
        "label": "all params",
        "run": _smoke_case_59,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/image/sources/{image_source_id}",
        "run": _smoke_case_60,
    },
    {
        "operation": "purgeCache",
        "method": "POST",
        "path": "/purge/{subdomain}",
        "run": _smoke_case_61,
    },
    {
        "operation": "purge",
        "method": "POST",
        "path": "/image/purge/{source_id}",
        "run": _smoke_case_62,
    },
    {
        "operation": "retrieve",
        "method": "POST",
        "path": "/image/analytics",
        "label": "required params",
        "run": _smoke_case_63,
    },
    {
        "operation": "retrieve",
        "method": "POST",
        "path": "/image/analytics",
        "label": "all params",
        "run": _smoke_case_64,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/live/assets",
        "label": "required params",
        "run": _smoke_case_65,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/live/assets",
        "label": "all params",
        "run": _smoke_case_66,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/live/assets/update",
        "label": "required params",
        "run": _smoke_case_67,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/live/assets/update",
        "label": "all params",
        "run": _smoke_case_68,
    },
    {
        "operation": "retrieveStatus",
        "method": "GET",
        "path": "/video/live/assets/{live_asset_id}",
        "run": _smoke_case_69,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/live/assets/{live_asset_id}",
        "run": _smoke_case_70,
    },
    {
        "operation": "complete",
        "method": "POST",
        "path": "/video/live/assets/{live_asset_id}/complete",
        "run": _smoke_case_71,
    },
    {
        "operation": "filter",
        "method": "GET",
        "path": "/video/live/assets/list/{live_source_id}",
        "label": "required params",
        "run": _smoke_case_72,
    },
    {
        "operation": "filter",
        "method": "GET",
        "path": "/video/live/assets/list/{live_source_id}",
        "label": "all params",
        "run": _smoke_case_73,
    },
    {
        "operation": "start",
        "method": "POST",
        "path": "/video/live/assets/{live_asset_id}/start",
        "run": _smoke_case_74,
    },
    {
        "operation": "upload",
        "method": "POST",
        "path": "/video/live/assets/thumbnail/upload",
        "run": _smoke_case_75,
    },
    {
        "operation": "statusHistory",
        "method": "GET",
        "path": "/video/live/assets/{live_asset_id}/history",
        "run": _smoke_case_76,
    },
    {
        "operation": "recover",
        "method": "POST",
        "path": "/video/asset/recover",
        "run": _smoke_case_77,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/asset/recoverable/list",
        "label": "required params",
        "run": _smoke_case_78,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/asset/recoverable/list",
        "label": "all params",
        "run": _smoke_case_79,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/workspaces",
        "run": _smoke_case_80,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/workspaces",
        "label": "required params",
        "run": _smoke_case_81,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/workspaces",
        "label": "all params",
        "run": _smoke_case_82,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/workspaces/{workspace_id}",
        "label": "required params",
        "run": _smoke_case_83,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/workspaces/{workspace_id}",
        "label": "all params",
        "run": _smoke_case_84,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/video/workspaces/{workspace_id}",
        "run": _smoke_case_85,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/workspaces/{workspace_id}",
        "run": _smoke_case_86,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/workspaces/{workspace_id}/folders",
        "run": _smoke_case_87,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/workspaces/{workspace_id}/folders",
        "label": "required params",
        "run": _smoke_case_88,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/workspaces/{workspace_id}/folders",
        "label": "all params",
        "run": _smoke_case_89,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/video/workspaces/{workspace_id}/folders/{folder_id}",
        "run": _smoke_case_90,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/workspaces/{workspace_id}/folders/{folder_id}",
        "label": "required params",
        "run": _smoke_case_91,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/workspaces/{workspace_id}/folders/{folder_id}",
        "label": "all params",
        "run": _smoke_case_92,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/workspaces/{workspace_id}/folders/{folder_id}",
        "run": _smoke_case_93,
    },
    {
        "operation": "deleteAssets",
        "method": "POST",
        "path": "/video/workspaces/{workspace_id}/remove-assets-from-folder",
        "run": _smoke_case_94,
    },
    {
        "operation": "invite",
        "method": "POST",
        "path": "/channel/{video_workspace_id}/viewers/invite",
        "run": _smoke_case_95,
    },
    {
        "operation": "delete",
        "method": "POST",
        "path": "/channel/{video_workspace_id}/viewers/remove",
        "run": _smoke_case_96,
    },
    {
        "operation": "inviteCsv",
        "method": "POST",
        "path": "/channel/{video_workspace_id}/viewers/invite/csv",
        "run": _smoke_case_97,
    },
    {
        "operation": "listSubscribers",
        "method": "GET",
        "path": "/channel/{workspace_id}/viewers",
        "run": _smoke_case_98,
    },
    {
        "operation": "chartData",
        "method": "POST",
        "path": "/insights/viewer-analytics",
        "label": "required params",
        "run": _smoke_case_99,
    },
    {
        "operation": "chartData",
        "method": "POST",
        "path": "/insights/viewer-analytics",
        "label": "all params",
        "run": _smoke_case_100,
    },
    {
        "operation": "breakdownData",
        "method": "POST",
        "path": "/insights/breakdown-data",
        "run": _smoke_case_101,
    },
    {
        "operation": "aggregatedData",
        "method": "POST",
        "path": "/insights/aggregated-data",
        "label": "required params",
        "run": _smoke_case_102,
    },
    {
        "operation": "aggregatedData",
        "method": "POST",
        "path": "/insights/aggregated-data",
        "label": "all params",
        "run": _smoke_case_103,
    },
    {
        "operation": "fetchOrg",
        "method": "GET",
        "path": "/org/data",
        "run": _smoke_case_104,
    },
    {
        "operation": "fetch",
        "method": "GET",
        "path": "/user/data",
        "run": _smoke_case_105,
    },
    {
        "operation": "fetch",
        "method": "POST",
        "path": "/user/audit-log",
        "label": "required params",
        "run": _smoke_case_106,
    },
    {
        "operation": "fetch",
        "method": "POST",
        "path": "/user/audit-log",
        "label": "all params",
        "run": _smoke_case_107,
    },
    {
        "operation": "listInvoices",
        "method": "GET",
        "path": "/mixed/billing/invoice/history",
        "run": _smoke_case_108,
    },
    {
        "operation": "fetchDetails",
        "method": "GET",
        "path": "/mixed/billing/details",
        "run": _smoke_case_109,
    },
    {
        "operation": "updateDetails",
        "method": "POST",
        "path": "/mixed/billing/details",
        "run": _smoke_case_110,
    },
    {
        "operation": "fetchUpcomingInvoice",
        "method": "GET",
        "path": "/mixed/billing/invoice/upcoming",
        "run": _smoke_case_111,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/video/sources/live",
        "run": _smoke_case_112,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/video/sources/live",
        "run": _smoke_case_113,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/video/sources/live/{live_workspace_id}",
        "run": _smoke_case_114,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/video/sources/live/{live_workspace_id}",
        "run": _smoke_case_115,
    },
    {
        "operation": "usage",
        "method": "POST",
        "path": "/video/live/analytics",
        "run": _smoke_case_116,
    },
    {
        "operation": "search",
        "method": "GET",
        "path": "/entities/global-search",
        "label": "required params",
        "run": _smoke_case_117,
    },
    {
        "operation": "search",
        "method": "GET",
        "path": "/entities/global-search",
        "label": "all params",
        "run": _smoke_case_118,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
