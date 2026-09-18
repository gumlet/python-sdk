# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.billing_list_invoices_response import BillingListInvoicesResponse
from ..types.billing_fetch_details_response import BillingFetchDetailsResponse
from ..types.billing_update_details_response import BillingUpdateDetailsResponse
from ..types import billing_update_details_params
from ..types.billing_fetch_upcoming_invoice_response import BillingFetchUpcomingInvoiceResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self)

    def list_invoices(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListInvoicesResponse:
        """
        Liost all invoices that are generated so far.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingListInvoicesResponse: Successful response

        Example:
            ```python
            billing = client.billing.list_invoices()
            ```
        """
        return self._get(
            "/mixed/billing/invoice/history",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingListInvoicesResponse,
        )

    def fetch_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingFetchDetailsResponse:
        """
        Get billing details for this organization.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingFetchDetailsResponse: Successful response

        Example:
            ```python
            billing = client.billing.fetch_details()
            ```
        """
        return self._get(
            "/mixed/billing/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingFetchDetailsResponse,
        )

    def update_details(
        self,
        *,
        address_line: str,
        city: str,
        company_name: str,
        country_code: str,
        gst_number: str,
        postal: str,
        state_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingUpdateDetailsResponse:
        """
        Update billing details

        Args:
            address_line: Address line 1
            city: Name of the city
            company_name: Company name
            country_code: ISO country code
            gst_number: GST / VAT details of the company
            postal: Postal code of the company
            state_code: ISO code of the state / region
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingUpdateDetailsResponse: Successful response

        Example:
            ```python
            billing = client.billing.update_details(
                address_line="",
                city="",
                company_name="",
                country_code="",
                gst_number="",
                postal="",
                state_code="",
            )
            ```
        """
        return self._post(
            "/mixed/billing/details",
            body=maybe_transform(
                {
                    "address_line": address_line,
                    "city": city,
                    "company_name": company_name,
                    "country_code": country_code,
                    "gst_number": gst_number,
                    "postal": postal,
                    "state_code": state_code,
                },
                billing_update_details_params.BillingUpdateDetailsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingUpdateDetailsResponse,
        )

    def fetch_upcoming_invoice(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingFetchUpcomingInvoiceResponse:
        """
        Get details about upcoming invoice.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingFetchUpcomingInvoiceResponse: Successful response

        Example:
            ```python
            billing = client.billing.fetch_upcoming_invoice()
            ```
        """
        return self._get(
            "/mixed/billing/invoice/upcoming",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingFetchUpcomingInvoiceResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self)

    async def list_invoices(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListInvoicesResponse:
        """
        Liost all invoices that are generated so far.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingListInvoicesResponse: Successful response

        Example:
            ```python
            billing = await client.billing.list_invoices()
            ```
        """
        return await self._get(
            "/mixed/billing/invoice/history",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingListInvoicesResponse,
        )

    async def fetch_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingFetchDetailsResponse:
        """
        Get billing details for this organization.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingFetchDetailsResponse: Successful response

        Example:
            ```python
            billing = await client.billing.fetch_details()
            ```
        """
        return await self._get(
            "/mixed/billing/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingFetchDetailsResponse,
        )

    async def update_details(
        self,
        *,
        address_line: str,
        city: str,
        company_name: str,
        country_code: str,
        gst_number: str,
        postal: str,
        state_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingUpdateDetailsResponse:
        """
        Update billing details

        Args:
            address_line: Address line 1
            city: Name of the city
            company_name: Company name
            country_code: ISO country code
            gst_number: GST / VAT details of the company
            postal: Postal code of the company
            state_code: ISO code of the state / region
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingUpdateDetailsResponse: Successful response

        Example:
            ```python
            billing = await client.billing.update_details(
                address_line="",
                city="",
                company_name="",
                country_code="",
                gst_number="",
                postal="",
                state_code="",
            )
            ```
        """
        return await self._post(
            "/mixed/billing/details",
            body=await async_maybe_transform(
                {
                    "address_line": address_line,
                    "city": city,
                    "company_name": company_name,
                    "country_code": country_code,
                    "gst_number": gst_number,
                    "postal": postal,
                    "state_code": state_code,
                },
                billing_update_details_params.BillingUpdateDetailsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingUpdateDetailsResponse,
        )

    async def fetch_upcoming_invoice(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingFetchUpcomingInvoiceResponse:
        """
        Get details about upcoming invoice.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingFetchUpcomingInvoiceResponse: Successful response

        Example:
            ```python
            billing = await client.billing.fetch_upcoming_invoice()
            ```
        """
        return await self._get(
            "/mixed/billing/invoice/upcoming",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingFetchUpcomingInvoiceResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.list_invoices = to_raw_response_wrapper(
            billing.list_invoices,
        )
        self.fetch_details = to_raw_response_wrapper(
            billing.fetch_details,
        )
        self.update_details = to_raw_response_wrapper(
            billing.update_details,
        )
        self.fetch_upcoming_invoice = to_raw_response_wrapper(
            billing.fetch_upcoming_invoice,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.list_invoices = async_to_raw_response_wrapper(
            billing.list_invoices,
        )
        self.fetch_details = async_to_raw_response_wrapper(
            billing.fetch_details,
        )
        self.update_details = async_to_raw_response_wrapper(
            billing.update_details,
        )
        self.fetch_upcoming_invoice = async_to_raw_response_wrapper(
            billing.fetch_upcoming_invoice,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.list_invoices = to_streamed_response_wrapper(
            billing.list_invoices,
        )
        self.fetch_details = to_streamed_response_wrapper(
            billing.fetch_details,
        )
        self.update_details = to_streamed_response_wrapper(
            billing.update_details,
        )
        self.fetch_upcoming_invoice = to_streamed_response_wrapper(
            billing.fetch_upcoming_invoice,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.list_invoices = async_to_streamed_response_wrapper(
            billing.list_invoices,
        )
        self.fetch_details = async_to_streamed_response_wrapper(
            billing.fetch_details,
        )
        self.update_details = async_to_streamed_response_wrapper(
            billing.update_details,
        )
        self.fetch_upcoming_invoice = async_to_streamed_response_wrapper(
            billing.fetch_upcoming_invoice,
        )
