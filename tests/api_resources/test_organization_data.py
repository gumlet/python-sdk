# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestOrganizationData:
    @smoke_case("organizationData.fetchOrg:single", operation="fetchOrg", path="/org/data")
    def test_method_fetch_org(self) -> None:
        organization_data = client.organization_data.fetch_org()
