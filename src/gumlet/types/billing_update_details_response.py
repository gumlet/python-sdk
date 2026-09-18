# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["BillingUpdateDetailsResponse"]


class BillingUpdateDetailsResponse(BaseModel):
    address_line: str
    """Address line 1"""

    city: str
    """Name of the city"""

    company_name: str
    """Company name"""

    country_code: str
    """ISO country code"""

    gst_number: str
    """GST / VAT details of the company"""

    postal: str
    """Postal code of the company"""

    state_code: str
    """ISO code of the state / region"""
