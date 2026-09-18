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
from ..types.video_profile_create_response import VideoProfileCreateResponse
from ..types import video_profile_create_params, video_profile_list_params, video_profile_update_params
from ..types.video_profile_list_response import VideoProfileListResponse
from ..types.video_profile_update_response import VideoProfileUpdateResponse
from ..types.video_profile_retrieve_response import VideoProfileRetrieveResponse
from ..types.video_profile_delete_response import VideoProfileDeleteResponse

__all__ = ["VideoProfilesResource", "AsyncVideoProfilesResource"]


class VideoProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoProfilesResourceWithRawResponse:
        return VideoProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoProfilesResourceWithStreamingResponse:
        return VideoProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        format: Literal["ABR", "MP4"],
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_profile_create_params.Crop | Omit = omit,
        pad: video_profile_create_params.Pad | Omit = omit,
        trim: video_profile_create_params.Trim | Omit = omit,
        image_overlay: video_profile_create_params.ImageOverlay | Omit = omit,
        text_overlay: video_profile_create_params.TextOverlay | Omit = omit,
        animated_gif: video_profile_create_params.AnimatedGif | Omit = omit,
        generate_subtitles: video_profile_create_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileCreateResponse:
        """
        Gumlet provides the functionality of creating multiple video assets using the same set of parameters. A Video profile is a set of parameters that can be referenced/used while creating a video as a single parameter.

        Args:
            name: Profile name or identifier.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`.
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Only applicable when specified `format` is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`.
            resolution: Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`,  and `1080p `. Re-sized rendition will retain the input aspect ratio.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from a video.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes). Remove this object if you do not want to generate AI subtitles.
            mp4_access: Creates `mp4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case,This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileCreateResponse: 200

        Example:
            ```python
            video_profile = client.video_profiles.create(
                name="Gumlet-Profile-1",
                format="ABR",
            )
            ```
        """
        return self._post(
            "/video/profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "format": format,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                },
                video_profile_create_params.VideoProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileCreateResponse,
        )

    def list(
        self,
        *,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileListResponse:
        """
        This endpoint retrieves the details of all profiles that have previously been created.

        Args:
            offset: Offset value for a paginated list of profiles. Can be zero for the first time and `current_offset` value received from the last request afterwards.
            size: Page size for the paginated list. **Default: `10`**
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileListResponse: 200

        Example:
            ```python
            video_profile = client.video_profiles.list()
            ```
        """
        return self._get(
            "/video/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"offset": offset, "size": size}, video_profile_list_params.VideoProfileListParams
                ),
            ),
            cast_to=VideoProfileListResponse,
        )

    def update(
        self,
        path_profile_id: str,
        *,
        body_profile_id: str,
        name: str | Omit = omit,
        format: Literal["ABR", "MP4"] | Omit = omit,
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_profile_update_params.Crop | Omit = omit,
        pad: video_profile_update_params.Pad | Omit = omit,
        trim: video_profile_update_params.Trim | Omit = omit,
        image_overlay: video_profile_update_params.ImageOverlay | Omit = omit,
        text_overlay: video_profile_update_params.TextOverlay | Omit = omit,
        animated_gif: video_profile_update_params.AnimatedGif | Omit = omit,
        generate_subtitles: video_profile_update_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        vc: SequenceNotStr[str] | Omit = omit,
        generate_chapters: bool | Omit = omit,
        generate_description: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileUpdateResponse:
        """
        Update an existing profile. Settings provided in body parameters will only be updated in the existing profile.

        Args:
            path_profile_id: Profile id of the profile which need to be updated.
            body_profile_id: Profile id of the profile which needs to be deleted.
            name: Profile name or identifier.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`.
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Only applicable when specified `format` is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`.
            resolution: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from a video.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes). You can remove this object if don't want to generate AI subtitles.
            mp4_access: Creates `mp4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case,This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            vc: Video Codecs
            generate_chapters: Whether Gumlet should generate chapters.
            generate_description: Whether Gumlet should generate descriptions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileUpdateResponse: 200

        Example:
            ```python
            video_profile = client.video_profiles.update(
                path_profile_id="profileId",
                body_profile_id="",
                format="ABR",
            )
            ```
        """
        if path_profile_id is None or (isinstance(path_profile_id, str) and not path_profile_id):
            raise ValueError(f"Expected a non-empty value for `path_profile_id` but received {path_profile_id!r}")
        return self._post(
            path_template("/video/profiles/{profile_id}", **{"profile_id": path_profile_id}),
            body=maybe_transform(
                {
                    "body_profile_id": body_profile_id,
                    "name": name,
                    "format": format,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                    "vc": vc,
                    "generate_chapters": generate_chapters,
                    "generate_description": generate_description,
                },
                video_profile_update_params.VideoProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileUpdateResponse,
        )

    def retrieve(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileRetrieveResponse:
        """
        This endpoint retrieves the details of a video profile that has previously been created.

        Args:
            profile_id: Profile id of the profile which needs to be retrieved.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileRetrieveResponse: 200

        Example:
            ```python
            video_profile = client.video_profiles.retrieve(
                profile_id="profileId",
            )
            ```
        """
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            path_template("/video/profiles/{profile_id}", **{"profile_id": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileRetrieveResponse,
        )

    def delete(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileDeleteResponse:
        """
        This endpoint removes a profile given its unique `profile_id`. The profile will be removed but video assets created using the profile will remain as it is.

        Args:
            profile_id: Profile id of the profile which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileDeleteResponse: 204

        Example:
            ```python
            video_profile = client.video_profiles.delete(
                profile_id="profileId",
            )
            ```
        """
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            path_template("/video/profiles/{profile_id}", **{"profile_id": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileDeleteResponse,
        )


class AsyncVideoProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoProfilesResourceWithRawResponse:
        return AsyncVideoProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoProfilesResourceWithStreamingResponse:
        return AsyncVideoProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        format: Literal["ABR", "MP4"],
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_profile_create_params.Crop | Omit = omit,
        pad: video_profile_create_params.Pad | Omit = omit,
        trim: video_profile_create_params.Trim | Omit = omit,
        image_overlay: video_profile_create_params.ImageOverlay | Omit = omit,
        text_overlay: video_profile_create_params.TextOverlay | Omit = omit,
        animated_gif: video_profile_create_params.AnimatedGif | Omit = omit,
        generate_subtitles: video_profile_create_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileCreateResponse:
        """
        Gumlet provides the functionality of creating multiple video assets using the same set of parameters. A Video profile is a set of parameters that can be referenced/used while creating a video as a single parameter.

        Args:
            name: Profile name or identifier.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`.
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Only applicable when specified `format` is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`.
            resolution: Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`,  and `1080p `. Re-sized rendition will retain the input aspect ratio.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from a video.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes). Remove this object if you do not want to generate AI subtitles.
            mp4_access: Creates `mp4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case,This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileCreateResponse: 200

        Example:
            ```python
            video_profile = await client.video_profiles.create(
                name="Gumlet-Profile-1",
                format="ABR",
            )
            ```
        """
        return await self._post(
            "/video/profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "format": format,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                },
                video_profile_create_params.VideoProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileCreateResponse,
        )

    async def list(
        self,
        *,
        offset: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileListResponse:
        """
        This endpoint retrieves the details of all profiles that have previously been created.

        Args:
            offset: Offset value for a paginated list of profiles. Can be zero for the first time and `current_offset` value received from the last request afterwards.
            size: Page size for the paginated list. **Default: `10`**
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileListResponse: 200

        Example:
            ```python
            video_profile = await client.video_profiles.list()
            ```
        """
        return await self._get(
            "/video/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"offset": offset, "size": size}, video_profile_list_params.VideoProfileListParams
                ),
            ),
            cast_to=VideoProfileListResponse,
        )

    async def update(
        self,
        path_profile_id: str,
        *,
        body_profile_id: str,
        name: str | Omit = omit,
        format: Literal["ABR", "MP4"] | Omit = omit,
        width: str | Omit = omit,
        height: str | Omit = omit,
        resolution: str | Omit = omit,
        crop: video_profile_update_params.Crop | Omit = omit,
        pad: video_profile_update_params.Pad | Omit = omit,
        trim: video_profile_update_params.Trim | Omit = omit,
        image_overlay: video_profile_update_params.ImageOverlay | Omit = omit,
        text_overlay: video_profile_update_params.TextOverlay | Omit = omit,
        animated_gif: video_profile_update_params.AnimatedGif | Omit = omit,
        generate_subtitles: video_profile_update_params.GenerateSubtitles | Omit = omit,
        mp4_access: bool | Omit = omit,
        per_title_encoding: bool | Omit = omit,
        process_low_resolution_input: bool | Omit = omit,
        audio_only: bool | Omit = omit,
        enable_drm: bool | Omit = omit,
        vc: SequenceNotStr[str] | Omit = omit,
        generate_chapters: bool | Omit = omit,
        generate_description: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileUpdateResponse:
        """
        Update an existing profile. Settings provided in body parameters will only be updated in the existing profile.

        Args:
            path_profile_id: Profile id of the profile which need to be updated.
            body_profile_id: Profile id of the profile which needs to be deleted.
            name: Profile name or identifier.
            format: Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`.
            width: Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Only applicable when specified `format` is `MP4`.
            height: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`.
            resolution: Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`.
            crop: This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.
            pad: This transformation can be used to add padding to the video.
            trim: Trim transformation can be used to trim videos based on time duration.
            image_overlay: Image overlay can be used to brand a video or add a visual label in the form of an image.
            text_overlay: Text overlay can be used to brand a video or add a label in the form of text.
            animated_gif: Create an animated GIF from a video.
            generate_subtitles: Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes). You can remove this object if don't want to generate AI subtitles.
            mp4_access: Creates `mp4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**
            per_title_encoding: Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**
            process_low_resolution_input: Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**
            audio_only: This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case,This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**
            enable_drm: Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs.
            vc: Video Codecs
            generate_chapters: Whether Gumlet should generate chapters.
            generate_description: Whether Gumlet should generate descriptions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileUpdateResponse: 200

        Example:
            ```python
            video_profile = await client.video_profiles.update(
                path_profile_id="profileId",
                body_profile_id="",
                format="ABR",
            )
            ```
        """
        if path_profile_id is None or (isinstance(path_profile_id, str) and not path_profile_id):
            raise ValueError(f"Expected a non-empty value for `path_profile_id` but received {path_profile_id!r}")
        return await self._post(
            path_template("/video/profiles/{profile_id}", **{"profile_id": path_profile_id}),
            body=await async_maybe_transform(
                {
                    "body_profile_id": body_profile_id,
                    "name": name,
                    "format": format,
                    "width": width,
                    "height": height,
                    "resolution": resolution,
                    "crop": crop,
                    "pad": pad,
                    "trim": trim,
                    "image_overlay": image_overlay,
                    "text_overlay": text_overlay,
                    "animated_gif": animated_gif,
                    "generate_subtitles": generate_subtitles,
                    "mp4_access": mp4_access,
                    "per_title_encoding": per_title_encoding,
                    "process_low_resolution_input": process_low_resolution_input,
                    "audio_only": audio_only,
                    "enable_drm": enable_drm,
                    "vc": vc,
                    "generate_chapters": generate_chapters,
                    "generate_description": generate_description,
                },
                video_profile_update_params.VideoProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileUpdateResponse,
        )

    async def retrieve(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileRetrieveResponse:
        """
        This endpoint retrieves the details of a video profile that has previously been created.

        Args:
            profile_id: Profile id of the profile which needs to be retrieved.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileRetrieveResponse: 200

        Example:
            ```python
            video_profile = await client.video_profiles.retrieve(
                profile_id="profileId",
            )
            ```
        """
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            path_template("/video/profiles/{profile_id}", **{"profile_id": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileRetrieveResponse,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoProfileDeleteResponse:
        """
        This endpoint removes a profile given its unique `profile_id`. The profile will be removed but video assets created using the profile will remain as it is.

        Args:
            profile_id: Profile id of the profile which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoProfileDeleteResponse: 204

        Example:
            ```python
            video_profile = await client.video_profiles.delete(
                profile_id="profileId",
            )
            ```
        """
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            path_template("/video/profiles/{profile_id}", **{"profile_id": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoProfileDeleteResponse,
        )


class VideoProfilesResourceWithRawResponse:
    def __init__(self, video_profiles: VideoProfilesResource) -> None:
        self._video_profiles = video_profiles

        self.create = to_raw_response_wrapper(
            video_profiles.create,
        )
        self.list = to_raw_response_wrapper(
            video_profiles.list,
        )
        self.update = to_raw_response_wrapper(
            video_profiles.update,
        )
        self.retrieve = to_raw_response_wrapper(
            video_profiles.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            video_profiles.delete,
        )


class AsyncVideoProfilesResourceWithRawResponse:
    def __init__(self, video_profiles: AsyncVideoProfilesResource) -> None:
        self._video_profiles = video_profiles

        self.create = async_to_raw_response_wrapper(
            video_profiles.create,
        )
        self.list = async_to_raw_response_wrapper(
            video_profiles.list,
        )
        self.update = async_to_raw_response_wrapper(
            video_profiles.update,
        )
        self.retrieve = async_to_raw_response_wrapper(
            video_profiles.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            video_profiles.delete,
        )


class VideoProfilesResourceWithStreamingResponse:
    def __init__(self, video_profiles: VideoProfilesResource) -> None:
        self._video_profiles = video_profiles

        self.create = to_streamed_response_wrapper(
            video_profiles.create,
        )
        self.list = to_streamed_response_wrapper(
            video_profiles.list,
        )
        self.update = to_streamed_response_wrapper(
            video_profiles.update,
        )
        self.retrieve = to_streamed_response_wrapper(
            video_profiles.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            video_profiles.delete,
        )


class AsyncVideoProfilesResourceWithStreamingResponse:
    def __init__(self, video_profiles: AsyncVideoProfilesResource) -> None:
        self._video_profiles = video_profiles

        self.create = async_to_streamed_response_wrapper(
            video_profiles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            video_profiles.list,
        )
        self.update = async_to_streamed_response_wrapper(
            video_profiles.update,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            video_profiles.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            video_profiles.delete,
        )
