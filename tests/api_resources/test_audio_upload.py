# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAudioUpload:
    @smoke_case("audioUpload.upload:single", operation="upload", path="/video/assets/{asset_ID}/audio/upload")
    def test_method_upload(self) -> None:
        audio_upload = client.audio_upload.upload(
            asset_id="assetId",
            language_codes=["en"],
        )

    @smoke_case("audioUpload.complete:single", operation="complete", path="/video/assets/{asset_ID}/audio/upload/event")
    def test_method_complete(self) -> None:
        audio_upload = client.audio_upload.complete(
            asset_id="assetId",
            upload_responses=[{"language_codes": ["en"], "uploaded": True}],
        )
