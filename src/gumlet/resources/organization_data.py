# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.organization_data_fetch_org_response import OrganizationDataFetchOrgResponse

__all__ = ["OrganizationDataResource", "AsyncOrganizationDataResource"]


class OrganizationDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationDataResourceWithRawResponse:
        return OrganizationDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationDataResourceWithStreamingResponse:
        return OrganizationDataResourceWithStreamingResponse(self)

    def fetch_org(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDataFetchOrgResponse:
        """
        You can get organization data using this API.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationDataFetchOrgResponse: Successful response

        Example:
            ```python
            organization_data = client.organization_data.fetch_org()
            ```
        """
        return self._get(
            "/org/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationDataFetchOrgResponse,
        )


class AsyncOrganizationDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationDataResourceWithRawResponse:
        return AsyncOrganizationDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationDataResourceWithStreamingResponse:
        return AsyncOrganizationDataResourceWithStreamingResponse(self)

    async def fetch_org(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDataFetchOrgResponse:
        """
        You can get organization data using this API.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationDataFetchOrgResponse: Successful response

        Example:
            ```python
            organization_data = await client.organization_data.fetch_org()
            ```
        """
        return await self._get(
            "/org/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationDataFetchOrgResponse,
        )


class OrganizationDataResourceWithRawResponse:
    def __init__(self, organization_data: OrganizationDataResource) -> None:
        self._organization_data = organization_data

        self.fetch_org = to_raw_response_wrapper(
            organization_data.fetch_org,
        )


class AsyncOrganizationDataResourceWithRawResponse:
    def __init__(self, organization_data: AsyncOrganizationDataResource) -> None:
        self._organization_data = organization_data

        self.fetch_org = async_to_raw_response_wrapper(
            organization_data.fetch_org,
        )


class OrganizationDataResourceWithStreamingResponse:
    def __init__(self, organization_data: OrganizationDataResource) -> None:
        self._organization_data = organization_data

        self.fetch_org = to_streamed_response_wrapper(
            organization_data.fetch_org,
        )


class AsyncOrganizationDataResourceWithStreamingResponse:
    def __init__(self, organization_data: AsyncOrganizationDataResource) -> None:
        self._organization_data = organization_data

        self.fetch_org = async_to_streamed_response_wrapper(
            organization_data.fetch_org,
        )
