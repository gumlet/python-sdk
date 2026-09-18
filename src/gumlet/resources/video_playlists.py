# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable
from typing_extensions import Literal, overload
from .._types import SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform, required_args
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.video_playlist_create_response import VideoPlaylistCreateResponse
from ..types import (
    video_playlist_create_params,
    video_playlist_list_all_params,
    video_playlist_create_asset_params,
    video_playlist_delete_asset_params,
    video_playlist_update_params,
    video_playlist_list_assets_params,
    video_playlist_reorder_asset_params,
)
from ..types.video_playlist_list_all_response import VideoPlaylistListAllResponse
from ..types.video_playlist_create_asset_response import VideoPlaylistCreateAssetResponse
from ..types.video_playlist_delete_asset_response import VideoPlaylistDeleteAssetResponse
from ..types.video_playlist_update_response import VideoPlaylistUpdateResponse
from ..types.video_playlist_list_assets_response import VideoPlaylistListAssetsResponse
from ..types.video_playlist_reorder_asset_response import VideoPlaylistReorderAssetResponse

__all__ = ["VideoPlaylistsResource", "AsyncVideoPlaylistsResource"]


class VideoPlaylistsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoPlaylistsResourceWithRawResponse:
        return VideoPlaylistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoPlaylistsResourceWithStreamingResponse:
        return VideoPlaylistsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_id: str,
        title: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistCreateResponse:
        """
        Create new playlist inside video wprkspace

        Args:
            collection_id: Body parameter.
            title: Body parameter.
            description: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistCreateResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.create(
                collection_id="{{video-source-id}}",
                title="Playlist-Title",
                description="This is description for playlist.",
            )
            ```
        """
        return self._post(
            "/video/playlist",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "title": title,
                    "description": description,
                },
                video_playlist_create_params.VideoPlaylistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistCreateResponse,
        )

    def list_all(
        self,
        *,
        collection_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistListAllResponse:
        """
        Get all playlists for given workspace

        Args:
            collection_id: Video Collection ID
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistListAllResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.list_all()
            ```
        """
        return self._get(
            "/video/playlist",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"collection_id": collection_id}, video_playlist_list_all_params.VideoPlaylistListAllParams
                ),
            ),
            cast_to=VideoPlaylistListAllResponse,
        )

    def create_asset(
        self,
        playlist_id: str,
        *,
        asset_list: Iterable[video_playlist_create_asset_params.AssetList],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistCreateAssetResponse:
        """
        This operation adds a single asset or a list of assets to a playlist.

        Args:
            playlist_id: Playlist ID in which the asset needs to be added.
            asset_list: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistCreateAssetResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.create_asset(
                playlist_id="playlistId",
                asset_list=[
                    {"asset_id": "6508790283e4d60611846790"},
                    {"position": 1, "asset_id": "650878f883e4d6061184677d"},
                    {"asset_id": "650878de83e4d6061184676a"},
                    {"position": 2, "asset_id": "650878d883e4d60611846757"},
                    {"position": 3, "asset_id": "65578dd87eebc22dcdd549a2"},
                ],
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._post(
            path_template("/video/playlist/{playlist_id}/asset", **{"playlist_id": playlist_id}),
            body=maybe_transform(
                {"asset_list": asset_list},
                video_playlist_create_asset_params.VideoPlaylistCreateAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistCreateAssetResponse,
        )

    def delete_asset(
        self,
        playlist_id: str,
        *,
        delete_list: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistDeleteAssetResponse:
        """
        Removed an asset or list of assets from a given playlist.

        Args:
            playlist_id: Playlist ID that is to be deleted.
            delete_list: Array of video asset ids.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistDeleteAssetResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.delete_asset(
                playlist_id="playlistId",
                delete_list=["6508790783e4d606118467a3"],
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._delete(
            path_template("/video/playlist/{playlist_id}/asset", **{"playlist_id": playlist_id}),
            body=maybe_transform(
                {"delete_list": delete_list},
                video_playlist_delete_asset_params.VideoPlaylistDeleteAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistDeleteAssetResponse,
        )

    def update(
        self,
        playlist_id: str,
        *,
        title: str | Omit = omit,
        description: str | Omit = omit,
        position: int | Omit = omit,
        player_config: video_playlist_update_params.PlayerConfig | Omit = omit,
        channel_visibility: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistUpdateResponse:
        """
        This endpoint allows you to update playlist name, channel visibility, or playlist order on a channel page.

        Args:
            playlist_id: ID for the playlist to update.
            title: Body parameter.
            description: Body parameter.
            position: Playlists have order in which they will be shown on the channel page.
            player_config: Configure player settings for this playlist, it overrides the setting set on collection.
            channel_visibility: If true then playlist will be visible on channel page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistUpdateResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.update(
                playlist_id="playlistId",
                title="Playlist-Title-Updated",
                description="This is updated description",
                position=6,
                player_config={
                    "preload": True,
                    "autoplay": False,
                    "disable_seek": True,
                    "disable_player_controls": False,
                    "powered_by_gumlet_overlay": False,
                    "allow_drm_protected_videos": False,
                    "loop": False,
                    "player_color": "#6658ea",
                    "include_seo": True,
                    "subtitle_enabled": True,
                    "pixel_tags": {},
                    "logo_width": 51,
                    "logo_height": 100,
                    "dynamic_watermark": False,
                    "watermark_font_size": 1,
                    "watermark_font_color": "#ff0000",
                    "watermark_bg_color": "transparent",
                    "watermark_interval": 1000,
                },
                channel_visibility=False,
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._post(
            path_template("/video/playlist/{playlist_id}", **{"playlist_id": playlist_id}),
            body=maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "position": position,
                    "player_config": player_config,
                    "channel_visibility": channel_visibility,
                },
                video_playlist_update_params.VideoPlaylistUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistUpdateResponse,
        )

    def delete(
        self,
        playlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes this playlist.

        Args:
            playlist_id: Playlist ID that is to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Example:
            ```python
            client.video_playlists.delete(
                playlist_id="playlistId",
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/video/playlist/{playlist_id}", **{"playlist_id": playlist_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_assets(
        self,
        playlist_id: str,
        *,
        sort_by: str | Omit = omit,
        sort_order: int | Omit = omit,
        page_number: int | Omit = omit,
        page_size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistListAssetsResponse:
        """
        Get a list of all assets inside playlist. You can choose in which order are assets returned.

        Args:
            playlist_id: ID of playlist in which you need to list assets.
            sort_by: Optional, if sort_by is set to asset_title it will sorted by title name. Otherwise order in which user added the assets in playlist.
            sort_order: -1 or 1
            page_number: Optional, Minimun 1
            page_size: Optional, Minimun 10
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistListAssetsResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.list_assets(
                playlist_id="playlistId",
                sort_order=1,
                page_number=1,
                page_size="10",
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._get(
            path_template("/video/playlist/{playlist_id}/assets", **{"playlist_id": playlist_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"sort_by": sort_by, "sort_order": sort_order, "page_number": page_number, "page_size": page_size},
                    video_playlist_list_assets_params.VideoPlaylistListAssetsParams,
                ),
            ),
            cast_to=VideoPlaylistListAssetsResponse,
        )

    @overload
    def reorder_asset(
        self,
        playlist_id: str,
        *,
        asset_id: str,
        page_number: int,
        page_size: int,
        asset_position: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistReorderAssetResponse: ...

    @overload
    def reorder_asset(
        self,
        playlist_id: str,
        *,
        sort_by: Literal["title", "created_at"],
        sort_order: Literal["asc", "desc"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistReorderAssetResponse: ...

    @required_args(["asset_id", "asset_position", "page_number", "page_size"], ["sort_by", "sort_order"])
    def reorder_asset(
        self,
        playlist_id: str,
        *,
        asset_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        asset_position: int | Omit = omit,
        sort_by: Literal["title", "created_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistReorderAssetResponse:
        """
        Reorder videos inside a playlist either by moving a single asset to a position or by sorting the playlist by title or created date.

        Args:
            playlist_id: Playlist id.
            asset_id: Asset id to move.
            page_number: Current playlist page number.
            page_size: Playlist page size used by the caller.
            asset_position: Zero-based position inside the provided page.
            sort_by: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistReorderAssetResponse: 200

        Example:
            ```python
            video_playlist = client.video_playlists.reorder_asset(
                playlist_id="playlistId",
                asset_id="6e82bf783e88be000ab45ed2",
                page_number=1,
                page_size=10,
                asset_position=0,
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._post(
            path_template("/video/playlists/{playlist_id}/reorder", **{"playlist_id": playlist_id}),
            body=maybe_transform(
                {
                    "asset_id": asset_id,
                    "page_number": page_number,
                    "page_size": page_size,
                    "asset_position": asset_position,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                video_playlist_reorder_asset_params.VideoPlaylistReorderAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistReorderAssetResponse,
        )


class AsyncVideoPlaylistsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoPlaylistsResourceWithRawResponse:
        return AsyncVideoPlaylistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoPlaylistsResourceWithStreamingResponse:
        return AsyncVideoPlaylistsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_id: str,
        title: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistCreateResponse:
        """
        Create new playlist inside video wprkspace

        Args:
            collection_id: Body parameter.
            title: Body parameter.
            description: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistCreateResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.create(
                collection_id="{{video-source-id}}",
                title="Playlist-Title",
                description="This is description for playlist.",
            )
            ```
        """
        return await self._post(
            "/video/playlist",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "title": title,
                    "description": description,
                },
                video_playlist_create_params.VideoPlaylistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistCreateResponse,
        )

    async def list_all(
        self,
        *,
        collection_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistListAllResponse:
        """
        Get all playlists for given workspace

        Args:
            collection_id: Video Collection ID
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistListAllResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.list_all()
            ```
        """
        return await self._get(
            "/video/playlist",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"collection_id": collection_id}, video_playlist_list_all_params.VideoPlaylistListAllParams
                ),
            ),
            cast_to=VideoPlaylistListAllResponse,
        )

    async def create_asset(
        self,
        playlist_id: str,
        *,
        asset_list: Iterable[video_playlist_create_asset_params.AssetList],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistCreateAssetResponse:
        """
        This operation adds a single asset or a list of assets to a playlist.

        Args:
            playlist_id: Playlist ID in which the asset needs to be added.
            asset_list: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistCreateAssetResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.create_asset(
                playlist_id="playlistId",
                asset_list=[
                    {"asset_id": "6508790283e4d60611846790"},
                    {"position": 1, "asset_id": "650878f883e4d6061184677d"},
                    {"asset_id": "650878de83e4d6061184676a"},
                    {"position": 2, "asset_id": "650878d883e4d60611846757"},
                    {"position": 3, "asset_id": "65578dd87eebc22dcdd549a2"},
                ],
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._post(
            path_template("/video/playlist/{playlist_id}/asset", **{"playlist_id": playlist_id}),
            body=await async_maybe_transform(
                {"asset_list": asset_list},
                video_playlist_create_asset_params.VideoPlaylistCreateAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistCreateAssetResponse,
        )

    async def delete_asset(
        self,
        playlist_id: str,
        *,
        delete_list: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistDeleteAssetResponse:
        """
        Removed an asset or list of assets from a given playlist.

        Args:
            playlist_id: Playlist ID that is to be deleted.
            delete_list: Array of video asset ids.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistDeleteAssetResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.delete_asset(
                playlist_id="playlistId",
                delete_list=["6508790783e4d606118467a3"],
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._delete(
            path_template("/video/playlist/{playlist_id}/asset", **{"playlist_id": playlist_id}),
            body=await async_maybe_transform(
                {"delete_list": delete_list},
                video_playlist_delete_asset_params.VideoPlaylistDeleteAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistDeleteAssetResponse,
        )

    async def update(
        self,
        playlist_id: str,
        *,
        title: str | Omit = omit,
        description: str | Omit = omit,
        position: int | Omit = omit,
        player_config: video_playlist_update_params.PlayerConfig | Omit = omit,
        channel_visibility: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistUpdateResponse:
        """
        This endpoint allows you to update playlist name, channel visibility, or playlist order on a channel page.

        Args:
            playlist_id: ID for the playlist to update.
            title: Body parameter.
            description: Body parameter.
            position: Playlists have order in which they will be shown on the channel page.
            player_config: Configure player settings for this playlist, it overrides the setting set on collection.
            channel_visibility: If true then playlist will be visible on channel page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistUpdateResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.update(
                playlist_id="playlistId",
                title="Playlist-Title-Updated",
                description="This is updated description",
                position=6,
                player_config={
                    "preload": True,
                    "autoplay": False,
                    "disable_seek": True,
                    "disable_player_controls": False,
                    "powered_by_gumlet_overlay": False,
                    "allow_drm_protected_videos": False,
                    "loop": False,
                    "player_color": "#6658ea",
                    "include_seo": True,
                    "subtitle_enabled": True,
                    "pixel_tags": {},
                    "logo_width": 51,
                    "logo_height": 100,
                    "dynamic_watermark": False,
                    "watermark_font_size": 1,
                    "watermark_font_color": "#ff0000",
                    "watermark_bg_color": "transparent",
                    "watermark_interval": 1000,
                },
                channel_visibility=False,
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._post(
            path_template("/video/playlist/{playlist_id}", **{"playlist_id": playlist_id}),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "position": position,
                    "player_config": player_config,
                    "channel_visibility": channel_visibility,
                },
                video_playlist_update_params.VideoPlaylistUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistUpdateResponse,
        )

    async def delete(
        self,
        playlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes this playlist.

        Args:
            playlist_id: Playlist ID that is to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Example:
            ```python
            await client.video_playlists.delete(
                playlist_id="playlistId",
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/video/playlist/{playlist_id}", **{"playlist_id": playlist_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_assets(
        self,
        playlist_id: str,
        *,
        sort_by: str | Omit = omit,
        sort_order: int | Omit = omit,
        page_number: int | Omit = omit,
        page_size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistListAssetsResponse:
        """
        Get a list of all assets inside playlist. You can choose in which order are assets returned.

        Args:
            playlist_id: ID of playlist in which you need to list assets.
            sort_by: Optional, if sort_by is set to asset_title it will sorted by title name. Otherwise order in which user added the assets in playlist.
            sort_order: -1 or 1
            page_number: Optional, Minimun 1
            page_size: Optional, Minimun 10
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistListAssetsResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.list_assets(
                playlist_id="playlistId",
                sort_order=1,
                page_number=1,
                page_size="10",
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._get(
            path_template("/video/playlist/{playlist_id}/assets", **{"playlist_id": playlist_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"sort_by": sort_by, "sort_order": sort_order, "page_number": page_number, "page_size": page_size},
                    video_playlist_list_assets_params.VideoPlaylistListAssetsParams,
                ),
            ),
            cast_to=VideoPlaylistListAssetsResponse,
        )

    @overload
    async def reorder_asset(
        self,
        playlist_id: str,
        *,
        asset_id: str,
        page_number: int,
        page_size: int,
        asset_position: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistReorderAssetResponse: ...

    @overload
    async def reorder_asset(
        self,
        playlist_id: str,
        *,
        sort_by: Literal["title", "created_at"],
        sort_order: Literal["asc", "desc"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistReorderAssetResponse: ...

    @required_args(["asset_id", "asset_position", "page_number", "page_size"], ["sort_by", "sort_order"])
    async def reorder_asset(
        self,
        playlist_id: str,
        *,
        asset_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        asset_position: int | Omit = omit,
        sort_by: Literal["title", "created_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoPlaylistReorderAssetResponse:
        """
        Reorder videos inside a playlist either by moving a single asset to a position or by sorting the playlist by title or created date.

        Args:
            playlist_id: Playlist id.
            asset_id: Asset id to move.
            page_number: Current playlist page number.
            page_size: Playlist page size used by the caller.
            asset_position: Zero-based position inside the provided page.
            sort_by: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoPlaylistReorderAssetResponse: 200

        Example:
            ```python
            video_playlist = await client.video_playlists.reorder_asset(
                playlist_id="playlistId",
                asset_id="6e82bf783e88be000ab45ed2",
                page_number=1,
                page_size=10,
                asset_position=0,
            )
            ```
        """
        if playlist_id is None or (isinstance(playlist_id, str) and not playlist_id):
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._post(
            path_template("/video/playlists/{playlist_id}/reorder", **{"playlist_id": playlist_id}),
            body=await async_maybe_transform(
                {
                    "asset_id": asset_id,
                    "page_number": page_number,
                    "page_size": page_size,
                    "asset_position": asset_position,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                video_playlist_reorder_asset_params.VideoPlaylistReorderAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoPlaylistReorderAssetResponse,
        )


class VideoPlaylistsResourceWithRawResponse:
    def __init__(self, video_playlists: VideoPlaylistsResource) -> None:
        self._video_playlists = video_playlists

        self.create = to_raw_response_wrapper(
            video_playlists.create,
        )
        self.list_all = to_raw_response_wrapper(
            video_playlists.list_all,
        )
        self.create_asset = to_raw_response_wrapper(
            video_playlists.create_asset,
        )
        self.delete_asset = to_raw_response_wrapper(
            video_playlists.delete_asset,
        )
        self.update = to_raw_response_wrapper(
            video_playlists.update,
        )
        self.delete = to_raw_response_wrapper(
            video_playlists.delete,
        )
        self.list_assets = to_raw_response_wrapper(
            video_playlists.list_assets,
        )
        self.reorder_asset = to_raw_response_wrapper(
            video_playlists.reorder_asset,
        )


class AsyncVideoPlaylistsResourceWithRawResponse:
    def __init__(self, video_playlists: AsyncVideoPlaylistsResource) -> None:
        self._video_playlists = video_playlists

        self.create = async_to_raw_response_wrapper(
            video_playlists.create,
        )
        self.list_all = async_to_raw_response_wrapper(
            video_playlists.list_all,
        )
        self.create_asset = async_to_raw_response_wrapper(
            video_playlists.create_asset,
        )
        self.delete_asset = async_to_raw_response_wrapper(
            video_playlists.delete_asset,
        )
        self.update = async_to_raw_response_wrapper(
            video_playlists.update,
        )
        self.delete = async_to_raw_response_wrapper(
            video_playlists.delete,
        )
        self.list_assets = async_to_raw_response_wrapper(
            video_playlists.list_assets,
        )
        self.reorder_asset = async_to_raw_response_wrapper(
            video_playlists.reorder_asset,
        )


class VideoPlaylistsResourceWithStreamingResponse:
    def __init__(self, video_playlists: VideoPlaylistsResource) -> None:
        self._video_playlists = video_playlists

        self.create = to_streamed_response_wrapper(
            video_playlists.create,
        )
        self.list_all = to_streamed_response_wrapper(
            video_playlists.list_all,
        )
        self.create_asset = to_streamed_response_wrapper(
            video_playlists.create_asset,
        )
        self.delete_asset = to_streamed_response_wrapper(
            video_playlists.delete_asset,
        )
        self.update = to_streamed_response_wrapper(
            video_playlists.update,
        )
        self.delete = to_streamed_response_wrapper(
            video_playlists.delete,
        )
        self.list_assets = to_streamed_response_wrapper(
            video_playlists.list_assets,
        )
        self.reorder_asset = to_streamed_response_wrapper(
            video_playlists.reorder_asset,
        )


class AsyncVideoPlaylistsResourceWithStreamingResponse:
    def __init__(self, video_playlists: AsyncVideoPlaylistsResource) -> None:
        self._video_playlists = video_playlists

        self.create = async_to_streamed_response_wrapper(
            video_playlists.create,
        )
        self.list_all = async_to_streamed_response_wrapper(
            video_playlists.list_all,
        )
        self.create_asset = async_to_streamed_response_wrapper(
            video_playlists.create_asset,
        )
        self.delete_asset = async_to_streamed_response_wrapper(
            video_playlists.delete_asset,
        )
        self.update = async_to_streamed_response_wrapper(
            video_playlists.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            video_playlists.delete,
        )
        self.list_assets = async_to_streamed_response_wrapper(
            video_playlists.list_assets,
        )
        self.reorder_asset = async_to_streamed_response_wrapper(
            video_playlists.reorder_asset,
        )
