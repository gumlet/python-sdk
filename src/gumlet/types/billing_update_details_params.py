# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillingUpdateDetailsParams"]


class BillingUpdateDetailsParams(TypedDict, total=False):
    address_line: Required[str]
    """Address line 1"""

    city: Required[str]
    """Name of the city"""

    company_name: Required[str]
    """Company name"""

    country_code: Required[str]
    """ISO country code"""

    gst_number: Required[str]
    """GST / VAT details of the company"""

    postal: Required[str]
    """Postal code of the company"""

    state_code: Required[str]
    """ISO code of the state / region"""
