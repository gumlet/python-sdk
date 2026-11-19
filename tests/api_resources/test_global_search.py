# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestGlobalSearch:
    @smoke_case("globalSearch.search:required", operation="search", path="/entities/global-search")
    def test_method_search(self) -> None:
        global_search = client.global_search.search(
            search_query="search_query",
            size=20,
            assets_offset=0,
            folders_offset=0,
            playlists_offset=0,
            channels_offset=0,
        )

    @smoke_case("globalSearch.search:all", operation="search", path="/entities/global-search")
    def test_method_search_with_all_params(self) -> None:
        global_search = client.global_search.search(
            search_query="search_query",
            workspace_id="workspace_id",
            collection_id="collection_id",
            size=20,
            assets_offset=0,
            folders_offset=0,
            playlists_offset=0,
            channels_offset=0,
        )
