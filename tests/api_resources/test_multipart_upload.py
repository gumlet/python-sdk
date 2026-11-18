# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestMultipartUpload:
    @smoke_case(
        "multipartUpload.retrievePartUrl:single",
        operation="retrievePartUrl",
        path="/video/assets/{asset_id}/multipartupload/{part_number}/sign",
    )
    def test_method_retrieve_part_url(self) -> None:
        multipart_upload = client.multipart_upload.retrieve_part_url(
            asset_id="assetId",
            part_number="partNumber",
        )

    @smoke_case(
        "multipartUpload.complete:required",
        operation="complete",
        path="/video/assets/{asset_id}/multipartupload/complete",
    )
    def test_method_complete(self) -> None:
        multipart_upload = client.multipart_upload.complete(
            asset_id="assetId",
        )

    @smoke_case(
        "multipartUpload.complete:all", operation="complete", path="/video/assets/{asset_id}/multipartupload/complete"
    )
    def test_method_complete_with_all_params(self) -> None:
        multipart_upload = client.multipart_upload.complete(
            asset_id="assetId",
            parts=[{}],
        )

    @smoke_case(
        "multipartUpload.abort:single", operation="abort", path="/video/assets/{asset_id}/multipartupload/abort"
    )
    def test_method_abort(self) -> None:
        multipart_upload = client.multipart_upload.abort(
            asset_id="assetId",
        )

    @smoke_case("multipartUpload.list:single", operation="list", path="/video/assets/{asset_id}/multipartupload/list")
    def test_method_list(self) -> None:
        multipart_upload = client.multipart_upload.list(
            asset_id="assetId",
        )
