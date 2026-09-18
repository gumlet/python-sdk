# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
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
from ..types.live_stream_asset_create_response import LiveStreamAssetCreateResponse
from ..types import (
    live_stream_asset_create_params,
    live_stream_asset_update_params,
    live_stream_asset_filter_params,
    live_stream_asset_upload_params,
)
from ..types.live_stream_asset_update_response import LiveStreamAssetUpdateResponse
from ..types.live_stream_asset_retrieve_status_response import LiveStreamAssetRetrieveStatusResponse
from ..types.live_stream_asset_delete_response import LiveStreamAssetDeleteResponse
from ..types.live_stream_asset_complete_response import LiveStreamAssetCompleteResponse
from ..types.live_stream_asset_filter_response import LiveStreamAssetFilterResponse
from ..types.live_stream_asset_upload_response import LiveStreamAssetUploadResponse
from ..types.live_stream_asset_status_history_response import LiveStreamAssetStatusHistoryResponse

__all__ = ["LiveStreamAssetsResource", "AsyncLiveStreamAssetsResource"]


class LiveStreamAssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveStreamAssetsResourceWithRawResponse:
        return LiveStreamAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveStreamAssetsResourceWithStreamingResponse:
        return LiveStreamAssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        live_source_id: str,
        resolution: str,
        title: str | Omit = omit,
        mp4_access: bool | Omit = omit,
        orientation: Literal["landscape", "potrait"] | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetCreateResponse:
        """
        A live asset refers to a media content/video that is live-streamed through Gumlet. This endpoint creates a live streaming asset allowing users to live stream a video that will be pushed to Gumlet.

        Args:
            live_source_id: Gumlet live video source/collection id.
            resolution: Required resolutions in HLS delivery format for live stream. Can be an array of string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio.
            title: Your live stream asset title
            mp4_access: Creates <code>MP4</code> version for download purpose.
            orientation: Body parameter.
            start_at: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetCreateResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.create(
                live_source_id="",
                resolution="",
            )
            ```
        """
        return self._post(
            "/video/live/assets",
            body=maybe_transform(
                {
                    "live_source_id": live_source_id,
                    "resolution": resolution,
                    "title": title,
                    "mp4_access": mp4_access,
                    "orientation": orientation,
                    "start_at": start_at,
                },
                live_stream_asset_create_params.LiveStreamAssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetCreateResponse,
        )

    def update(
        self,
        *,
        live_asset_id: str,
        title: str | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetUpdateResponse:
        """
        A live asset refers to a media content/video that is live-streamed through Gumlet. This endpoint allows user to update a live streaming asset.

        Args:
            live_asset_id: Gumlet live video asset id.
            title: Your live stream asset title
            start_at: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetUpdateResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.update(
                live_asset_id="",
            )
            ```
        """
        return self._post(
            "/video/live/assets/update",
            body=maybe_transform(
                {
                    "live_asset_id": live_asset_id,
                    "title": title,
                    "start_at": start_at,
                },
                live_stream_asset_update_params.LiveStreamAssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetUpdateResponse,
        )

    def retrieve_status(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetRetrieveStatusResponse:
        """
        This endpoint retrieves the details of a live video asset that has previously been created.

        Args:
            live_asset_id: An live asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetRetrieveStatusResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.retrieve_status(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return self._get(
            path_template("/video/live/assets/{live_asset_id}", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetRetrieveStatusResponse,
        )

    def delete(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetDeleteResponse:
        """
        This endpoint removes a live asset given its unique live asset id. The live asset will be removed from storage as well, associated URLs will be inaccessible.

        Args:
            live_asset_id: Live asset id of the live asset which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetDeleteResponse: 204

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.delete(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return self._delete(
            path_template("/video/live/assets/{live_asset_id}", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetDeleteResponse,
        )

    def complete(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetCompleteResponse:
        """
        This endpoint allows marking live assets complete. Once the live asset is marked complete, it can no longer be used to ingest the live stream on Gumlet.

        Args:
            live_asset_id: Live asset id of the live stream which needs to be completed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetCompleteResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.complete(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return self._post(
            path_template("/video/live/assets/{live_asset_id}/complete", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetCompleteResponse,
        )

    def filter(
        self,
        live_source_id: str,
        *,
        status: str | Omit = omit,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetFilterResponse:
        """
        This endpoint lists live assets on the basis of `status` for the given `live_source_id`.

        Args:
            live_source_id: Gumlet live source/collection id.
            status: To filter live assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `created`, `active`, `complete`, `disconnected`, `errored`, and `deleted`.
            offset: Offset value for a paginated list of assets.
            size: Page size for the paginated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetFilterResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.filter(
                live_source_id="liveSourceId",
            )
            ```
        """
        if live_source_id is None or (isinstance(live_source_id, str) and not live_source_id):
            raise ValueError(f"Expected a non-empty value for `live_source_id` but received {live_source_id!r}")
        return self._get(
            path_template("/video/live/assets/list/{live_source_id}", **{"live_source_id": live_source_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"status": status, "offset": offset, "size": size},
                    live_stream_asset_filter_params.LiveStreamAssetFilterParams,
                ),
            ),
            cast_to=LiveStreamAssetFilterResponse,
        )

    def start(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Start a live stream.

        Args:
            live_asset_id: List asset id for which the stream needs to start.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Example:
            ```python
            client.live_stream_assets.start(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/video/live/assets/{live_asset_id}/start", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload(
        self,
        *,
        live_asset_id: str,
        statuses: Union[List[Literal["preparing", "disconnected", "end"]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetUploadResponse:
        """
        Generate presigned upload URLs for live stream thumbnails. Supported thumbnail states are `preparing`, `disconnected`, and `end`.

        Args:
            live_asset_id: Gumlet live video asset id.
            statuses: Thumbnail states to upload. You can send an array or a comma-separated string.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetUploadResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.upload(
                live_asset_id="68c406b147f9ad0c0d584ce2",
                statuses="preparing",
            )
            ```
        """
        return self._post(
            "/video/live/assets/thumbnail/upload",
            body=maybe_transform(
                {
                    "live_asset_id": live_asset_id,
                    "statuses": statuses,
                },
                live_stream_asset_upload_params.LiveStreamAssetUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetUploadResponse,
        )

    def status_history(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetStatusHistoryResponse:
        """
        This endpoint retrieves the history of a live video asset that has previously been created.

        Args:
            live_asset_id: An live asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetStatusHistoryResponse: 200

        Example:
            ```python
            live_stream_asset = client.live_stream_assets.status_history(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return self._get(
            path_template("/video/live/assets/{live_asset_id}/history", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetStatusHistoryResponse,
        )


class AsyncLiveStreamAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveStreamAssetsResourceWithRawResponse:
        return AsyncLiveStreamAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveStreamAssetsResourceWithStreamingResponse:
        return AsyncLiveStreamAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        live_source_id: str,
        resolution: str,
        title: str | Omit = omit,
        mp4_access: bool | Omit = omit,
        orientation: Literal["landscape", "potrait"] | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetCreateResponse:
        """
        A live asset refers to a media content/video that is live-streamed through Gumlet. This endpoint creates a live streaming asset allowing users to live stream a video that will be pushed to Gumlet.

        Args:
            live_source_id: Gumlet live video source/collection id.
            resolution: Required resolutions in HLS delivery format for live stream. Can be an array of string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio.
            title: Your live stream asset title
            mp4_access: Creates <code>MP4</code> version for download purpose.
            orientation: Body parameter.
            start_at: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetCreateResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.create(
                live_source_id="",
                resolution="",
            )
            ```
        """
        return await self._post(
            "/video/live/assets",
            body=await async_maybe_transform(
                {
                    "live_source_id": live_source_id,
                    "resolution": resolution,
                    "title": title,
                    "mp4_access": mp4_access,
                    "orientation": orientation,
                    "start_at": start_at,
                },
                live_stream_asset_create_params.LiveStreamAssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetCreateResponse,
        )

    async def update(
        self,
        *,
        live_asset_id: str,
        title: str | Omit = omit,
        start_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetUpdateResponse:
        """
        A live asset refers to a media content/video that is live-streamed through Gumlet. This endpoint allows user to update a live streaming asset.

        Args:
            live_asset_id: Gumlet live video asset id.
            title: Your live stream asset title
            start_at: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetUpdateResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.update(
                live_asset_id="",
            )
            ```
        """
        return await self._post(
            "/video/live/assets/update",
            body=await async_maybe_transform(
                {
                    "live_asset_id": live_asset_id,
                    "title": title,
                    "start_at": start_at,
                },
                live_stream_asset_update_params.LiveStreamAssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetUpdateResponse,
        )

    async def retrieve_status(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetRetrieveStatusResponse:
        """
        This endpoint retrieves the details of a live video asset that has previously been created.

        Args:
            live_asset_id: An live asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetRetrieveStatusResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.retrieve_status(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return await self._get(
            path_template("/video/live/assets/{live_asset_id}", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetRetrieveStatusResponse,
        )

    async def delete(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetDeleteResponse:
        """
        This endpoint removes a live asset given its unique live asset id. The live asset will be removed from storage as well, associated URLs will be inaccessible.

        Args:
            live_asset_id: Live asset id of the live asset which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetDeleteResponse: 204

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.delete(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return await self._delete(
            path_template("/video/live/assets/{live_asset_id}", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetDeleteResponse,
        )

    async def complete(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetCompleteResponse:
        """
        This endpoint allows marking live assets complete. Once the live asset is marked complete, it can no longer be used to ingest the live stream on Gumlet.

        Args:
            live_asset_id: Live asset id of the live stream which needs to be completed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetCompleteResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.complete(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return await self._post(
            path_template("/video/live/assets/{live_asset_id}/complete", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetCompleteResponse,
        )

    async def filter(
        self,
        live_source_id: str,
        *,
        status: str | Omit = omit,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetFilterResponse:
        """
        This endpoint lists live assets on the basis of `status` for the given `live_source_id`.

        Args:
            live_source_id: Gumlet live source/collection id.
            status: To filter live assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `created`, `active`, `complete`, `disconnected`, `errored`, and `deleted`.
            offset: Offset value for a paginated list of assets.
            size: Page size for the paginated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetFilterResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.filter(
                live_source_id="liveSourceId",
            )
            ```
        """
        if live_source_id is None or (isinstance(live_source_id, str) and not live_source_id):
            raise ValueError(f"Expected a non-empty value for `live_source_id` but received {live_source_id!r}")
        return await self._get(
            path_template("/video/live/assets/list/{live_source_id}", **{"live_source_id": live_source_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status, "offset": offset, "size": size},
                    live_stream_asset_filter_params.LiveStreamAssetFilterParams,
                ),
            ),
            cast_to=LiveStreamAssetFilterResponse,
        )

    async def start(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Start a live stream.

        Args:
            live_asset_id: List asset id for which the stream needs to start.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Example:
            ```python
            await client.live_stream_assets.start(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/video/live/assets/{live_asset_id}/start", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload(
        self,
        *,
        live_asset_id: str,
        statuses: Union[List[Literal["preparing", "disconnected", "end"]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetUploadResponse:
        """
        Generate presigned upload URLs for live stream thumbnails. Supported thumbnail states are `preparing`, `disconnected`, and `end`.

        Args:
            live_asset_id: Gumlet live video asset id.
            statuses: Thumbnail states to upload. You can send an array or a comma-separated string.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetUploadResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.upload(
                live_asset_id="68c406b147f9ad0c0d584ce2",
                statuses="preparing",
            )
            ```
        """
        return await self._post(
            "/video/live/assets/thumbnail/upload",
            body=await async_maybe_transform(
                {
                    "live_asset_id": live_asset_id,
                    "statuses": statuses,
                },
                live_stream_asset_upload_params.LiveStreamAssetUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetUploadResponse,
        )

    async def status_history(
        self,
        live_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAssetStatusHistoryResponse:
        """
        This endpoint retrieves the history of a live video asset that has previously been created.

        Args:
            live_asset_id: An live asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAssetStatusHistoryResponse: 200

        Example:
            ```python
            live_stream_asset = await client.live_stream_assets.status_history(
                live_asset_id="liveAssetId",
            )
            ```
        """
        if live_asset_id is None or (isinstance(live_asset_id, str) and not live_asset_id):
            raise ValueError(f"Expected a non-empty value for `live_asset_id` but received {live_asset_id!r}")
        return await self._get(
            path_template("/video/live/assets/{live_asset_id}/history", **{"live_asset_id": live_asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAssetStatusHistoryResponse,
        )


class LiveStreamAssetsResourceWithRawResponse:
    def __init__(self, live_stream_assets: LiveStreamAssetsResource) -> None:
        self._live_stream_assets = live_stream_assets

        self.create = to_raw_response_wrapper(
            live_stream_assets.create,
        )
        self.update = to_raw_response_wrapper(
            live_stream_assets.update,
        )
        self.retrieve_status = to_raw_response_wrapper(
            live_stream_assets.retrieve_status,
        )
        self.delete = to_raw_response_wrapper(
            live_stream_assets.delete,
        )
        self.complete = to_raw_response_wrapper(
            live_stream_assets.complete,
        )
        self.filter = to_raw_response_wrapper(
            live_stream_assets.filter,
        )
        self.start = to_raw_response_wrapper(
            live_stream_assets.start,
        )
        self.upload = to_raw_response_wrapper(
            live_stream_assets.upload,
        )
        self.status_history = to_raw_response_wrapper(
            live_stream_assets.status_history,
        )


class AsyncLiveStreamAssetsResourceWithRawResponse:
    def __init__(self, live_stream_assets: AsyncLiveStreamAssetsResource) -> None:
        self._live_stream_assets = live_stream_assets

        self.create = async_to_raw_response_wrapper(
            live_stream_assets.create,
        )
        self.update = async_to_raw_response_wrapper(
            live_stream_assets.update,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            live_stream_assets.retrieve_status,
        )
        self.delete = async_to_raw_response_wrapper(
            live_stream_assets.delete,
        )
        self.complete = async_to_raw_response_wrapper(
            live_stream_assets.complete,
        )
        self.filter = async_to_raw_response_wrapper(
            live_stream_assets.filter,
        )
        self.start = async_to_raw_response_wrapper(
            live_stream_assets.start,
        )
        self.upload = async_to_raw_response_wrapper(
            live_stream_assets.upload,
        )
        self.status_history = async_to_raw_response_wrapper(
            live_stream_assets.status_history,
        )


class LiveStreamAssetsResourceWithStreamingResponse:
    def __init__(self, live_stream_assets: LiveStreamAssetsResource) -> None:
        self._live_stream_assets = live_stream_assets

        self.create = to_streamed_response_wrapper(
            live_stream_assets.create,
        )
        self.update = to_streamed_response_wrapper(
            live_stream_assets.update,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            live_stream_assets.retrieve_status,
        )
        self.delete = to_streamed_response_wrapper(
            live_stream_assets.delete,
        )
        self.complete = to_streamed_response_wrapper(
            live_stream_assets.complete,
        )
        self.filter = to_streamed_response_wrapper(
            live_stream_assets.filter,
        )
        self.start = to_streamed_response_wrapper(
            live_stream_assets.start,
        )
        self.upload = to_streamed_response_wrapper(
            live_stream_assets.upload,
        )
        self.status_history = to_streamed_response_wrapper(
            live_stream_assets.status_history,
        )


class AsyncLiveStreamAssetsResourceWithStreamingResponse:
    def __init__(self, live_stream_assets: AsyncLiveStreamAssetsResource) -> None:
        self._live_stream_assets = live_stream_assets

        self.create = async_to_streamed_response_wrapper(
            live_stream_assets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            live_stream_assets.update,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            live_stream_assets.retrieve_status,
        )
        self.delete = async_to_streamed_response_wrapper(
            live_stream_assets.delete,
        )
        self.complete = async_to_streamed_response_wrapper(
            live_stream_assets.complete,
        )
        self.filter = async_to_streamed_response_wrapper(
            live_stream_assets.filter,
        )
        self.start = async_to_streamed_response_wrapper(
            live_stream_assets.start,
        )
        self.upload = async_to_streamed_response_wrapper(
            live_stream_assets.upload,
        )
        self.status_history = async_to_streamed_response_wrapper(
            live_stream_assets.status_history,
        )
