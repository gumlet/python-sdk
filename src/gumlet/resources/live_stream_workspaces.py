# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.live_stream_workspace_list_response import LiveStreamWorkspaceListResponse
from ..types.live_stream_workspace_create_response import LiveStreamWorkspaceCreateResponse
from ..types import live_stream_workspace_create_params, live_stream_workspace_update_params
from ..types.live_stream_workspace_update_response import LiveStreamWorkspaceUpdateResponse
from ..types.live_stream_workspace_delete_response import LiveStreamWorkspaceDeleteResponse

__all__ = ["LiveStreamWorkspacesResource", "AsyncLiveStreamWorkspacesResource"]


class LiveStreamWorkspacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveStreamWorkspacesResourceWithRawResponse:
        return LiveStreamWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveStreamWorkspacesResourceWithStreamingResponse:
        return LiveStreamWorkspacesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceListResponse:
        """
        List all live stream workspaces.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceListResponse: Successful response

        Example:
            ```python
            live_stream_workspace = client.live_stream_workspaces.list()
            ```
        """
        return self._get(
            "/video/sources/live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceListResponse,
        )

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceCreateResponse:
        """
        Create live stream workspace.

        Args:
            name: Collection name
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceCreateResponse: Successful response

        Example:
            ```python
            live_stream_workspace = client.live_stream_workspaces.create(
                name="",
            )
            ```
        """
        return self._post(
            "/video/sources/live",
            body=maybe_transform(
                {"name": name},
                live_stream_workspace_create_params.LiveStreamWorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceCreateResponse,
        )

    def update(
        self,
        live_workspace_id: str,
        *,
        name: str | Omit = omit,
        video_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceUpdateResponse:
        """
        Update live stream workspace.

        Args:
            live_workspace_id: Live stream workspace ID.
            name: Live stream collection name
            video_source_id: Video on demand workspace ID
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceUpdateResponse: Get updated collection details.

        Example:
            ```python
            live_stream_workspace = client.live_stream_workspaces.update(
                live_workspace_id="liveWorkspaceId",
                name="live-stream-collections",
                video_source_id="67bea1d66ca0059a95bf7de9",
            )
            ```
        """
        if live_workspace_id is None or (isinstance(live_workspace_id, str) and not live_workspace_id):
            raise ValueError(f"Expected a non-empty value for `live_workspace_id` but received {live_workspace_id!r}")
        return self._post(
            path_template("/video/sources/live/{live_workspace_id}", **{"live_workspace_id": live_workspace_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "video_source_id": video_source_id,
                },
                live_stream_workspace_update_params.LiveStreamWorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceUpdateResponse,
        )

    def delete(
        self,
        live_workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceDeleteResponse:
        """
        Delete the live stream workspace.

        Args:
            live_workspace_id: Live stream workspace ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceDeleteResponse: Successful response

        Example:
            ```python
            live_stream_workspace = client.live_stream_workspaces.delete(
                live_workspace_id="liveWorkspaceId",
            )
            ```
        """
        if live_workspace_id is None or (isinstance(live_workspace_id, str) and not live_workspace_id):
            raise ValueError(f"Expected a non-empty value for `live_workspace_id` but received {live_workspace_id!r}")
        return self._delete(
            path_template("/video/sources/live/{live_workspace_id}", **{"live_workspace_id": live_workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceDeleteResponse,
        )


class AsyncLiveStreamWorkspacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveStreamWorkspacesResourceWithRawResponse:
        return AsyncLiveStreamWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveStreamWorkspacesResourceWithStreamingResponse:
        return AsyncLiveStreamWorkspacesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceListResponse:
        """
        List all live stream workspaces.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceListResponse: Successful response

        Example:
            ```python
            live_stream_workspace = await client.live_stream_workspaces.list()
            ```
        """
        return await self._get(
            "/video/sources/live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceCreateResponse:
        """
        Create live stream workspace.

        Args:
            name: Collection name
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceCreateResponse: Successful response

        Example:
            ```python
            live_stream_workspace = await client.live_stream_workspaces.create(
                name="",
            )
            ```
        """
        return await self._post(
            "/video/sources/live",
            body=await async_maybe_transform(
                {"name": name},
                live_stream_workspace_create_params.LiveStreamWorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceCreateResponse,
        )

    async def update(
        self,
        live_workspace_id: str,
        *,
        name: str | Omit = omit,
        video_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceUpdateResponse:
        """
        Update live stream workspace.

        Args:
            live_workspace_id: Live stream workspace ID.
            name: Live stream collection name
            video_source_id: Video on demand workspace ID
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceUpdateResponse: Get updated collection details.

        Example:
            ```python
            live_stream_workspace = await client.live_stream_workspaces.update(
                live_workspace_id="liveWorkspaceId",
                name="live-stream-collections",
                video_source_id="67bea1d66ca0059a95bf7de9",
            )
            ```
        """
        if live_workspace_id is None or (isinstance(live_workspace_id, str) and not live_workspace_id):
            raise ValueError(f"Expected a non-empty value for `live_workspace_id` but received {live_workspace_id!r}")
        return await self._post(
            path_template("/video/sources/live/{live_workspace_id}", **{"live_workspace_id": live_workspace_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "video_source_id": video_source_id,
                },
                live_stream_workspace_update_params.LiveStreamWorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceUpdateResponse,
        )

    async def delete(
        self,
        live_workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamWorkspaceDeleteResponse:
        """
        Delete the live stream workspace.

        Args:
            live_workspace_id: Live stream workspace ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamWorkspaceDeleteResponse: Successful response

        Example:
            ```python
            live_stream_workspace = await client.live_stream_workspaces.delete(
                live_workspace_id="liveWorkspaceId",
            )
            ```
        """
        if live_workspace_id is None or (isinstance(live_workspace_id, str) and not live_workspace_id):
            raise ValueError(f"Expected a non-empty value for `live_workspace_id` but received {live_workspace_id!r}")
        return await self._delete(
            path_template("/video/sources/live/{live_workspace_id}", **{"live_workspace_id": live_workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamWorkspaceDeleteResponse,
        )


class LiveStreamWorkspacesResourceWithRawResponse:
    def __init__(self, live_stream_workspaces: LiveStreamWorkspacesResource) -> None:
        self._live_stream_workspaces = live_stream_workspaces

        self.list = to_raw_response_wrapper(
            live_stream_workspaces.list,
        )
        self.create = to_raw_response_wrapper(
            live_stream_workspaces.create,
        )
        self.update = to_raw_response_wrapper(
            live_stream_workspaces.update,
        )
        self.delete = to_raw_response_wrapper(
            live_stream_workspaces.delete,
        )


class AsyncLiveStreamWorkspacesResourceWithRawResponse:
    def __init__(self, live_stream_workspaces: AsyncLiveStreamWorkspacesResource) -> None:
        self._live_stream_workspaces = live_stream_workspaces

        self.list = async_to_raw_response_wrapper(
            live_stream_workspaces.list,
        )
        self.create = async_to_raw_response_wrapper(
            live_stream_workspaces.create,
        )
        self.update = async_to_raw_response_wrapper(
            live_stream_workspaces.update,
        )
        self.delete = async_to_raw_response_wrapper(
            live_stream_workspaces.delete,
        )


class LiveStreamWorkspacesResourceWithStreamingResponse:
    def __init__(self, live_stream_workspaces: LiveStreamWorkspacesResource) -> None:
        self._live_stream_workspaces = live_stream_workspaces

        self.list = to_streamed_response_wrapper(
            live_stream_workspaces.list,
        )
        self.create = to_streamed_response_wrapper(
            live_stream_workspaces.create,
        )
        self.update = to_streamed_response_wrapper(
            live_stream_workspaces.update,
        )
        self.delete = to_streamed_response_wrapper(
            live_stream_workspaces.delete,
        )


class AsyncLiveStreamWorkspacesResourceWithStreamingResponse:
    def __init__(self, live_stream_workspaces: AsyncLiveStreamWorkspacesResource) -> None:
        self._live_stream_workspaces = live_stream_workspaces

        self.list = async_to_streamed_response_wrapper(
            live_stream_workspaces.list,
        )
        self.create = async_to_streamed_response_wrapper(
            live_stream_workspaces.create,
        )
        self.update = async_to_streamed_response_wrapper(
            live_stream_workspaces.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            live_stream_workspaces.delete,
        )
