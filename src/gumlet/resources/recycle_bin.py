# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
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
from ..types import recycle_bin_recover_params, recycle_bin_list_params
from ..types.recycle_bin_list_response import RecycleBinListResponse

__all__ = ["RecycleBinResource", "AsyncRecycleBinResource"]


class RecycleBinResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecycleBinResourceWithRawResponse:
        return RecycleBinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecycleBinResourceWithStreamingResponse:
        return RecycleBinResourceWithStreamingResponse(self)

    def recover(
        self,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Recovers a deleted asset from the recycle bin.

        Args:
            asset_id: Gumlet Video Asset Id which needs to be recovered.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Example:
            ```python
            client.recycle_bin.recover(
                asset_id="",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/video/asset/recover",
            body=maybe_transform(
                {"asset_id": asset_id},
                recycle_bin_recover_params.RecycleBinRecoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecycleBinListResponse:
        """
        List all assets in a recycle bin for a given workspace. The deleted assets are available for 30 days. After that, assets are permanently deleted.

        Args:
            offset: Number of items to skip from start of page response.
            size: Number of items to return for a single page.
            workspace_id: ID of workspace for which you want to list the recycle bin items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RecycleBinListResponse: Successful response

        Example:
            ```python
            recycle_bin = client.recycle_bin.list(
                size=20,
                workspace_id="workspace_id",
            )
            ```
        """
        return self._get(
            "/video/asset/recoverable/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"offset": offset, "size": size, "workspace_id": workspace_id},
                    recycle_bin_list_params.RecycleBinListParams,
                ),
            ),
            cast_to=RecycleBinListResponse,
        )


class AsyncRecycleBinResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecycleBinResourceWithRawResponse:
        return AsyncRecycleBinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecycleBinResourceWithStreamingResponse:
        return AsyncRecycleBinResourceWithStreamingResponse(self)

    async def recover(
        self,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Recovers a deleted asset from the recycle bin.

        Args:
            asset_id: Gumlet Video Asset Id which needs to be recovered.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Example:
            ```python
            await client.recycle_bin.recover(
                asset_id="",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/video/asset/recover",
            body=await async_maybe_transform(
                {"asset_id": asset_id},
                recycle_bin_recover_params.RecycleBinRecoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecycleBinListResponse:
        """
        List all assets in a recycle bin for a given workspace. The deleted assets are available for 30 days. After that, assets are permanently deleted.

        Args:
            offset: Number of items to skip from start of page response.
            size: Number of items to return for a single page.
            workspace_id: ID of workspace for which you want to list the recycle bin items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RecycleBinListResponse: Successful response

        Example:
            ```python
            recycle_bin = await client.recycle_bin.list(
                size=20,
                workspace_id="workspace_id",
            )
            ```
        """
        return await self._get(
            "/video/asset/recoverable/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"offset": offset, "size": size, "workspace_id": workspace_id},
                    recycle_bin_list_params.RecycleBinListParams,
                ),
            ),
            cast_to=RecycleBinListResponse,
        )


class RecycleBinResourceWithRawResponse:
    def __init__(self, recycle_bin: RecycleBinResource) -> None:
        self._recycle_bin = recycle_bin

        self.recover = to_raw_response_wrapper(
            recycle_bin.recover,
        )
        self.list = to_raw_response_wrapper(
            recycle_bin.list,
        )


class AsyncRecycleBinResourceWithRawResponse:
    def __init__(self, recycle_bin: AsyncRecycleBinResource) -> None:
        self._recycle_bin = recycle_bin

        self.recover = async_to_raw_response_wrapper(
            recycle_bin.recover,
        )
        self.list = async_to_raw_response_wrapper(
            recycle_bin.list,
        )


class RecycleBinResourceWithStreamingResponse:
    def __init__(self, recycle_bin: RecycleBinResource) -> None:
        self._recycle_bin = recycle_bin

        self.recover = to_streamed_response_wrapper(
            recycle_bin.recover,
        )
        self.list = to_streamed_response_wrapper(
            recycle_bin.list,
        )


class AsyncRecycleBinResourceWithStreamingResponse:
    def __init__(self, recycle_bin: AsyncRecycleBinResource) -> None:
        self._recycle_bin = recycle_bin

        self.recover = async_to_streamed_response_wrapper(
            recycle_bin.recover,
        )
        self.list = async_to_streamed_response_wrapper(
            recycle_bin.list,
        )
