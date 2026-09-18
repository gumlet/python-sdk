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
from ..types.user_data_fetch_response import UserDataFetchResponse

__all__ = ["UserDataResource", "AsyncUserDataResource"]


class UserDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserDataResourceWithRawResponse:
        return UserDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserDataResourceWithStreamingResponse:
        return UserDataResourceWithStreamingResponse(self)

    def fetch(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDataFetchResponse:
        """
        This endpoint gives information about the user account.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserDataFetchResponse: Successful response

        Example:
            ```python
            user_data = client.user_data.fetch()
            ```
        """
        return self._get(
            "/user/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDataFetchResponse,
        )


class AsyncUserDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserDataResourceWithRawResponse:
        return AsyncUserDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserDataResourceWithStreamingResponse:
        return AsyncUserDataResourceWithStreamingResponse(self)

    async def fetch(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDataFetchResponse:
        """
        This endpoint gives information about the user account.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserDataFetchResponse: Successful response

        Example:
            ```python
            user_data = await client.user_data.fetch()
            ```
        """
        return await self._get(
            "/user/data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDataFetchResponse,
        )


class UserDataResourceWithRawResponse:
    def __init__(self, user_data: UserDataResource) -> None:
        self._user_data = user_data

        self.fetch = to_raw_response_wrapper(
            user_data.fetch,
        )


class AsyncUserDataResourceWithRawResponse:
    def __init__(self, user_data: AsyncUserDataResource) -> None:
        self._user_data = user_data

        self.fetch = async_to_raw_response_wrapper(
            user_data.fetch,
        )


class UserDataResourceWithStreamingResponse:
    def __init__(self, user_data: UserDataResource) -> None:
        self._user_data = user_data

        self.fetch = to_streamed_response_wrapper(
            user_data.fetch,
        )


class AsyncUserDataResourceWithStreamingResponse:
    def __init__(self, user_data: AsyncUserDataResource) -> None:
        self._user_data = user_data

        self.fetch = async_to_streamed_response_wrapper(
            user_data.fetch,
        )
