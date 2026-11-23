# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BillingListInvoicesParams"]


class BillingListInvoicesParams(TypedDict, total=False):
    page_size: int
    """Number of invoices to return per page. **Default: `20`**. **Maximum: `100`**."""

    last_id: str
    """Stripe invoice ID cursor for the next page. Pass the `id` of the last invoice from the previous response to fetch the next set of invoices."""
