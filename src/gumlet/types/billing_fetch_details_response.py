# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["BillingFetchDetailsResponse"]


class BillingFetchDetailsResponse(BaseModel):
    company_name: str
    """Company name"""

    gst_number: str
    """GST / VAT number"""

    address_line: str
    """Address line 1"""

    city: str
    """City"""

    state_code: str
    """ISO code of the state"""

    postal: str
    """Postal code"""

    country_code: str
    """ISO code of country. For example, it's "US" for USA."""
