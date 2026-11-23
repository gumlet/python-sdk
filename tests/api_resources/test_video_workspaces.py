# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVideoWorkspaces:
    @smoke_case("videoWorkspaces.list:required", operation="list", path="/video/workspaces")
    def test_method_list(self) -> None:
        video_workspace = client.video_workspaces.list(
            page_number=1,
            page_size=20,
        )

    @smoke_case("videoWorkspaces.list:all", operation="list", path="/video/workspaces")
    def test_method_list_with_all_params(self) -> None:
        video_workspace = client.video_workspaces.list(
            page_number=1,
            page_size=20,
            next_page_token="next_page_token",
        )

    @smoke_case("videoWorkspaces.create:required", operation="create", path="/video/workspaces")
    def test_method_create(self) -> None:
        video_workspace = client.video_workspaces.create(
            name="My Workspace",
            type="direct-upload",
            data_localization="us",
            idempotency_key="",
        )

    @smoke_case("videoWorkspaces.create:all", operation="create", path="/video/workspaces")
    def test_method_create_with_all_params(self) -> None:
        video_workspace = client.video_workspaces.create(
            name="My Workspace",
            type="direct-upload",
            default_profile_id="",
            insight_property_id="",
            video_protection={
                "signed_url": False,
                "signed_url_secret": "",
                "blacklisted_countries": [""],
                "whitelisted_referrers": "",
            },
            aws={
                "bucket_name": "",
                "bucket_region": "",
                "access_key": "",
                "secret": "",
                "base_path": "",
                "endpoint": "",
            },
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
            zoom={"secret": ""},
            data_localization="us",
            idempotency_key="",
        )

    @smoke_case("videoWorkspaces.update:required", operation="update", path="/video/workspaces/{workspace_id}")
    def test_method_update(self) -> None:
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
            idempotency_key="",
        )

    @smoke_case("videoWorkspaces.update:all", operation="update", path="/video/workspaces/{workspace_id}")
    def test_method_update_with_all_params(self) -> None:
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
            idempotency_key="",
        )

    @smoke_case("videoWorkspaces.retrieve:single", operation="retrieve", path="/video/workspaces/{workspace_id}")
    def test_method_retrieve(self) -> None:
        video_workspace = client.video_workspaces.retrieve(
            workspace_id="workspaceId",
        )

    @smoke_case("videoWorkspaces.delete:single", operation="delete", path="/video/workspaces/{workspace_id}")
    def test_method_delete(self) -> None:
        video_workspace = client.video_workspaces.delete(
            workspace_id="workspaceId",
            idempotency_key="",
        )
