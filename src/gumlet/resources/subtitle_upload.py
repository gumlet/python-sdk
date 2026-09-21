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
from ..types.subtitle_upload_upload_response import SubtitleUploadUploadResponse
from ..types import subtitle_upload_upload_params, subtitle_upload_complete_params
from ..types.subtitle_upload_complete_response import SubtitleUploadCompleteResponse

__all__ = ["SubtitleUploadResource", "AsyncSubtitleUploadResource"]


class SubtitleUploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubtitleUploadResourceWithRawResponse:
        return SubtitleUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubtitleUploadResourceWithStreamingResponse:
        return SubtitleUploadResourceWithStreamingResponse(self)

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
    ) -> SubtitleUploadUploadResponse:
        """
        Upload `.srt` or `.vtt` file to the video asset. The response of this API call gives `upload_url` for each language specified. You need to send a `PUT` request of the subtitle files to those URLs. Once that's done, you need to call the subtitle upload complete API. Only after that, Gumlet will add subtitles to asset.

        Args:
            asset_id: An asset id for the previously created asset.
            language_codes: List of language codes to upload subtitle file (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubtitleUploadUploadResponse: 200

        Example:
            ```python
            subtitle_upload = client.subtitle_upload.upload(
                asset_id="assetId",
                language_codes=["en"],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_ID}/subtitle/upload", **{"asset_ID": asset_id}),
            body=maybe_transform(
                {"language_codes": language_codes},
                subtitle_upload_upload_params.SubtitleUploadUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleUploadUploadResponse,
        )

    def complete(
        self,
        asset_id: str,
        *,
        upload_responses: Iterable[subtitle_upload_complete_params.UploadResponse] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubtitleUploadCompleteResponse:
        """
        This API must be called after adding subtitles; the add subtitle call gives you URLs to upload, and you complete a `PUT` request to those URLs.
        Once that is done, calling this initiates the process to actually add the subtitle to the video.

        Args:
            asset_id: An asset id for the previously created asset.
            upload_responses: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubtitleUploadCompleteResponse: 200

        Example:
            ```python
            subtitle_upload = client.subtitle_upload.complete(
                asset_id="assetId",
                upload_responses=[{"language_code": "en", "uploaded": True}],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_ID}/subtitle/upload/event", **{"asset_ID": asset_id}),
            body=maybe_transform(
                {"upload_responses": upload_responses},
                subtitle_upload_complete_params.SubtitleUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleUploadCompleteResponse,
        )


class AsyncSubtitleUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubtitleUploadResourceWithRawResponse:
        return AsyncSubtitleUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubtitleUploadResourceWithStreamingResponse:
        return AsyncSubtitleUploadResourceWithStreamingResponse(self)

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
    ) -> SubtitleUploadUploadResponse:
        """
        Upload `.srt` or `.vtt` file to the video asset. The response of this API call gives `upload_url` for each language specified. You need to send a `PUT` request of the subtitle files to those URLs. Once that's done, you need to call the subtitle upload complete API. Only after that, Gumlet will add subtitles to asset.

        Args:
            asset_id: An asset id for the previously created asset.
            language_codes: List of language codes to upload subtitle file (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubtitleUploadUploadResponse: 200

        Example:
            ```python
            subtitle_upload = await client.subtitle_upload.upload(
                asset_id="assetId",
                language_codes=["en"],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_ID}/subtitle/upload", **{"asset_ID": asset_id}),
            body=await async_maybe_transform(
                {"language_codes": language_codes},
                subtitle_upload_upload_params.SubtitleUploadUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleUploadUploadResponse,
        )

    async def complete(
        self,
        asset_id: str,
        *,
        upload_responses: Iterable[subtitle_upload_complete_params.UploadResponse] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubtitleUploadCompleteResponse:
        """
        This API must be called after adding subtitles; the add subtitle call gives you URLs to upload, and you complete a `PUT` request to those URLs.
        Once that is done, calling this initiates the process to actually add the subtitle to the video.

        Args:
            asset_id: An asset id for the previously created asset.
            upload_responses: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubtitleUploadCompleteResponse: 200

        Example:
            ```python
            subtitle_upload = await client.subtitle_upload.complete(
                asset_id="assetId",
                upload_responses=[{"language_code": "en", "uploaded": True}],
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_ID}/subtitle/upload/event", **{"asset_ID": asset_id}),
            body=await async_maybe_transform(
                {"upload_responses": upload_responses},
                subtitle_upload_complete_params.SubtitleUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtitleUploadCompleteResponse,
        )


class SubtitleUploadResourceWithRawResponse:
    def __init__(self, subtitle_upload: SubtitleUploadResource) -> None:
        self._subtitle_upload = subtitle_upload

        self.upload = to_raw_response_wrapper(
            subtitle_upload.upload,
        )
        self.complete = to_raw_response_wrapper(
            subtitle_upload.complete,
        )


class AsyncSubtitleUploadResourceWithRawResponse:
    def __init__(self, subtitle_upload: AsyncSubtitleUploadResource) -> None:
        self._subtitle_upload = subtitle_upload

        self.upload = async_to_raw_response_wrapper(
            subtitle_upload.upload,
        )
        self.complete = async_to_raw_response_wrapper(
            subtitle_upload.complete,
        )


class SubtitleUploadResourceWithStreamingResponse:
    def __init__(self, subtitle_upload: SubtitleUploadResource) -> None:
        self._subtitle_upload = subtitle_upload

        self.upload = to_streamed_response_wrapper(
            subtitle_upload.upload,
        )
        self.complete = to_streamed_response_wrapper(
            subtitle_upload.complete,
        )


class AsyncSubtitleUploadResourceWithStreamingResponse:
    def __init__(self, subtitle_upload: AsyncSubtitleUploadResource) -> None:
        self._subtitle_upload = subtitle_upload

        self.upload = async_to_streamed_response_wrapper(
            subtitle_upload.upload,
        )
        self.complete = async_to_streamed_response_wrapper(
            subtitle_upload.complete,
        )
