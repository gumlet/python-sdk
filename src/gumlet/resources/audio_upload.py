# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable
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
from ..types.audio_upload_upload_response import AudioUploadUploadResponse
from ..types import audio_upload_upload_params, audio_upload_complete_params
from ..types.audio_upload_complete_response import AudioUploadCompleteResponse

__all__ = ["AudioUploadResource", "AsyncAudioUploadResource"]


class AudioUploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudioUploadResourceWithRawResponse:
        return AudioUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioUploadResourceWithStreamingResponse:
        return AudioUploadResourceWithStreamingResponse(self)

    def upload(
        self,
        asset_id: str,
        *,
        language_codes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudioUploadUploadResponse:
        """
        Add any audio file to the video asset.
        The response of this API call gives `upload_url` for each language specified. You need to send a `PUT` request of the audio files to those URLs. Once that's done, you need to call the audio upload complete API. Only after that will Gumlet add audio to the asset.

        Args:
            asset_id: An asset id for the previously created asset.
            language_codes: List of language Code to upload audio file  (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AudioUploadUploadResponse: 200

        Example:
            ```python
            audio_upload = client.audio_upload.upload(
                asset_id="assetId",
                language_codes=["en"],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_ID}/audio/upload", **{"asset_ID": asset_id}),
            body=maybe_transform(
                {"language_codes": language_codes},
                audio_upload_upload_params.AudioUploadUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioUploadUploadResponse,
        )

    def complete(
        self,
        asset_id: str,
        *,
        upload_responses: Iterable[audio_upload_complete_params.UploadResponse] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudioUploadCompleteResponse:
        """
        This API must be called after adding audio(s); The add audio call gives you URLs to upload, and you complete a `PUT` request to those URLs.
        Once that is done, calling this initiates the process to actually add the subtitle to the video.

        Args:
            asset_id: An asset id for the previously created asset.
            upload_responses: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AudioUploadCompleteResponse: 200

        Example:
            ```python
            audio_upload = client.audio_upload.complete(
                asset_id="assetId",
                upload_responses=[{"language_codes": ["en"], "uploaded": True}],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_ID}/audio/upload/event", **{"asset_ID": asset_id}),
            body=maybe_transform(
                {"upload_responses": upload_responses},
                audio_upload_complete_params.AudioUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioUploadCompleteResponse,
        )


class AsyncAudioUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudioUploadResourceWithRawResponse:
        return AsyncAudioUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioUploadResourceWithStreamingResponse:
        return AsyncAudioUploadResourceWithStreamingResponse(self)

    async def upload(
        self,
        asset_id: str,
        *,
        language_codes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudioUploadUploadResponse:
        """
        Add any audio file to the video asset.
        The response of this API call gives `upload_url` for each language specified. You need to send a `PUT` request of the audio files to those URLs. Once that's done, you need to call the audio upload complete API. Only after that will Gumlet add audio to the asset.

        Args:
            asset_id: An asset id for the previously created asset.
            language_codes: List of language Code to upload audio file  (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AudioUploadUploadResponse: 200

        Example:
            ```python
            audio_upload = await client.audio_upload.upload(
                asset_id="assetId",
                language_codes=["en"],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_ID}/audio/upload", **{"asset_ID": asset_id}),
            body=await async_maybe_transform(
                {"language_codes": language_codes},
                audio_upload_upload_params.AudioUploadUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioUploadUploadResponse,
        )

    async def complete(
        self,
        asset_id: str,
        *,
        upload_responses: Iterable[audio_upload_complete_params.UploadResponse] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudioUploadCompleteResponse:
        """
        This API must be called after adding audio(s); The add audio call gives you URLs to upload, and you complete a `PUT` request to those URLs.
        Once that is done, calling this initiates the process to actually add the subtitle to the video.

        Args:
            asset_id: An asset id for the previously created asset.
            upload_responses: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AudioUploadCompleteResponse: 200

        Example:
            ```python
            audio_upload = await client.audio_upload.complete(
                asset_id="assetId",
                upload_responses=[{"language_codes": ["en"], "uploaded": True}],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_ID}/audio/upload/event", **{"asset_ID": asset_id}),
            body=await async_maybe_transform(
                {"upload_responses": upload_responses},
                audio_upload_complete_params.AudioUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioUploadCompleteResponse,
        )


class AudioUploadResourceWithRawResponse:
    def __init__(self, audio_upload: AudioUploadResource) -> None:
        self._audio_upload = audio_upload

        self.upload = to_raw_response_wrapper(
            audio_upload.upload,
        )
        self.complete = to_raw_response_wrapper(
            audio_upload.complete,
        )


class AsyncAudioUploadResourceWithRawResponse:
    def __init__(self, audio_upload: AsyncAudioUploadResource) -> None:
        self._audio_upload = audio_upload

        self.upload = async_to_raw_response_wrapper(
            audio_upload.upload,
        )
        self.complete = async_to_raw_response_wrapper(
            audio_upload.complete,
        )


class AudioUploadResourceWithStreamingResponse:
    def __init__(self, audio_upload: AudioUploadResource) -> None:
        self._audio_upload = audio_upload

        self.upload = to_streamed_response_wrapper(
            audio_upload.upload,
        )
        self.complete = to_streamed_response_wrapper(
            audio_upload.complete,
        )


class AsyncAudioUploadResourceWithStreamingResponse:
    def __init__(self, audio_upload: AsyncAudioUploadResource) -> None:
        self._audio_upload = audio_upload

        self.upload = async_to_streamed_response_wrapper(
            audio_upload.upload,
        )
        self.complete = async_to_streamed_response_wrapper(
            audio_upload.complete,
        )
