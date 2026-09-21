# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.global_search_search_response import GlobalSearchSearchResponse
from ..types import global_search_search_params

__all__ = ["GlobalSearchResource", "AsyncGlobalSearchResource"]


class GlobalSearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalSearchResourceWithRawResponse:
        return GlobalSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalSearchResourceWithStreamingResponse:
        return GlobalSearchResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        search_query: str,
        collection_id: str | Omit = omit,
        size: int | Omit = omit,
        assets_offset: int | Omit = omit,
        folders_offset: int | Omit = omit,
        playlists_offset: int | Omit = omit,
        channels_offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalSearchSearchResponse:
        """
        Search all video assets / playlists / folders etc across workspaces.

        Args:
            search_query: Search query term
            collection_id: Workspace ID if you want to limit search to a specific workspace
            size: Number of results to return
            assets_offset: Offset for assets
            folders_offset: Offset for folders
            playlists_offset: Offset for playlists
            channels_offset: Offset for channels
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GlobalSearchSearchResponse: Successful response

        Example:
            ```python
            global_search = client.global_search.search(
                search_query="search_query",
                size=20,
                assets_offset=0,
                folders_offset=0,
                playlists_offset=0,
                channels_offset=0,
            )
            ```
        """
        return self._get(
            "/entities/global-search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "search_query": search_query,
                        "collection_id": collection_id,
                        "size": size,
                        "assets_offset": assets_offset,
                        "folders_offset": folders_offset,
                        "playlists_offset": playlists_offset,
                        "channels_offset": channels_offset,
                    },
                    global_search_search_params.GlobalSearchSearchParams,
                ),
            ),
            cast_to=GlobalSearchSearchResponse,
        )


class AsyncGlobalSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalSearchResourceWithRawResponse:
        return AsyncGlobalSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalSearchResourceWithStreamingResponse:
        return AsyncGlobalSearchResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        search_query: str,
        collection_id: str | Omit = omit,
        size: int | Omit = omit,
        assets_offset: int | Omit = omit,
        folders_offset: int | Omit = omit,
        playlists_offset: int | Omit = omit,
        channels_offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalSearchSearchResponse:
        """
        Search all video assets / playlists / folders etc across workspaces.

        Args:
            search_query: Search query term
            collection_id: Workspace ID if you want to limit search to a specific workspace
            size: Number of results to return
            assets_offset: Offset for assets
            folders_offset: Offset for folders
            playlists_offset: Offset for playlists
            channels_offset: Offset for channels
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GlobalSearchSearchResponse: Successful response

        Example:
            ```python
            global_search = await client.global_search.search(
                search_query="search_query",
                size=20,
                assets_offset=0,
                folders_offset=0,
                playlists_offset=0,
                channels_offset=0,
            )
            ```
        """
        return await self._get(
            "/entities/global-search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "search_query": search_query,
                        "collection_id": collection_id,
                        "size": size,
                        "assets_offset": assets_offset,
                        "folders_offset": folders_offset,
                        "playlists_offset": playlists_offset,
                        "channels_offset": channels_offset,
                    },
                    global_search_search_params.GlobalSearchSearchParams,
                ),
            ),
            cast_to=GlobalSearchSearchResponse,
        )


class GlobalSearchResourceWithRawResponse:
    def __init__(self, global_search: GlobalSearchResource) -> None:
        self._global_search = global_search

        self.search = to_raw_response_wrapper(
            global_search.search,
        )


class AsyncGlobalSearchResourceWithRawResponse:
    def __init__(self, global_search: AsyncGlobalSearchResource) -> None:
        self._global_search = global_search

        self.search = async_to_raw_response_wrapper(
            global_search.search,
        )


class GlobalSearchResourceWithStreamingResponse:
    def __init__(self, global_search: GlobalSearchResource) -> None:
        self._global_search = global_search

        self.search = to_streamed_response_wrapper(
            global_search.search,
        )


class AsyncGlobalSearchResourceWithStreamingResponse:
    def __init__(self, global_search: AsyncGlobalSearchResource) -> None:
        self._global_search = global_search

        self.search = async_to_streamed_response_wrapper(
            global_search.search,
        )
