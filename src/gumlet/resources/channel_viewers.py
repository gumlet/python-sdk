# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Mapping, cast
from .._types import FileTypes, SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._files import deepcopy_with_paths
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.channel_viewer_invite_response import ChannelViewerInviteResponse
from ..types import (
    channel_viewer_invite_params,
    channel_viewer_delete_params,
    channel_viewer_invite_csv_params,
    channel_viewer_list_subscribers_params,
)
from ..types.channel_viewer_delete_response import ChannelViewerDeleteResponse
from ..types.channel_viewer_invite_csv_response import ChannelViewerInviteCsvResponse
from ..types.channel_viewer_list_subscribers_response import ChannelViewerListSubscribersResponse

__all__ = ["ChannelViewersResource", "AsyncChannelViewersResource"]


class ChannelViewersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelViewersResourceWithRawResponse:
        return ChannelViewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelViewersResourceWithStreamingResponse:
        return ChannelViewersResourceWithStreamingResponse(self)

    def invite(
        self,
        video_workspace_id: str,
        *,
        users: Iterable[channel_viewer_invite_params.User],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerInviteResponse:
        """
        Invite one or more viewers to a members-only channel.

        Args:
            video_workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            users: List of viewers to invite. A maximum of 200 viewers can be invited in one request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerInviteResponse: 200

        Example:
            ```python
            channel_viewer = client.channel_viewers.invite(
                video_workspace_id="videoWorkspaceId",
                users=[
                    {"email": "test@gumlet.com", "name": "Test User-0"},
                    {"email": "test+1@gumlet.com", "name": "Test User-1"},
                    {"email": "test+2@gumlet.com", "name": "Test User-2"},
                ],
            )
            ```
        """
        if video_workspace_id is None or (isinstance(video_workspace_id, str) and not video_workspace_id):
            raise ValueError(f"Expected a non-empty value for `video_workspace_id` but received {video_workspace_id!r}")
        return self._post(
            path_template("/channel/{video_workspace_id}/viewers/invite", **{"video_workspace_id": video_workspace_id}),
            body=maybe_transform(
                {"users": users},
                channel_viewer_invite_params.ChannelViewerInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelViewerInviteResponse,
        )

    def delete(
        self,
        video_workspace_id: str,
        *,
        emails: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerDeleteResponse:
        """
        Remove one or more viewers from a channel by email address.

        Args:
            video_workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            emails: Email addresses of viewers to remove. A maximum of 200 viewers can be removed in one request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerDeleteResponse: 200

        Example:
            ```python
            channel_viewer = client.channel_viewers.delete(
                video_workspace_id="videoWorkspaceId",
                emails=["test@gumlet.com", "test+2@gumlet.com"],
            )
            ```
        """
        if video_workspace_id is None or (isinstance(video_workspace_id, str) and not video_workspace_id):
            raise ValueError(f"Expected a non-empty value for `video_workspace_id` but received {video_workspace_id!r}")
        return self._post(
            path_template("/channel/{video_workspace_id}/viewers/remove", **{"video_workspace_id": video_workspace_id}),
            body=maybe_transform(
                {"emails": emails},
                channel_viewer_delete_params.ChannelViewerDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelViewerDeleteResponse,
        )

    def invite_csv(
        self,
        video_workspace_id: str,
        *,
        viewers_csv: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerInviteCsvResponse:
        """
        Invite viewers to a channel by uploading a CSV file.

        Args:
            video_workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            viewers_csv: CSV file containing viewer rows. Required columns: email, name. Maximum 500 viewers.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerInviteCsvResponse: 200

        Example:
            ```python
            channel_viewer = client.channel_viewers.invite_csv(
                video_workspace_id="videoWorkspaceId",
                viewers_csv=b"viewers.csv",
            )
            ```
        """
        if video_workspace_id is None or (isinstance(video_workspace_id, str) and not video_workspace_id):
            raise ValueError(f"Expected a non-empty value for `video_workspace_id` but received {video_workspace_id!r}")
        body = deepcopy_with_paths(
            {
                "viewers_csv": viewers_csv,
            },
            [["viewers_csv"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["viewers_csv"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template(
                "/channel/{video_workspace_id}/viewers/invite/csv", **{"video_workspace_id": video_workspace_id}
            ),
            body=maybe_transform(body, channel_viewer_invite_csv_params.ChannelViewerInviteCsvParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelViewerInviteCsvResponse,
        )

    def list_subscribers(
        self,
        workspace_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerListSubscribersResponse:
        """
        List all channel subscribers.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            page_number: Page number to retrieve. Starts at 1.
            page_size: Number of items to return per page
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerListSubscribersResponse: Successful response

        Example:
            ```python
            channel_viewer = client.channel_viewers.list_subscribers(
                workspace_id="workspaceId",
                page_number=1,
                page_size=10,
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            path_template("/channel/{workspace_id}/viewers", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page_number": page_number, "page_size": page_size},
                    channel_viewer_list_subscribers_params.ChannelViewerListSubscribersParams,
                ),
            ),
            cast_to=ChannelViewerListSubscribersResponse,
        )


class AsyncChannelViewersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelViewersResourceWithRawResponse:
        return AsyncChannelViewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelViewersResourceWithStreamingResponse:
        return AsyncChannelViewersResourceWithStreamingResponse(self)

    async def invite(
        self,
        video_workspace_id: str,
        *,
        users: Iterable[channel_viewer_invite_params.User],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerInviteResponse:
        """
        Invite one or more viewers to a members-only channel.

        Args:
            video_workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            users: List of viewers to invite. A maximum of 200 viewers can be invited in one request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerInviteResponse: 200

        Example:
            ```python
            channel_viewer = await client.channel_viewers.invite(
                video_workspace_id="videoWorkspaceId",
                users=[
                    {"email": "test@gumlet.com", "name": "Test User-0"},
                    {"email": "test+1@gumlet.com", "name": "Test User-1"},
                    {"email": "test+2@gumlet.com", "name": "Test User-2"},
                ],
            )
            ```
        """
        if video_workspace_id is None or (isinstance(video_workspace_id, str) and not video_workspace_id):
            raise ValueError(f"Expected a non-empty value for `video_workspace_id` but received {video_workspace_id!r}")
        return await self._post(
            path_template("/channel/{video_workspace_id}/viewers/invite", **{"video_workspace_id": video_workspace_id}),
            body=await async_maybe_transform(
                {"users": users},
                channel_viewer_invite_params.ChannelViewerInviteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelViewerInviteResponse,
        )

    async def delete(
        self,
        video_workspace_id: str,
        *,
        emails: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerDeleteResponse:
        """
        Remove one or more viewers from a channel by email address.

        Args:
            video_workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            emails: Email addresses of viewers to remove. A maximum of 200 viewers can be removed in one request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerDeleteResponse: 200

        Example:
            ```python
            channel_viewer = await client.channel_viewers.delete(
                video_workspace_id="videoWorkspaceId",
                emails=["test@gumlet.com", "test+2@gumlet.com"],
            )
            ```
        """
        if video_workspace_id is None or (isinstance(video_workspace_id, str) and not video_workspace_id):
            raise ValueError(f"Expected a non-empty value for `video_workspace_id` but received {video_workspace_id!r}")
        return await self._post(
            path_template("/channel/{video_workspace_id}/viewers/remove", **{"video_workspace_id": video_workspace_id}),
            body=await async_maybe_transform(
                {"emails": emails},
                channel_viewer_delete_params.ChannelViewerDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelViewerDeleteResponse,
        )

    async def invite_csv(
        self,
        video_workspace_id: str,
        *,
        viewers_csv: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerInviteCsvResponse:
        """
        Invite viewers to a channel by uploading a CSV file.

        Args:
            video_workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            viewers_csv: CSV file containing viewer rows. Required columns: email, name. Maximum 500 viewers.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerInviteCsvResponse: 200

        Example:
            ```python
            channel_viewer = await client.channel_viewers.invite_csv(
                video_workspace_id="videoWorkspaceId",
                viewers_csv=b"viewers.csv",
            )
            ```
        """
        if video_workspace_id is None or (isinstance(video_workspace_id, str) and not video_workspace_id):
            raise ValueError(f"Expected a non-empty value for `video_workspace_id` but received {video_workspace_id!r}")
        body = deepcopy_with_paths(
            {
                "viewers_csv": viewers_csv,
            },
            [["viewers_csv"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["viewers_csv"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/channel/{video_workspace_id}/viewers/invite/csv", **{"video_workspace_id": video_workspace_id}
            ),
            body=await async_maybe_transform(body, channel_viewer_invite_csv_params.ChannelViewerInviteCsvParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelViewerInviteCsvResponse,
        )

    async def list_subscribers(
        self,
        workspace_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelViewerListSubscribersResponse:
        """
        List all channel subscribers.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            page_number: Page number to retrieve. Starts at 1.
            page_size: Number of items to return per page
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChannelViewerListSubscribersResponse: Successful response

        Example:
            ```python
            channel_viewer = await client.channel_viewers.list_subscribers(
                workspace_id="workspaceId",
                page_number=1,
                page_size=10,
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            path_template("/channel/{workspace_id}/viewers", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page_number": page_number, "page_size": page_size},
                    channel_viewer_list_subscribers_params.ChannelViewerListSubscribersParams,
                ),
            ),
            cast_to=ChannelViewerListSubscribersResponse,
        )


class ChannelViewersResourceWithRawResponse:
    def __init__(self, channel_viewers: ChannelViewersResource) -> None:
        self._channel_viewers = channel_viewers

        self.invite = to_raw_response_wrapper(
            channel_viewers.invite,
        )
        self.delete = to_raw_response_wrapper(
            channel_viewers.delete,
        )
        self.invite_csv = to_raw_response_wrapper(
            channel_viewers.invite_csv,
        )
        self.list_subscribers = to_raw_response_wrapper(
            channel_viewers.list_subscribers,
        )


class AsyncChannelViewersResourceWithRawResponse:
    def __init__(self, channel_viewers: AsyncChannelViewersResource) -> None:
        self._channel_viewers = channel_viewers

        self.invite = async_to_raw_response_wrapper(
            channel_viewers.invite,
        )
        self.delete = async_to_raw_response_wrapper(
            channel_viewers.delete,
        )
        self.invite_csv = async_to_raw_response_wrapper(
            channel_viewers.invite_csv,
        )
        self.list_subscribers = async_to_raw_response_wrapper(
            channel_viewers.list_subscribers,
        )


class ChannelViewersResourceWithStreamingResponse:
    def __init__(self, channel_viewers: ChannelViewersResource) -> None:
        self._channel_viewers = channel_viewers

        self.invite = to_streamed_response_wrapper(
            channel_viewers.invite,
        )
        self.delete = to_streamed_response_wrapper(
            channel_viewers.delete,
        )
        self.invite_csv = to_streamed_response_wrapper(
            channel_viewers.invite_csv,
        )
        self.list_subscribers = to_streamed_response_wrapper(
            channel_viewers.list_subscribers,
        )


class AsyncChannelViewersResourceWithStreamingResponse:
    def __init__(self, channel_viewers: AsyncChannelViewersResource) -> None:
        self._channel_viewers = channel_viewers

        self.invite = async_to_streamed_response_wrapper(
            channel_viewers.invite,
        )
        self.delete = async_to_streamed_response_wrapper(
            channel_viewers.delete,
        )
        self.invite_csv = async_to_streamed_response_wrapper(
            channel_viewers.invite_csv,
        )
        self.list_subscribers = async_to_streamed_response_wrapper(
            channel_viewers.list_subscribers,
        )
