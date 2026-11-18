# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRecycleBin:
    @smoke_case("recycleBin.recover:single", operation="recover", path="/video/asset/recover")
    def test_method_recover(self) -> None:
        client.recycle_bin.recover(
            asset_id="",
        )

    @smoke_case("recycleBin.list:single", operation="list", path="/video/asset/recoverable/list")
    def test_method_list(self) -> None:
        recycle_bin = client.recycle_bin.list(
            workspace_id="workspace_id",
            page_number=1,
            page_size=20,
        )
