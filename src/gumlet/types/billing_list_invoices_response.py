# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingListInvoicesResponse", "StripeInvoice"]


class StripeInvoice(BaseModel):
    id: str
    """Invoice ID as per stripe. This is not invoice number."""

    status: Literal["draft", "open", "paid", "uncollectible", "void"]
    """Current status of the invoice"""

    created: int
    """Created timestamp of invoice in seconds since epoch"""

    amount_due: int
    """Amount due for invoice in the lowest denomination of the given currency. For example if the invoice is in USD, the amount shown here is in cents. Therefore, a value like 10000 means the invoice is $100."""

    hosted_invoice_url: str
    """URL of the invoice page where you can pay the invoice"""

    invoice_pdf: str
    """URL of the page from where you can download the invoice PDF"""


class BillingListInvoicesResponse(BaseModel):
    unpaid_invoices: bool
    """Flag which shows if this account has any unpaid invoices."""

    stripe_invoices: List[StripeInvoice]
    """List of invoices"""
