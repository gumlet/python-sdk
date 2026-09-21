# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Iterable, List
from typing_extensions import Literal
from .._types import SequenceNotStr

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
from ..types.video_asset_create_response import VideoAssetCreateResponse
from ..types import (
    video_asset_create_params,
    video_asset_upload_params,
    video_asset_update_params,
    video_asset_thumbnail_select_params,
    video_asset_create_update_chapter_params,
    video_asset_list_params,
    video_asset_list_deprecated_params,
    video_asset_delete_many_params,
    video_asset_tag_many_params,
    video_asset_analytics_params,
)
from ..types.video_asset_upload_response import VideoAssetUploadResponse
from ..types.video_asset_retrieve_details_response import VideoAssetRetrieveDetailsResponse
from ..types.video_asset_update_response import VideoAssetUpdateResponse
from ..types.video_asset_thumbnail_select_response import VideoAssetThumbnailSelectResponse
from ..types.video_asset_thumbnail_upload_response import VideoAssetThumbnailUploadResponse
from ..types.video_asset_create_update_chapter_response import VideoAssetCreateUpdateChapterResponse
from ..types.video_asset_list_response import VideoAssetListResponse
from ..types.video_asset_list_deprecated_response import VideoAssetListDeprecatedResponse
from ..types.video_asset_delete_many_response import VideoAssetDeleteManyResponse
from ..types.video_asset_tag_many_response import VideoAssetTagManyResponse
from ..types.video_asset_analytics_response import VideoAssetAnalyticsResponse

__all__ = ["VideoAssetsResource", "AsyncVideoAssetsResource"]


class VideoAssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoAssetsResourceWithRawResponse:
        return VideoAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoAssetsResourceWithStreamingResponse:
        return VideoAssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: str,
        collection_id: str,
        profile_id: str | Omit = omit,
        format: Literal["ABR", "MP4"],
        tag: SequenceNotStr[str] | Omit = omit,
        title: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_asset_create_params.Crop | Omit = omit,
        pad: video_asset_create_params.Pad | Omit = omit,
        trim: video_asset_create_params.Trim | Omit = omit,
        image_overlay: video_asset_create_params.ImageOverlay | Omit = omit,
        text_overlay: video_asset_create_params.TextOverlay | Omit = omit,
        animated_gif: video_asset_create_params.AnimatedGif | Omit = omit,
        additional_tracks: Iterable[video_asset_create_params.AdditionalTrack] | Omit = omit,
        generate_subtitles: video_asset_create_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        call_to_actions: Iterable[video_asset_create_params.CallToAction] | Omit = omit,
        playlist_id: str | Omit = omit,
        folder: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetCreateResponse:
        """
        An asset refers to a media content/video that is processed, stored, and delivered through Gumlet. This endpoint creates an asset allowing users to ingest media content into the Gumlet system for processing and delivery.

        Args:
            input: URL or web address of a file that Gumlet should download to create a new asset.
            collection_id: Gumlet video workspace id.
            profile_id: Provide `profile_id` of the previously created video profile. This parameter will override all the parameters (except `input` and `collection_id`) from the video profile.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and`MP4`.
            tag: Specify a text string or identifier which can identify an asset or bunch of assets later.
            title: Specify a text string or identifier which can be used for filtering or searching the asset.
            description: Attach some textual data with the asset. This field is neither searchable nor filterable.
            metadata: Add your metadata you want to associate with this asset.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Applicable only when specified format is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Applicable only when specified format is `MP4`.
            resolution: Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values: `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from the video.
            additional_tracks: Add additional Audio / Subtitle tracks to Gumlet for transcoding and delivery along with video asset track.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            mp4_access: Creates `MP4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            call_to_actions: CTA, is an explicit prompt within the video content encouraging viewers to take a particular action.
            playlist_id: Add this asset to a playlist.
            folder: Add this asset to an existing folder by `folder_id`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetCreateResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.create(
                input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
                collection_id="646df1c9173a4a2fcac180b4",
                profile_id="646df1c9173a4a2fcac180b7",
                format="ABR",
                tag=["ball"],
                description="some description",
                metadata={"headermeta": "metavalue"},
                call_to_actions=[
                    {
                        "start_time": 1,
                        "end_time": 90,
                        "text": "some test",
                        "url": "https://some-url.com",
                        "position_from_top": 11,
                        "position_from_right": 23,
                        "border_radius": "11",
                        "font_color": "#000001",
                        "background_color": "#ffffff",
                    }
                ],
                playlist_id="6597acd5ed6f26a9c5ca9633",
                folder="697375fbfa2d1037283140e4",
            )
            ```
        """
        return self._post(
            "/video/assets",
            body=maybe_transform(
                {
                    "input": input,
                    "collection_id": collection_id,
                    "profile_id": profile_id,
                    "format": format,
                    "tag": tag,
                    "title": title,
                    "description": description,
                    "metadata": metadata,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "additional_tracks": additional_tracks,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                    "call_to_actions": call_to_actions,
                    "playlist_id": playlist_id,
                    "folder": folder,
                },
                video_asset_create_params.VideoAssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetCreateResponse,
        )

    def upload(
        self,
        *,
        collection_id: str,
        profile_id: str | Omit = omit,
        format: Literal["ABR", "MP4"] | Omit = omit,
        tag: SequenceNotStr[str] | Omit = omit,
        title: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_asset_upload_params.Crop | Omit = omit,
        pad: video_asset_upload_params.Pad | Omit = omit,
        trim: video_asset_upload_params.Trim | Omit = omit,
        image_overlay: video_asset_upload_params.ImageOverlay | Omit = omit,
        text_overlay: video_asset_upload_params.TextOverlay | Omit = omit,
        animated_gif: video_asset_upload_params.AnimatedGif | Omit = omit,
        additional_tracks: Iterable[video_asset_upload_params.AdditionalTrack] | Omit = omit,
        generate_subtitles: video_asset_upload_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        call_to_actions: Iterable[video_asset_upload_params.CallToAction] | Omit = omit,
        playlist_id: str | Omit = omit,
        folder: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetUploadResponse:
        """
        This endpoint creates a video asset allowing to upload of the video from the local file system and ingest media content into the Gumlet system for processing and delivery.Body Parameters are the same as the Create Asset Body Parameters except for the `input` parameter which this endpoint does not take.A successful response will be returned with `upload_url` field. You can make `PUT` request to that URL to upload video. To upload video using `upload_url` refer to [this](https://docs.gumlet.com/docs/direct-upload#2-use-the-url-to-upload-a-file).

        Args:
            collection_id: Gumlet video workspace id.
            profile_id: Provide `profile_id` of the previously created video profile. This parameter will override all the parameters (except `input` and `collection_id`) from the video profile.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and`MP4`.
            tag: Specify a text string or identifier which can identify an asset or bunch of assets later.
            title: Specify a text string or identifier which can be used for filtering or searching the asset.
            description: Attach some textual data with the asset. This field is neither searchable nor filterable.
            metadata: Add your metadata you want to associate with this asset.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Applicable only when specified format is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Applicable only when specified format is `MP4`.
            resolution: Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values: `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from the video.
            additional_tracks: Add additional Audio / Subtitle tracks to Gumlet for transcoding and delivery along with video asset track.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            mp4_access: Creates `MP4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            call_to_actions: CTA, is an explicit prompt within the video content encouraging viewers to take a particular action.
            playlist_id: Add this asset to a playlist.
            folder: Add this asset to an existing folder by `folder_id`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetUploadResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.upload(
                collection_id="646df1c9173a4a2fcac180b4",
                profile_id="646df1c9173a4a2fcac180b7",
                format="ABR",
                tag=["ball"],
                description="some description",
                metadata={"headermeta": "metavalue"},
                call_to_actions=[
                    {
                        "start_time": 1,
                        "end_time": 90,
                        "text": "some test",
                        "url": "https://some-url.com",
                        "position_from_top": 11,
                        "position_from_right": 23,
                        "border_radius": "11",
                        "font_color": "#000001",
                        "background_color": "#ffffff",
                    }
                ],
                playlist_id="6597acd5ed6f26a9c5ca9633",
                folder="697375fbfa2d1037283140e4",
            )
            ```
        """
        return self._post(
            "/video/assets/upload",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "profile_id": profile_id,
                    "format": format,
                    "tag": tag,
                    "title": title,
                    "description": description,
                    "metadata": metadata,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "additional_tracks": additional_tracks,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                    "call_to_actions": call_to_actions,
                    "playlist_id": playlist_id,
                    "folder": folder,
                },
                video_asset_upload_params.VideoAssetUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetUploadResponse,
        )

    def retrieve_details(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetRetrieveDetailsResponse:
        """
        This endpoint retrieves the details of an asset that has previously been created.

        Args:
            asset_id: An asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetRetrieveDetailsResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.retrieve_details(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            path_template("/video/assets/{asset_id}", **{"asset_id": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetRetrieveDetailsResponse,
        )

    def delete(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        This endpoint removes an asset given its unique asset id. The asset will be removed from storage as well, associated URLs will be inaccessible.

        Args:
            asset_id: Asset id of the video asset which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            204

        Example:
            ```python
            client.video_assets.delete(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/video/assets/{asset_id}", **{"asset_id": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        *,
        asset_id: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        tag: str | Omit = omit,
        call_to_actions: Iterable[video_asset_update_params.CallToAction] | Omit = omit,
        metadata: str | Omit = omit,
        remove_subtitles: SequenceNotStr[str] | Omit = omit,
        input: str | Omit = omit,
        reprocess: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetUpdateResponse:
        """
        This endpoint allows users to update video asset that has previously been created.

        Args:
            asset_id: Asset Id
            title: Specify a text string or identifier which can be used for filtering or searching the asset.
            description: Attach some textual data with the asset. This field is neither searchable nor filterable.
            tag: Specify a text string or identifier which can identify an asset or bunch of assets later. You can pass multiple comma separated values.
            call_to_actions: CTA, is an explicit prompt within the video content encouraging viewers to take a particular action.
            metadata: Set of key-value pairs that you can attach to this Asset. This can be useful for storing additional information.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>
            remove_subtitles: Comma separated string of language codes.
            input: For replacing videos, pass this along with `asset_id`
            reprocess: To reprocess same video, pass this as true.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetUpdateResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.update(
                asset_id="<YOUR_ASSET_ID>",
                title="Updated Title",
            )
            ```
        """
        return self._post(
            "/video/assets/update",
            body=maybe_transform(
                {
                    "asset_id": asset_id,
                    "title": title,
                    "description": description,
                    "tag": tag,
                    "call_to_actions": call_to_actions,
                    "metadata": metadata,
                    "remove_subtitles": remove_subtitles,
                    "input": input,
                    "reprocess": reprocess,
                },
                video_asset_update_params.VideoAssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetUpdateResponse,
        )

    def thumbnail_select(
        self,
        asset_id: str,
        *,
        frame_at_second: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetThumbnailSelectResponse:
        """
        Select frame from video to use as thumbnail.

        Args:
            asset_id: Asset id of the video asset which needs to be deleted.
            frame_at_second: Frame secound
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetThumbnailSelectResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.thumbnail_select(
                asset_id="assetId",
                frame_at_second=2,
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            path_template("/video/assets/{asset_id}/thumbnail-select", **{"asset_id": asset_id}),
            body=maybe_transform(
                {"frame_at_second": frame_at_second},
                video_asset_thumbnail_select_params.VideoAssetThumbnailSelectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetThumbnailSelectResponse,
        )

    def thumbnail_upload(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetThumbnailUploadResponse:
        """
        Use any image file to use as thumbnail. Once you use the API, you will get `upload_url` in the response, and that can be used to upload the image file.
        
        Here is the sample curl request.
        
        ```bash
        curl --location --request PUT '<upload_url>' \
        --data '<YOUR_FILE_PATH>'
        ```
        
        Args:
            asset_id: An asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            VideoAssetThumbnailUploadResponse
        
        Example:
            ```python
            video_asset = client.video_assets.thumbnail_upload(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_ID}/thumbnail", **{"asset_ID": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetThumbnailUploadResponse,
        )

    def create_update_chapter(
        self,
        asset_id: str,
        *,
        chapters: Iterable[video_asset_create_update_chapter_params.Chapter],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetCreateUpdateChapterResponse:
        """
        This endpoint will create/update video asset chapters.

        Args:
            asset_id: Gumlet asset ID
            chapters: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetCreateUpdateChapterResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.create_update_chapter(
                asset_id="assetId",
                chapters=[{"label": "Chapter 1", "startTime": 0}, {"label": "Chapter 2", "startTime": 10}],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_id}/chapters", **{"asset_id": asset_id}),
            body=maybe_transform(
                {"chapters": chapters},
                video_asset_create_update_chapter_params.VideoAssetCreateUpdateChapterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetCreateUpdateChapterResponse,
        )

    def list(
        self,
        workspace_id: str,
        *,
        type: Literal["folders", "videos", "all"] | Omit = omit,
        parent_id: str | Omit = omit,
        title: str | Omit = omit,
        status: str | Omit = omit,
        tag: str | Omit = omit,
        playlist_id: str | Omit = omit,
        start_date: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: float | Omit = omit,
        max_duration: float | Omit = omit,
        sort_by: Literal["title", "duration", "uploaded_at", "created_at"] | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        search_index: Literal["search_index_for_asset_list", "cms-search", "cms-search-v2"] | Omit = omit,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        signed_token: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetListResponse:
        """
        List folders and assets for a workspace in a single response. Use `parent_id` to browse a specific folder, or filters like `title`, `status`, and `playlist_id` to search assets.

        Args:
            workspace_id: Video workspace id.
            type: Return `folders`, `videos`, or `all`. Default is `all`.
            parent_id: Parent folder id. Send `null` to browse the root level.
            title: Search folders or assets by title or description.
            status: Comma-separated asset status values.
            tag: Comma-separated asset tags.
            playlist_id: Filter assets to a playlist.
            start_date: Asset created_at lower bound.
            end_date: Asset created_at upper bound.
            min_duration: Minimum asset duration in seconds.
            max_duration: Maximum asset duration in seconds.
            sort_by: Sort assets by a supported field.
            order_by: Asset sort order.
            search_index: Search index used for asset title search.
            offset: Offset for paginated results.
            size: Page size. Maximum 100.
            signed_token: Whether URLs should be pre-signed in the API response. Possible values: `true` and `false`. Default is `false`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetListResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.list(
                workspace_id="workspaceId",
                type="all",
                offset=0,
                size=20,
                signed_token="false",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            path_template("/video/workspaces/{workspace_id}/list", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "parent_id": parent_id,
                        "title": title,
                        "status": status,
                        "tag": tag,
                        "playlist_id": playlist_id,
                        "start_date": start_date,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "max_duration": max_duration,
                        "sort_by": sort_by,
                        "order_by": order_by,
                        "search_index": search_index,
                        "offset": offset,
                        "size": size,
                        "signed_token": signed_token,
                    },
                    video_asset_list_params.VideoAssetListParams,
                ),
            ),
            cast_to=VideoAssetListResponse,
        )

    def list_deprecated(
        self,
        workspace_id: str,
        *,
        status: Literal["queued", "processing", "ready", "errored", "deleted"] | Omit = omit,
        tag: str | Omit = omit,
        title: str | Omit = omit,
        folder: str | Omit = omit,
        offset: str | Omit = omit,
        size: str | Omit = omit,
        playlist_id: str | Omit = omit,
        sort_by: Literal["title", "duration", "uploaded_at", "created_at"] | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetListDeprecatedResponse:
        """
        [Deprecated] This endpoint list assets in video workspace. You can also pass `status` and `tag` to filter assets.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            status: To filter assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `queued`, `processing`, `ready`, `errored`, and `deleted`.
            tag: Input tag on the basis of which assets need to be filtered. To filter on multiple tags use comma-separated string.
            title: Title on the basis of which assets need to be filtered.
            folder: Folder name on the basis of which assets need to be filtered.
            offset: Offset value for a paginated list of assets.
            size: Page size for the paginated list. **Default: `10`** **Max Size: `100`**
            playlist_id: filter assets from a playlist.
            sort_by: assets will be sorted based on the provided field.
            order_by: assets will be sorted in the specified order based on provided sortBy field or by default createAt field.
            type: Search for folders, videos, or both. For videos, use `videos`. For folders, use `folders`. If you do not send this parameter, it will search for both.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetListDeprecatedResponse: 200

        Example:
            ```python
            video_asset = client.video_assets.list_deprecated(
                workspace_id="workspaceId",
                sort_by="created_at",
                order_by="desc",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            path_template("/video/assets/list/{workspace_id}", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status": status,
                        "tag": tag,
                        "title": title,
                        "folder": folder,
                        "offset": offset,
                        "size": size,
                        "playlist_id": playlist_id,
                        "sort_by": sort_by,
                        "order_by": order_by,
                        "type": type,
                    },
                    video_asset_list_deprecated_params.VideoAssetListDeprecatedParams,
                ),
            ),
            cast_to=VideoAssetListDeprecatedResponse,
        )

    def delete_many(
        self,
        *,
        asset_list: SequenceNotStr[str],
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetDeleteManyResponse:
        """
        Delete multiple VOD assets at once.

        Args:
            asset_list: LIst of asset ids to delete
            source_id: Workspace ID from which assets needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetDeleteManyResponse: Successful response

        Example:
            ```python
            video_asset = client.video_assets.delete_many(
                asset_list=["64249a8858fd3a208b987702", "64784bae843b155b829bbf84"],
                source_id="60bd2ba353ff754d28179ee6",
            )
            ```
        """
        return self._delete(
            "/video/assets/bulk/delete",
            body=maybe_transform(
                {
                    "asset_list": asset_list,
                    "source_id": source_id,
                },
                video_asset_delete_many_params.VideoAssetDeleteManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetDeleteManyResponse,
        )

    def tag_many(
        self,
        *,
        asset_list: SequenceNotStr[str],
        source_id: str,
        add_tags: SequenceNotStr[str],
        remove_tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetTagManyResponse:
        """
        Add / remove tags from multiple assets at once.

        Args:
            asset_list: List of asset ids to update the tags for.
            source_id: Workspace ID in which the videos needs the operation
            add_tags: List of tags to add to given assets.
            remove_tags: List of tags to remove from given assets. Pass empty array if nothing is to be removed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetTagManyResponse: Successful response

        Example:
            ```python
            video_asset = client.video_assets.tag_many(
                asset_list=["6221db301c8b821b0519fba0", "61e8f2726ec832ab2ac4fa6e"],
                source_id="60bd2ba353ff754d28179ee6",
                add_tags=["tag-1"],
                remove_tags=["playlist-1"],
            )
            ```
        """
        return self._post(
            "/video/assets/bulk/tag",
            body=maybe_transform(
                {
                    "asset_list": asset_list,
                    "source_id": source_id,
                    "add_tags": add_tags,
                    "remove_tags": remove_tags,
                },
                video_asset_tag_many_params.VideoAssetTagManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetTagManyResponse,
        )

    def analytics(
        self,
        asset_id: str,
        *,
        group_by: Literal["daily", "monthly", "weekly"],
        date_range: video_asset_analytics_params.DateRange,
        metrics: List[
            Literal[
                "impressions",
                "views",
                "playing_time",
                "top_countries",
                "top_pages",
                "top_cities",
                "top_device_types",
                "top_browsers",
                "heatmap",
                "widget_data",
            ]
        ],
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetAnalyticsResponse:
        """
        Get video analytics for a single asset.

        Args:
            asset_id: Gumlet asset ID
            group_by: Group the data by this period.
            date_range: Body parameter.
            metrics: List of metrics to return in response.
            page_number: Page number to fetch. Starting at 1
            page_size: Number of items to return per page
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetAnalyticsResponse: Successful response

        Example:
            ```python
            video_asset = client.video_assets.analytics(
                asset_id="assetId",
                group_by="daily",
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                metrics=["impressions"],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_id}/analytics", **{"asset_id": asset_id}),
            body=maybe_transform(
                {
                    "group_by": group_by,
                    "date_range": date_range,
                    "metrics": metrics,
                    "page_number": page_number,
                    "page_size": page_size,
                },
                video_asset_analytics_params.VideoAssetAnalyticsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetAnalyticsResponse,
        )


class AsyncVideoAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoAssetsResourceWithRawResponse:
        return AsyncVideoAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoAssetsResourceWithStreamingResponse:
        return AsyncVideoAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: str,
        collection_id: str,
        profile_id: str | Omit = omit,
        format: Literal["ABR", "MP4"],
        tag: SequenceNotStr[str] | Omit = omit,
        title: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_asset_create_params.Crop | Omit = omit,
        pad: video_asset_create_params.Pad | Omit = omit,
        trim: video_asset_create_params.Trim | Omit = omit,
        image_overlay: video_asset_create_params.ImageOverlay | Omit = omit,
        text_overlay: video_asset_create_params.TextOverlay | Omit = omit,
        animated_gif: video_asset_create_params.AnimatedGif | Omit = omit,
        additional_tracks: Iterable[video_asset_create_params.AdditionalTrack] | Omit = omit,
        generate_subtitles: video_asset_create_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        call_to_actions: Iterable[video_asset_create_params.CallToAction] | Omit = omit,
        playlist_id: str | Omit = omit,
        folder: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetCreateResponse:
        """
        An asset refers to a media content/video that is processed, stored, and delivered through Gumlet. This endpoint creates an asset allowing users to ingest media content into the Gumlet system for processing and delivery.

        Args:
            input: URL or web address of a file that Gumlet should download to create a new asset.
            collection_id: Gumlet video workspace id.
            profile_id: Provide `profile_id` of the previously created video profile. This parameter will override all the parameters (except `input` and `collection_id`) from the video profile.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and`MP4`.
            tag: Specify a text string or identifier which can identify an asset or bunch of assets later.
            title: Specify a text string or identifier which can be used for filtering or searching the asset.
            description: Attach some textual data with the asset. This field is neither searchable nor filterable.
            metadata: Add your metadata you want to associate with this asset.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Applicable only when specified format is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Applicable only when specified format is `MP4`.
            resolution: Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values: `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from the video.
            additional_tracks: Add additional Audio / Subtitle tracks to Gumlet for transcoding and delivery along with video asset track.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            mp4_access: Creates `MP4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            call_to_actions: CTA, is an explicit prompt within the video content encouraging viewers to take a particular action.
            playlist_id: Add this asset to a playlist.
            folder: Add this asset to an existing folder by `folder_id`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetCreateResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.create(
                input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
                collection_id="646df1c9173a4a2fcac180b4",
                profile_id="646df1c9173a4a2fcac180b7",
                format="ABR",
                tag=["ball"],
                description="some description",
                metadata={"headermeta": "metavalue"},
                call_to_actions=[
                    {
                        "start_time": 1,
                        "end_time": 90,
                        "text": "some test",
                        "url": "https://some-url.com",
                        "position_from_top": 11,
                        "position_from_right": 23,
                        "border_radius": "11",
                        "font_color": "#000001",
                        "background_color": "#ffffff",
                    }
                ],
                playlist_id="6597acd5ed6f26a9c5ca9633",
                folder="697375fbfa2d1037283140e4",
            )
            ```
        """
        return await self._post(
            "/video/assets",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "collection_id": collection_id,
                    "profile_id": profile_id,
                    "format": format,
                    "tag": tag,
                    "title": title,
                    "description": description,
                    "metadata": metadata,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "additional_tracks": additional_tracks,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                    "call_to_actions": call_to_actions,
                    "playlist_id": playlist_id,
                    "folder": folder,
                },
                video_asset_create_params.VideoAssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetCreateResponse,
        )

    async def upload(
        self,
        *,
        collection_id: str,
        profile_id: str | Omit = omit,
        format: Literal["ABR", "MP4"] | Omit = omit,
        tag: SequenceNotStr[str] | Omit = omit,
        title: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_asset_upload_params.Crop | Omit = omit,
        pad: video_asset_upload_params.Pad | Omit = omit,
        trim: video_asset_upload_params.Trim | Omit = omit,
        image_overlay: video_asset_upload_params.ImageOverlay | Omit = omit,
        text_overlay: video_asset_upload_params.TextOverlay | Omit = omit,
        animated_gif: video_asset_upload_params.AnimatedGif | Omit = omit,
        additional_tracks: Iterable[video_asset_upload_params.AdditionalTrack] | Omit = omit,
        generate_subtitles: video_asset_upload_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        call_to_actions: Iterable[video_asset_upload_params.CallToAction] | Omit = omit,
        playlist_id: str | Omit = omit,
        folder: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetUploadResponse:
        """
        This endpoint creates a video asset allowing to upload of the video from the local file system and ingest media content into the Gumlet system for processing and delivery.Body Parameters are the same as the Create Asset Body Parameters except for the `input` parameter which this endpoint does not take.A successful response will be returned with `upload_url` field. You can make `PUT` request to that URL to upload video. To upload video using `upload_url` refer to [this](https://docs.gumlet.com/docs/direct-upload#2-use-the-url-to-upload-a-file).

        Args:
            collection_id: Gumlet video workspace id.
            profile_id: Provide `profile_id` of the previously created video profile. This parameter will override all the parameters (except `input` and `collection_id`) from the video profile.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and`MP4`.
            tag: Specify a text string or identifier which can identify an asset or bunch of assets later.
            title: Specify a text string or identifier which can be used for filtering or searching the asset.
            description: Attach some textual data with the asset. This field is neither searchable nor filterable.
            metadata: Add your metadata you want to associate with this asset.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Applicable only when specified format is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Applicable only when specified format is `MP4`.
            resolution: Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values: `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from the video.
            additional_tracks: Add additional Audio / Subtitle tracks to Gumlet for transcoding and delivery along with video asset track.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            mp4_access: Creates `MP4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            call_to_actions: CTA, is an explicit prompt within the video content encouraging viewers to take a particular action.
            playlist_id: Add this asset to a playlist.
            folder: Add this asset to an existing folder by `folder_id`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetUploadResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.upload(
                collection_id="646df1c9173a4a2fcac180b4",
                profile_id="646df1c9173a4a2fcac180b7",
                format="ABR",
                tag=["ball"],
                description="some description",
                metadata={"headermeta": "metavalue"},
                call_to_actions=[
                    {
                        "start_time": 1,
                        "end_time": 90,
                        "text": "some test",
                        "url": "https://some-url.com",
                        "position_from_top": 11,
                        "position_from_right": 23,
                        "border_radius": "11",
                        "font_color": "#000001",
                        "background_color": "#ffffff",
                    }
                ],
                playlist_id="6597acd5ed6f26a9c5ca9633",
                folder="697375fbfa2d1037283140e4",
            )
            ```
        """
        return await self._post(
            "/video/assets/upload",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "profile_id": profile_id,
                    "format": format,
                    "tag": tag,
                    "title": title,
                    "description": description,
                    "metadata": metadata,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "additional_tracks": additional_tracks,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                    "call_to_actions": call_to_actions,
                    "playlist_id": playlist_id,
                    "folder": folder,
                },
                video_asset_upload_params.VideoAssetUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetUploadResponse,
        )

    async def retrieve_details(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetRetrieveDetailsResponse:
        """
        This endpoint retrieves the details of an asset that has previously been created.

        Args:
            asset_id: An asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetRetrieveDetailsResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.retrieve_details(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            path_template("/video/assets/{asset_id}", **{"asset_id": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetRetrieveDetailsResponse,
        )

    async def delete(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        This endpoint removes an asset given its unique asset id. The asset will be removed from storage as well, associated URLs will be inaccessible.

        Args:
            asset_id: Asset id of the video asset which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            204

        Example:
            ```python
            await client.video_assets.delete(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/video/assets/{asset_id}", **{"asset_id": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        *,
        asset_id: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        tag: str | Omit = omit,
        call_to_actions: Iterable[video_asset_update_params.CallToAction] | Omit = omit,
        metadata: str | Omit = omit,
        remove_subtitles: SequenceNotStr[str] | Omit = omit,
        input: str | Omit = omit,
        reprocess: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetUpdateResponse:
        """
        This endpoint allows users to update video asset that has previously been created.

        Args:
            asset_id: Asset Id
            title: Specify a text string or identifier which can be used for filtering or searching the asset.
            description: Attach some textual data with the asset. This field is neither searchable nor filterable.
            tag: Specify a text string or identifier which can identify an asset or bunch of assets later. You can pass multiple comma separated values.
            call_to_actions: CTA, is an explicit prompt within the video content encouraging viewers to take a particular action.
            metadata: Set of key-value pairs that you can attach to this Asset. This can be useful for storing additional information.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>
            remove_subtitles: Comma separated string of language codes.
            input: For replacing videos, pass this along with `asset_id`
            reprocess: To reprocess same video, pass this as true.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetUpdateResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.update(
                asset_id="<YOUR_ASSET_ID>",
                title="Updated Title",
            )
            ```
        """
        return await self._post(
            "/video/assets/update",
            body=await async_maybe_transform(
                {
                    "asset_id": asset_id,
                    "title": title,
                    "description": description,
                    "tag": tag,
                    "call_to_actions": call_to_actions,
                    "metadata": metadata,
                    "remove_subtitles": remove_subtitles,
                    "input": input,
                    "reprocess": reprocess,
                },
                video_asset_update_params.VideoAssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetUpdateResponse,
        )

    async def thumbnail_select(
        self,
        asset_id: str,
        *,
        frame_at_second: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetThumbnailSelectResponse:
        """
        Select frame from video to use as thumbnail.

        Args:
            asset_id: Asset id of the video asset which needs to be deleted.
            frame_at_second: Frame secound
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetThumbnailSelectResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.thumbnail_select(
                asset_id="assetId",
                frame_at_second=2,
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            path_template("/video/assets/{asset_id}/thumbnail-select", **{"asset_id": asset_id}),
            body=await async_maybe_transform(
                {"frame_at_second": frame_at_second},
                video_asset_thumbnail_select_params.VideoAssetThumbnailSelectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetThumbnailSelectResponse,
        )

    async def thumbnail_upload(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetThumbnailUploadResponse:
        """
        Use any image file to use as thumbnail. Once you use the API, you will get `upload_url` in the response, and that can be used to upload the image file.
        
        Here is the sample curl request.
        
        ```bash
        curl --location --request PUT '<upload_url>' \
        --data '<YOUR_FILE_PATH>'
        ```
        
        Args:
            asset_id: An asset id for the previously created asset.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            VideoAssetThumbnailUploadResponse
        
        Example:
            ```python
            video_asset = await client.video_assets.thumbnail_upload(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_ID}/thumbnail", **{"asset_ID": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetThumbnailUploadResponse,
        )

    async def create_update_chapter(
        self,
        asset_id: str,
        *,
        chapters: Iterable[video_asset_create_update_chapter_params.Chapter],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetCreateUpdateChapterResponse:
        """
        This endpoint will create/update video asset chapters.

        Args:
            asset_id: Gumlet asset ID
            chapters: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetCreateUpdateChapterResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.create_update_chapter(
                asset_id="assetId",
                chapters=[{"label": "Chapter 1", "startTime": 0}, {"label": "Chapter 2", "startTime": 10}],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_id}/chapters", **{"asset_id": asset_id}),
            body=await async_maybe_transform(
                {"chapters": chapters},
                video_asset_create_update_chapter_params.VideoAssetCreateUpdateChapterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetCreateUpdateChapterResponse,
        )

    async def list(
        self,
        workspace_id: str,
        *,
        type: Literal["folders", "videos", "all"] | Omit = omit,
        parent_id: str | Omit = omit,
        title: str | Omit = omit,
        status: str | Omit = omit,
        tag: str | Omit = omit,
        playlist_id: str | Omit = omit,
        start_date: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: float | Omit = omit,
        max_duration: float | Omit = omit,
        sort_by: Literal["title", "duration", "uploaded_at", "created_at"] | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        search_index: Literal["search_index_for_asset_list", "cms-search", "cms-search-v2"] | Omit = omit,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        signed_token: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetListResponse:
        """
        List folders and assets for a workspace in a single response. Use `parent_id` to browse a specific folder, or filters like `title`, `status`, and `playlist_id` to search assets.

        Args:
            workspace_id: Video workspace id.
            type: Return `folders`, `videos`, or `all`. Default is `all`.
            parent_id: Parent folder id. Send `null` to browse the root level.
            title: Search folders or assets by title or description.
            status: Comma-separated asset status values.
            tag: Comma-separated asset tags.
            playlist_id: Filter assets to a playlist.
            start_date: Asset created_at lower bound.
            end_date: Asset created_at upper bound.
            min_duration: Minimum asset duration in seconds.
            max_duration: Maximum asset duration in seconds.
            sort_by: Sort assets by a supported field.
            order_by: Asset sort order.
            search_index: Search index used for asset title search.
            offset: Offset for paginated results.
            size: Page size. Maximum 100.
            signed_token: Whether URLs should be pre-signed in the API response. Possible values: `true` and `false`. Default is `false`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetListResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.list(
                workspace_id="workspaceId",
                type="all",
                offset=0,
                size=20,
                signed_token="false",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            path_template("/video/workspaces/{workspace_id}/list", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "parent_id": parent_id,
                        "title": title,
                        "status": status,
                        "tag": tag,
                        "playlist_id": playlist_id,
                        "start_date": start_date,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "max_duration": max_duration,
                        "sort_by": sort_by,
                        "order_by": order_by,
                        "search_index": search_index,
                        "offset": offset,
                        "size": size,
                        "signed_token": signed_token,
                    },
                    video_asset_list_params.VideoAssetListParams,
                ),
            ),
            cast_to=VideoAssetListResponse,
        )

    async def list_deprecated(
        self,
        workspace_id: str,
        *,
        status: Literal["queued", "processing", "ready", "errored", "deleted"] | Omit = omit,
        tag: str | Omit = omit,
        title: str | Omit = omit,
        folder: str | Omit = omit,
        offset: str | Omit = omit,
        size: str | Omit = omit,
        playlist_id: str | Omit = omit,
        sort_by: Literal["title", "duration", "uploaded_at", "created_at"] | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetListDeprecatedResponse:
        """
        [Deprecated] This endpoint list assets in video workspace. You can also pass `status` and `tag` to filter assets.

        Args:
            workspace_id: Gumlet workspace ID. You can get it on Gumlet dashboard or retrieve it using list workspace API.
            status: To filter assets on the basis of their current status. Can be specified as a single status value string or comma-separated status values. The status value can be one of `queued`, `processing`, `ready`, `errored`, and `deleted`.
            tag: Input tag on the basis of which assets need to be filtered. To filter on multiple tags use comma-separated string.
            title: Title on the basis of which assets need to be filtered.
            folder: Folder name on the basis of which assets need to be filtered.
            offset: Offset value for a paginated list of assets.
            size: Page size for the paginated list. **Default: `10`** **Max Size: `100`**
            playlist_id: filter assets from a playlist.
            sort_by: assets will be sorted based on the provided field.
            order_by: assets will be sorted in the specified order based on provided sortBy field or by default createAt field.
            type: Search for folders, videos, or both. For videos, use `videos`. For folders, use `folders`. If you do not send this parameter, it will search for both.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetListDeprecatedResponse: 200

        Example:
            ```python
            video_asset = await client.video_assets.list_deprecated(
                workspace_id="workspaceId",
                sort_by="created_at",
                order_by="desc",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            path_template("/video/assets/list/{workspace_id}", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "status": status,
                        "tag": tag,
                        "title": title,
                        "folder": folder,
                        "offset": offset,
                        "size": size,
                        "playlist_id": playlist_id,
                        "sort_by": sort_by,
                        "order_by": order_by,
                        "type": type,
                    },
                    video_asset_list_deprecated_params.VideoAssetListDeprecatedParams,
                ),
            ),
            cast_to=VideoAssetListDeprecatedResponse,
        )

    async def delete_many(
        self,
        *,
        asset_list: SequenceNotStr[str],
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetDeleteManyResponse:
        """
        Delete multiple VOD assets at once.

        Args:
            asset_list: LIst of asset ids to delete
            source_id: Workspace ID from which assets needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetDeleteManyResponse: Successful response

        Example:
            ```python
            video_asset = await client.video_assets.delete_many(
                asset_list=["64249a8858fd3a208b987702", "64784bae843b155b829bbf84"],
                source_id="60bd2ba353ff754d28179ee6",
            )
            ```
        """
        return await self._delete(
            "/video/assets/bulk/delete",
            body=await async_maybe_transform(
                {
                    "asset_list": asset_list,
                    "source_id": source_id,
                },
                video_asset_delete_many_params.VideoAssetDeleteManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetDeleteManyResponse,
        )

    async def tag_many(
        self,
        *,
        asset_list: SequenceNotStr[str],
        source_id: str,
        add_tags: SequenceNotStr[str],
        remove_tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetTagManyResponse:
        """
        Add / remove tags from multiple assets at once.

        Args:
            asset_list: List of asset ids to update the tags for.
            source_id: Workspace ID in which the videos needs the operation
            add_tags: List of tags to add to given assets.
            remove_tags: List of tags to remove from given assets. Pass empty array if nothing is to be removed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetTagManyResponse: Successful response

        Example:
            ```python
            video_asset = await client.video_assets.tag_many(
                asset_list=["6221db301c8b821b0519fba0", "61e8f2726ec832ab2ac4fa6e"],
                source_id="60bd2ba353ff754d28179ee6",
                add_tags=["tag-1"],
                remove_tags=["playlist-1"],
            )
            ```
        """
        return await self._post(
            "/video/assets/bulk/tag",
            body=await async_maybe_transform(
                {
                    "asset_list": asset_list,
                    "source_id": source_id,
                    "add_tags": add_tags,
                    "remove_tags": remove_tags,
                },
                video_asset_tag_many_params.VideoAssetTagManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetTagManyResponse,
        )

    async def analytics(
        self,
        asset_id: str,
        *,
        group_by: Literal["daily", "monthly", "weekly"],
        date_range: video_asset_analytics_params.DateRange,
        metrics: List[
            Literal[
                "impressions",
                "views",
                "playing_time",
                "top_countries",
                "top_pages",
                "top_cities",
                "top_device_types",
                "top_browsers",
                "heatmap",
                "widget_data",
            ]
        ],
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAssetAnalyticsResponse:
        """
        Get video analytics for a single asset.

        Args:
            asset_id: Gumlet asset ID
            group_by: Group the data by this period.
            date_range: Body parameter.
            metrics: List of metrics to return in response.
            page_number: Page number to fetch. Starting at 1
            page_size: Number of items to return per page
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAssetAnalyticsResponse: Successful response

        Example:
            ```python
            video_asset = await client.video_assets.analytics(
                asset_id="assetId",
                group_by="daily",
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                metrics=["impressions"],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_id}/analytics", **{"asset_id": asset_id}),
            body=await async_maybe_transform(
                {
                    "group_by": group_by,
                    "date_range": date_range,
                    "metrics": metrics,
                    "page_number": page_number,
                    "page_size": page_size,
                },
                video_asset_analytics_params.VideoAssetAnalyticsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAssetAnalyticsResponse,
        )


class VideoAssetsResourceWithRawResponse:
    def __init__(self, video_assets: VideoAssetsResource) -> None:
        self._video_assets = video_assets

        self.create = to_raw_response_wrapper(
            video_assets.create,
        )
        self.upload = to_raw_response_wrapper(
            video_assets.upload,
        )
        self.retrieve_details = to_raw_response_wrapper(
            video_assets.retrieve_details,
        )
        self.delete = to_raw_response_wrapper(
            video_assets.delete,
        )
        self.update = to_raw_response_wrapper(
            video_assets.update,
        )
        self.thumbnail_select = to_raw_response_wrapper(
            video_assets.thumbnail_select,
        )
        self.thumbnail_upload = to_raw_response_wrapper(
            video_assets.thumbnail_upload,
        )
        self.create_update_chapter = to_raw_response_wrapper(
            video_assets.create_update_chapter,
        )
        self.list = to_raw_response_wrapper(
            video_assets.list,
        )
        self.list_deprecated = to_raw_response_wrapper(
            video_assets.list_deprecated,
        )
        self.delete_many = to_raw_response_wrapper(
            video_assets.delete_many,
        )
        self.tag_many = to_raw_response_wrapper(
            video_assets.tag_many,
        )
        self.analytics = to_raw_response_wrapper(
            video_assets.analytics,
        )


class AsyncVideoAssetsResourceWithRawResponse:
    def __init__(self, video_assets: AsyncVideoAssetsResource) -> None:
        self._video_assets = video_assets

        self.create = async_to_raw_response_wrapper(
            video_assets.create,
        )
        self.upload = async_to_raw_response_wrapper(
            video_assets.upload,
        )
        self.retrieve_details = async_to_raw_response_wrapper(
            video_assets.retrieve_details,
        )
        self.delete = async_to_raw_response_wrapper(
            video_assets.delete,
        )
        self.update = async_to_raw_response_wrapper(
            video_assets.update,
        )
        self.thumbnail_select = async_to_raw_response_wrapper(
            video_assets.thumbnail_select,
        )
        self.thumbnail_upload = async_to_raw_response_wrapper(
            video_assets.thumbnail_upload,
        )
        self.create_update_chapter = async_to_raw_response_wrapper(
            video_assets.create_update_chapter,
        )
        self.list = async_to_raw_response_wrapper(
            video_assets.list,
        )
        self.list_deprecated = async_to_raw_response_wrapper(
            video_assets.list_deprecated,
        )
        self.delete_many = async_to_raw_response_wrapper(
            video_assets.delete_many,
        )
        self.tag_many = async_to_raw_response_wrapper(
            video_assets.tag_many,
        )
        self.analytics = async_to_raw_response_wrapper(
            video_assets.analytics,
        )


class VideoAssetsResourceWithStreamingResponse:
    def __init__(self, video_assets: VideoAssetsResource) -> None:
        self._video_assets = video_assets

        self.create = to_streamed_response_wrapper(
            video_assets.create,
        )
        self.upload = to_streamed_response_wrapper(
            video_assets.upload,
        )
        self.retrieve_details = to_streamed_response_wrapper(
            video_assets.retrieve_details,
        )
        self.delete = to_streamed_response_wrapper(
            video_assets.delete,
        )
        self.update = to_streamed_response_wrapper(
            video_assets.update,
        )
        self.thumbnail_select = to_streamed_response_wrapper(
            video_assets.thumbnail_select,
        )
        self.thumbnail_upload = to_streamed_response_wrapper(
            video_assets.thumbnail_upload,
        )
        self.create_update_chapter = to_streamed_response_wrapper(
            video_assets.create_update_chapter,
        )
        self.list = to_streamed_response_wrapper(
            video_assets.list,
        )
        self.list_deprecated = to_streamed_response_wrapper(
            video_assets.list_deprecated,
        )
        self.delete_many = to_streamed_response_wrapper(
            video_assets.delete_many,
        )
        self.tag_many = to_streamed_response_wrapper(
            video_assets.tag_many,
        )
        self.analytics = to_streamed_response_wrapper(
            video_assets.analytics,
        )


class AsyncVideoAssetsResourceWithStreamingResponse:
    def __init__(self, video_assets: AsyncVideoAssetsResource) -> None:
        self._video_assets = video_assets

        self.create = async_to_streamed_response_wrapper(
            video_assets.create,
        )
        self.upload = async_to_streamed_response_wrapper(
            video_assets.upload,
        )
        self.retrieve_details = async_to_streamed_response_wrapper(
            video_assets.retrieve_details,
        )
        self.delete = async_to_streamed_response_wrapper(
            video_assets.delete,
        )
        self.update = async_to_streamed_response_wrapper(
            video_assets.update,
        )
        self.thumbnail_select = async_to_streamed_response_wrapper(
            video_assets.thumbnail_select,
        )
        self.thumbnail_upload = async_to_streamed_response_wrapper(
            video_assets.thumbnail_upload,
        )
        self.create_update_chapter = async_to_streamed_response_wrapper(
            video_assets.create_update_chapter,
        )
        self.list = async_to_streamed_response_wrapper(
            video_assets.list,
        )
        self.list_deprecated = async_to_streamed_response_wrapper(
            video_assets.list_deprecated,
        )
        self.delete_many = async_to_streamed_response_wrapper(
            video_assets.delete_many,
        )
        self.tag_many = async_to_streamed_response_wrapper(
            video_assets.tag_many,
        )
        self.analytics = async_to_streamed_response_wrapper(
            video_assets.analytics,
        )
