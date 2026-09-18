# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal
from .._types import SequenceNotStr

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
from ..types.video_workspace_list_response import VideoWorkspaceListResponse
from ..types import video_workspace_list_params, video_workspace_create_params, video_workspace_update_params
from ..types.video_workspace_create_response import VideoWorkspaceCreateResponse
from ..types.video_workspace_update_response import VideoWorkspaceUpdateResponse
from ..types.video_workspace_retrieve_response import VideoWorkspaceRetrieveResponse
from ..types.video_workspace_delete_response import VideoWorkspaceDeleteResponse

__all__ = ["VideoWorkspacesResource", "AsyncVideoWorkspacesResource"]


class VideoWorkspacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoWorkspacesResourceWithRawResponse:
        return VideoWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoWorkspacesResourceWithStreamingResponse:
        return VideoWorkspacesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        offset: str | Omit = omit,
        size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceListResponse:
        """
        This endpoint list video workspace which are assigned to the user or token.

        Args:
            offset: Number of workspaces to skip. For example if you need to list 11 to 20th workspaces, pass offset as 10 and size as 10.
            size: Number of workspace to return in single response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceListResponse: 200

        Example:
            ```python
            video_workspace = client.video_workspaces.list(
                offset="0",
                size="10",
            )
            ```
        """
        return self._get(
            "/video/workspaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"offset": offset, "size": size}, video_workspace_list_params.VideoWorkspaceListParams
                ),
            ),
            cast_to=VideoWorkspaceListResponse,
        )

    def create(
        self,
        *,
        name: str,
        type: Literal[
            "proxy",
            "direct-upload",
            "webfolder",
            "aws",
            "gcs",
            "dostorage",
            "wasabi",
            "cloudinary",
            "azure",
            "linode",
            "backblaze",
            "cloudflare",
            "zoom",
        ],
        default_profile_id: str | Omit = omit,
        insight_property_id: str | Omit = omit,
        video_protection: video_workspace_create_params.VideoProtection | Omit = omit,
        aws: video_workspace_create_params.Aws | Omit = omit,
        proxy: video_workspace_create_params.Proxy | Omit = omit,
        gcs: video_workspace_create_params.Gcs | Omit = omit,
        dostorage: video_workspace_create_params.Dostorage | Omit = omit,
        wasabi: video_workspace_create_params.Wasabi | Omit = omit,
        cloudinary: video_workspace_create_params.Cloudinary | Omit = omit,
        azure: video_workspace_create_params.Azure | Omit = omit,
        linode: video_workspace_create_params.Linode | Omit = omit,
        backblaze: video_workspace_create_params.Backblaze | Omit = omit,
        cloudflare: video_workspace_create_params.Cloudflare | Omit = omit,
        zoom: video_workspace_create_params.Zoom | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceCreateResponse:
        """
        Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.

        Args:
            name: Specify a text string or identifier for the workspace.
            type: Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.
            default_profile_id: Gumlet provides the functionality of creating multiple video assets using the same set of parameters.
            insight_property_id: The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard.
            video_protection: Gumlet provides multiple options for securing your video playback.
            aws: This is a required field if workspace type is aws.
            proxy: This is a required field if workspace type is proxy.
            gcs: This is a required field if workspace type is gcs.
            dostorage: This is a required field if workspace type is dostorage.
            wasabi: This is a required field if workspace type is wasabi.
            cloudinary: This is a required field if workspace type is cloudinary.
            azure: This is a required field if workspace type is azure.
            linode: This is a required field if workspace type is linode.
            backblaze: This is a required field if workspace type is backblaze.
            cloudflare: This is a required field if workspace type is cloudflare.
            zoom: This is a required field if workspace type is zoom.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceCreateResponse: 200

        Example:
            ```python
            video_workspace = client.video_workspaces.create(
                name="zoom-workspace",
                type="direct-upload",
                zoom={"secret": "yourSecret"},
            )
            ```
        """
        return self._post(
            "/video/workspaces",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "default_profile_id": default_profile_id,
                    "insight_property_id": insight_property_id,
                    "video_protection": video_protection,
                    "aws": aws,
                    "proxy": proxy,
                    "gcs": gcs,
                    "dostorage": dostorage,
                    "wasabi": wasabi,
                    "cloudinary": cloudinary,
                    "azure": azure,
                    "linode": linode,
                    "backblaze": backblaze,
                    "cloudflare": cloudflare,
                    "zoom": zoom,
                },
                video_workspace_create_params.VideoWorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceCreateResponse,
        )

    def update(
        self,
        workspace_id: str,
        *,
        name: str | Omit = omit,
        default_profile_id: str | Omit = omit,
        temp_cname: SequenceNotStr[str] | Omit = omit,
        insight_property_id: str | Omit = omit,
        player_config: video_workspace_update_params.PlayerConfig | Omit = omit,
        video_protection: video_workspace_update_params.VideoProtection | Omit = omit,
        channel_settings: video_workspace_update_params.ChannelSettings | Omit = omit,
        type: Literal[
            "proxy",
            "direct-upload",
            "webfolder",
            "aws",
            "gcs",
            "dostorage",
            "wasabi",
            "cloudinary",
            "azure",
            "linode",
            "backblaze",
            "cloudflare",
            "zoom",
        ]
        | Omit = omit,
        webfolder: video_workspace_update_params.Webfolder | Omit = omit,
        aws: video_workspace_update_params.Aws | Omit = omit,
        proxy: video_workspace_update_params.Proxy | Omit = omit,
        gcs: video_workspace_update_params.Gcs | Omit = omit,
        dostorage: video_workspace_update_params.Dostorage | Omit = omit,
        wasabi: video_workspace_update_params.Wasabi | Omit = omit,
        linode: video_workspace_update_params.Linode | Omit = omit,
        backblaze: video_workspace_update_params.Backblaze | Omit = omit,
        cloudflare: video_workspace_update_params.Cloudflare | Omit = omit,
        cloudinary: video_workspace_update_params.Cloudinary | Omit = omit,
        azure: video_workspace_update_params.Azure | Omit = omit,
        zoom: video_workspace_update_params.Zoom | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceUpdateResponse:
        """
        This endpoint allows users to update video workspace that has previously been created.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            name: video workspace name
            default_profile_id: Gumlet provides the functionality of creating multiple video assets using the same set of parameters.
            temp_cname: cname for channel
            insight_property_id: The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard.
            player_config: Configure player settings for this playlist, it overrides the setting set on workspace.
            video_protection: Gumlet provides multiple options for securing your video playback.
            channel_settings: Configurations to set various channel settings.
            type: Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.
            webfolder: This is a required field if workspace type is webfolder.
            aws: This is a required field if workspace type is aws.
            proxy: This is a required field if workspace type is proxy.
            gcs: This is a required field if workspace type is gcs.
            dostorage: This is a required field if workspace type is dostorage.
            wasabi: This is a required field if workspace type is wasabi.
            linode: This is a required field if workspace type is linode.
            backblaze: This is a required field if workspace type is backblaze.
            cloudflare: This is a required field if workspace type is cloudflare.
            cloudinary: This is a required field if workspace type is cloudinary.
            azure: This is a required field if workspace type is azure.
            zoom: This is a required field if workspace type is zoom.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceUpdateResponse: 200

        Example:
            ```python
            video_workspace = client.video_workspaces.update(
                workspace_id="workspaceId",
                name="awsrename",
                default_profile_id="646df1c9173a4a2fcac180b7",
                type="aws",
                aws={
                    "bucket_name": "my-bucket-test",
                    "bucket_region": "ap-southeast-1",
                    "access_key": "BQUA6QFXVWHAAB6IO2X1",
                    "secret": "aws_secret",
                },
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/video/workspaces/{workspace_id}", **{"workspace_id": workspace_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "default_profile_id": default_profile_id,
                    "temp_cname": temp_cname,
                    "insight_property_id": insight_property_id,
                    "player_config": player_config,
                    "video_protection": video_protection,
                    "channel_settings": channel_settings,
                    "type": type,
                    "webfolder": webfolder,
                    "aws": aws,
                    "proxy": proxy,
                    "gcs": gcs,
                    "dostorage": dostorage,
                    "wasabi": wasabi,
                    "linode": linode,
                    "backblaze": backblaze,
                    "cloudflare": cloudflare,
                    "cloudinary": cloudinary,
                    "azure": azure,
                    "zoom": zoom,
                },
                video_workspace_update_params.VideoWorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceUpdateResponse,
        )

    def retrieve(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceRetrieveResponse:
        """
        This endpoint get all the data of video workspace that has previously been created.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceRetrieveResponse: 200

        Example:
            ```python
            video_workspace = client.video_workspaces.retrieve(
                workspace_id="workspaceId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            path_template("/video/workspaces/{workspace_id}", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceRetrieveResponse,
        )

    def delete(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceDeleteResponse:
        """
        This endpoint removes a video workspace given its unique asset id. All the asset in workspace will be removed from storage as well, associated URLs will be inaccessible.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceDeleteResponse: 200

        Example:
            ```python
            video_workspace = client.video_workspaces.delete(
                workspace_id="workspaceId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._delete(
            path_template("/video/workspaces/{workspace_id}", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceDeleteResponse,
        )


class AsyncVideoWorkspacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoWorkspacesResourceWithRawResponse:
        return AsyncVideoWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoWorkspacesResourceWithStreamingResponse:
        return AsyncVideoWorkspacesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        offset: str | Omit = omit,
        size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceListResponse:
        """
        This endpoint list video workspace which are assigned to the user or token.

        Args:
            offset: Number of workspaces to skip. For example if you need to list 11 to 20th workspaces, pass offset as 10 and size as 10.
            size: Number of workspace to return in single response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceListResponse: 200

        Example:
            ```python
            video_workspace = await client.video_workspaces.list(
                offset="0",
                size="10",
            )
            ```
        """
        return await self._get(
            "/video/workspaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"offset": offset, "size": size}, video_workspace_list_params.VideoWorkspaceListParams
                ),
            ),
            cast_to=VideoWorkspaceListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        type: Literal[
            "proxy",
            "direct-upload",
            "webfolder",
            "aws",
            "gcs",
            "dostorage",
            "wasabi",
            "cloudinary",
            "azure",
            "linode",
            "backblaze",
            "cloudflare",
            "zoom",
        ],
        default_profile_id: str | Omit = omit,
        insight_property_id: str | Omit = omit,
        video_protection: video_workspace_create_params.VideoProtection | Omit = omit,
        aws: video_workspace_create_params.Aws | Omit = omit,
        proxy: video_workspace_create_params.Proxy | Omit = omit,
        gcs: video_workspace_create_params.Gcs | Omit = omit,
        dostorage: video_workspace_create_params.Dostorage | Omit = omit,
        wasabi: video_workspace_create_params.Wasabi | Omit = omit,
        cloudinary: video_workspace_create_params.Cloudinary | Omit = omit,
        azure: video_workspace_create_params.Azure | Omit = omit,
        linode: video_workspace_create_params.Linode | Omit = omit,
        backblaze: video_workspace_create_params.Backblaze | Omit = omit,
        cloudflare: video_workspace_create_params.Cloudflare | Omit = omit,
        zoom: video_workspace_create_params.Zoom | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceCreateResponse:
        """
        Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.

        Args:
            name: Specify a text string or identifier for the workspace.
            type: Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.
            default_profile_id: Gumlet provides the functionality of creating multiple video assets using the same set of parameters.
            insight_property_id: The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard.
            video_protection: Gumlet provides multiple options for securing your video playback.
            aws: This is a required field if workspace type is aws.
            proxy: This is a required field if workspace type is proxy.
            gcs: This is a required field if workspace type is gcs.
            dostorage: This is a required field if workspace type is dostorage.
            wasabi: This is a required field if workspace type is wasabi.
            cloudinary: This is a required field if workspace type is cloudinary.
            azure: This is a required field if workspace type is azure.
            linode: This is a required field if workspace type is linode.
            backblaze: This is a required field if workspace type is backblaze.
            cloudflare: This is a required field if workspace type is cloudflare.
            zoom: This is a required field if workspace type is zoom.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceCreateResponse: 200

        Example:
            ```python
            video_workspace = await client.video_workspaces.create(
                name="zoom-workspace",
                type="direct-upload",
                zoom={"secret": "yourSecret"},
            )
            ```
        """
        return await self._post(
            "/video/workspaces",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "default_profile_id": default_profile_id,
                    "insight_property_id": insight_property_id,
                    "video_protection": video_protection,
                    "aws": aws,
                    "proxy": proxy,
                    "gcs": gcs,
                    "dostorage": dostorage,
                    "wasabi": wasabi,
                    "cloudinary": cloudinary,
                    "azure": azure,
                    "linode": linode,
                    "backblaze": backblaze,
                    "cloudflare": cloudflare,
                    "zoom": zoom,
                },
                video_workspace_create_params.VideoWorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceCreateResponse,
        )

    async def update(
        self,
        workspace_id: str,
        *,
        name: str | Omit = omit,
        default_profile_id: str | Omit = omit,
        temp_cname: SequenceNotStr[str] | Omit = omit,
        insight_property_id: str | Omit = omit,
        player_config: video_workspace_update_params.PlayerConfig | Omit = omit,
        video_protection: video_workspace_update_params.VideoProtection | Omit = omit,
        channel_settings: video_workspace_update_params.ChannelSettings | Omit = omit,
        type: Literal[
            "proxy",
            "direct-upload",
            "webfolder",
            "aws",
            "gcs",
            "dostorage",
            "wasabi",
            "cloudinary",
            "azure",
            "linode",
            "backblaze",
            "cloudflare",
            "zoom",
        ]
        | Omit = omit,
        webfolder: video_workspace_update_params.Webfolder | Omit = omit,
        aws: video_workspace_update_params.Aws | Omit = omit,
        proxy: video_workspace_update_params.Proxy | Omit = omit,
        gcs: video_workspace_update_params.Gcs | Omit = omit,
        dostorage: video_workspace_update_params.Dostorage | Omit = omit,
        wasabi: video_workspace_update_params.Wasabi | Omit = omit,
        linode: video_workspace_update_params.Linode | Omit = omit,
        backblaze: video_workspace_update_params.Backblaze | Omit = omit,
        cloudflare: video_workspace_update_params.Cloudflare | Omit = omit,
        cloudinary: video_workspace_update_params.Cloudinary | Omit = omit,
        azure: video_workspace_update_params.Azure | Omit = omit,
        zoom: video_workspace_update_params.Zoom | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceUpdateResponse:
        """
        This endpoint allows users to update video workspace that has previously been created.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            name: video workspace name
            default_profile_id: Gumlet provides the functionality of creating multiple video assets using the same set of parameters.
            temp_cname: cname for channel
            insight_property_id: The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard.
            player_config: Configure player settings for this playlist, it overrides the setting set on workspace.
            video_protection: Gumlet provides multiple options for securing your video playback.
            channel_settings: Configurations to set various channel settings.
            type: Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.
            webfolder: This is a required field if workspace type is webfolder.
            aws: This is a required field if workspace type is aws.
            proxy: This is a required field if workspace type is proxy.
            gcs: This is a required field if workspace type is gcs.
            dostorage: This is a required field if workspace type is dostorage.
            wasabi: This is a required field if workspace type is wasabi.
            linode: This is a required field if workspace type is linode.
            backblaze: This is a required field if workspace type is backblaze.
            cloudflare: This is a required field if workspace type is cloudflare.
            cloudinary: This is a required field if workspace type is cloudinary.
            azure: This is a required field if workspace type is azure.
            zoom: This is a required field if workspace type is zoom.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceUpdateResponse: 200

        Example:
            ```python
            video_workspace = await client.video_workspaces.update(
                workspace_id="workspaceId",
                name="awsrename",
                default_profile_id="646df1c9173a4a2fcac180b7",
                type="aws",
                aws={
                    "bucket_name": "my-bucket-test",
                    "bucket_region": "ap-southeast-1",
                    "access_key": "BQUA6QFXVWHAAB6IO2X1",
                    "secret": "aws_secret",
                },
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/video/workspaces/{workspace_id}", **{"workspace_id": workspace_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "default_profile_id": default_profile_id,
                    "temp_cname": temp_cname,
                    "insight_property_id": insight_property_id,
                    "player_config": player_config,
                    "video_protection": video_protection,
                    "channel_settings": channel_settings,
                    "type": type,
                    "webfolder": webfolder,
                    "aws": aws,
                    "proxy": proxy,
                    "gcs": gcs,
                    "dostorage": dostorage,
                    "wasabi": wasabi,
                    "linode": linode,
                    "backblaze": backblaze,
                    "cloudflare": cloudflare,
                    "cloudinary": cloudinary,
                    "azure": azure,
                    "zoom": zoom,
                },
                video_workspace_update_params.VideoWorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceUpdateResponse,
        )

    async def retrieve(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceRetrieveResponse:
        """
        This endpoint get all the data of video workspace that has previously been created.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceRetrieveResponse: 200

        Example:
            ```python
            video_workspace = await client.video_workspaces.retrieve(
                workspace_id="workspaceId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            path_template("/video/workspaces/{workspace_id}", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceRetrieveResponse,
        )

    async def delete(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoWorkspaceDeleteResponse:
        """
        This endpoint removes a video workspace given its unique asset id. All the asset in workspace will be removed from storage as well, associated URLs will be inaccessible.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoWorkspaceDeleteResponse: 200

        Example:
            ```python
            video_workspace = await client.video_workspaces.delete(
                workspace_id="workspaceId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._delete(
            path_template("/video/workspaces/{workspace_id}", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoWorkspaceDeleteResponse,
        )


class VideoWorkspacesResourceWithRawResponse:
    def __init__(self, video_workspaces: VideoWorkspacesResource) -> None:
        self._video_workspaces = video_workspaces

        self.list = to_raw_response_wrapper(
            video_workspaces.list,
        )
        self.create = to_raw_response_wrapper(
            video_workspaces.create,
        )
        self.update = to_raw_response_wrapper(
            video_workspaces.update,
        )
        self.retrieve = to_raw_response_wrapper(
            video_workspaces.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            video_workspaces.delete,
        )


class AsyncVideoWorkspacesResourceWithRawResponse:
    def __init__(self, video_workspaces: AsyncVideoWorkspacesResource) -> None:
        self._video_workspaces = video_workspaces

        self.list = async_to_raw_response_wrapper(
            video_workspaces.list,
        )
        self.create = async_to_raw_response_wrapper(
            video_workspaces.create,
        )
        self.update = async_to_raw_response_wrapper(
            video_workspaces.update,
        )
        self.retrieve = async_to_raw_response_wrapper(
            video_workspaces.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            video_workspaces.delete,
        )


class VideoWorkspacesResourceWithStreamingResponse:
    def __init__(self, video_workspaces: VideoWorkspacesResource) -> None:
        self._video_workspaces = video_workspaces

        self.list = to_streamed_response_wrapper(
            video_workspaces.list,
        )
        self.create = to_streamed_response_wrapper(
            video_workspaces.create,
        )
        self.update = to_streamed_response_wrapper(
            video_workspaces.update,
        )
        self.retrieve = to_streamed_response_wrapper(
            video_workspaces.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            video_workspaces.delete,
        )


class AsyncVideoWorkspacesResourceWithStreamingResponse:
    def __init__(self, video_workspaces: AsyncVideoWorkspacesResource) -> None:
        self._video_workspaces = video_workspaces

        self.list = async_to_streamed_response_wrapper(
            video_workspaces.list,
        )
        self.create = async_to_streamed_response_wrapper(
            video_workspaces.create,
        )
        self.update = async_to_streamed_response_wrapper(
            video_workspaces.update,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            video_workspaces.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            video_workspaces.delete,
        )
