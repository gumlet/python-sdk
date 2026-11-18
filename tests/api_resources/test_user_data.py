# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestUserData:
    @smoke_case("userData.fetch:single", operation="fetch", path="/user/data")
    def test_method_fetch(self) -> None:
        user_data = client.user_data.fetch()
