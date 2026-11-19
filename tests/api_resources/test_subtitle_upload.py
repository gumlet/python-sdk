# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestSubtitleUpload:
    @smoke_case("subtitleUpload.upload:single", operation="upload", path="/video/assets/{asset_ID}/subtitle/upload")
    def test_method_upload(self) -> None:
        subtitle_upload = client.subtitle_upload.upload(
            asset_id="assetId",
            language_codes=["en"],
        )

    @smoke_case(
        "subtitleUpload.complete:single", operation="complete", path="/video/assets/{asset_ID}/subtitle/upload/event"
    )
    def test_method_complete(self) -> None:
        subtitle_upload = client.subtitle_upload.complete(
            asset_id="assetId",
            upload_responses=[{"language_code": "en", "uploaded": True}],
        )
