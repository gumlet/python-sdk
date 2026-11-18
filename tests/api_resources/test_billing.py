# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestBilling:
    @smoke_case("billing.listInvoices:single", operation="listInvoices", path="/mixed/billing/invoice/history")
    def test_method_list_invoices(self) -> None:
        billing = client.billing.list_invoices()

    @smoke_case("billing.fetchDetails:single", operation="fetchDetails", path="/mixed/billing/details")
    def test_method_fetch_details(self) -> None:
        billing = client.billing.fetch_details()

    @smoke_case("billing.updateDetails:single", operation="updateDetails", path="/mixed/billing/details")
    def test_method_update_details(self) -> None:
        billing = client.billing.update_details(
            address_line="",
            city="",
            company_name="",
            country_code="",
            gst_number="",
            postal="",
            state_code="",
        )

    @smoke_case(
        "billing.fetchUpcomingInvoice:single", operation="fetchUpcomingInvoice", path="/mixed/billing/invoice/upcoming"
    )
    def test_method_fetch_upcoming_invoice(self) -> None:
        billing = client.billing.fetch_upcoming_invoice()
