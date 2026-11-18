# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestImageSources:
    @smoke_case("imageSources.create:required", operation="create", path="/image/sources")
    def test_method_create(self) -> None:
        image_source = client.image_sources.create(
            namespace="google-demo",
            type="webfolder",
            webfolder={"base_url": "https://www.google.com"},
        )

    @smoke_case("imageSources.create:all", operation="create", path="/image/sources")
    def test_method_create_with_all_params(self) -> None:
        image_source = client.image_sources.create(
            namespace="google-demo",
            type="webfolder",
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
            webfolder={"base_url": "https://www.google.com"},
        )

    @smoke_case("imageSources.list:required", operation="list", path="/image/sources")
    def test_method_list(self) -> None:
        image_source = client.image_sources.list(
            page_number=1,
            page_size=20,
        )

    @smoke_case("imageSources.list:all", operation="list", path="/image/sources")
    def test_method_list_with_all_params(self) -> None:
        image_source = client.image_sources.list(
            page_number=1,
            page_size=20,
            next_page_token="next_page_token",
        )

    @smoke_case("imageSources.retrieve:single", operation="retrieve", path="/image/sources/{image_source_id}")
    def test_method_retrieve(self) -> None:
        image_source = client.image_sources.retrieve(
            image_source_id="imageSourceId",
        )

    @smoke_case("imageSources.update:required", operation="update", path="/image/sources/{image_source_id}")
    def test_method_update(self) -> None:
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

    @smoke_case("imageSources.update:all", operation="update", path="/image/sources/{image_source_id}")
    def test_method_update_with_all_params(self) -> None:
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
            fallback_origins=[{"name": "", "type": "dostorage"}],
            secure_urls=False,
        )

    @smoke_case("imageSources.delete:single", operation="delete", path="/image/sources/{image_source_id}")
    def test_method_delete(self) -> None:
        image_source = client.image_sources.delete(
            image_source_id="imageSourceId",
        )

    @smoke_case("imageSources.purgeCache:single", operation="purgeCache", path="/purge/{subdomain}")
    def test_method_purge_cache(self) -> None:
        image_source = client.image_sources.purge_cache(
            subdomain="subdomain",
            paths=["image.jpeg", "image2.png"],
        )

    @smoke_case("imageSources.purge:single", operation="purge", path="/image/purge/{source_id}")
    def test_method_purge(self) -> None:
        image_source = client.image_sources.purge(
            source_id="sourceId",
            paths=["image.jpeg", "image2.png"],
        )
