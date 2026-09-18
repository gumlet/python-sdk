# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BillingFetchUpcomingInvoiceResponse", "UpcomingInvoice", "UpcomingInvoiceLines", "UpcomingInvoiceLinesData"]


class UpcomingInvoiceLinesData(BaseModel):
    description: str
    """Description about invoice line item"""

    quantity: str
    """User friendly quantity of the line item"""

    unit_price: float
    """Price per unit for the given item in given currency."""

    amount: str
    """Total amount of the line item"""


class UpcomingInvoiceLines(BaseModel):
    data: List[UpcomingInvoiceLinesData]


class UpcomingInvoice(BaseModel):
    subtotal: str
    """Upcoming invoice amount without tax"""

    lines: UpcomingInvoiceLines
    """Invoice line items"""


class BillingFetchUpcomingInvoiceResponse(BaseModel):
    invoice_start_date: str
    """Invoice start date in DD MMM YYYY format"""

    invoice_last_date: str
    """Invoice end date in DD MMM YYYY format"""

    next_invoice_date: str
    """Next invoice date in DD MMM format"""

    trial_end_date: Optional[str] = None
    """Trial end date"""

    current_month_usage: str
    """Current month total amount in given currency."""

    upcoming_invoice: UpcomingInvoice
    """Upcoming invoice details"""
