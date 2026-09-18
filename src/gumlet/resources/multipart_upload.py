# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable

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
from ..types.multipart_upload_retrieve_part_url_response import MultipartUploadRetrievePartURLResponse
from ..types.multipart_upload_complete_response import MultipartUploadCompleteResponse
from ..types import multipart_upload_complete_params

__all__ = ["MultipartUploadResource", "AsyncMultipartUploadResource"]


class MultipartUploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MultipartUploadResourceWithRawResponse:
        return MultipartUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultipartUploadResourceWithStreamingResponse:
        return MultipartUploadResourceWithStreamingResponse(self)

    def retrieve_part_url(
        self,
        part_number: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadRetrievePartURLResponse:
        """
        Use this endpoint to retrieve a pre-signed upload URL for the given part number.

        Args:
            part_number: Part number of multiple parts of the original video which you you are uploading
            asset_id: An asset id of the created asset for which you are uploading parts
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MultipartUploadRetrievePartURLResponse: 200

        Example:
            ```python
            multipart_upload = client.multipart_upload.retrieve_part_url(
                asset_id="assetId",
                part_number="partNumber",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if part_number is None or (isinstance(part_number, str) and not part_number):
            raise ValueError(f"Expected a non-empty value for `part_number` but received {part_number!r}")
        return self._get(
            path_template(
                "/video/assets/{asset_id}/multipartupload/{part_number}/sign",
                **{"asset_id": asset_id, "part_number": part_number},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadRetrievePartURLResponse,
        )

    def complete(
        self,
        asset_id: str,
        *,
        parts: Iterable[multipart_upload_complete_params.Part] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadCompleteResponse:
        """
        Once you upload all parts to S3 bucket via pre-signed URL, use this endpoint to complete the multipart upload.

        Args:
            asset_id: An asset id for which you are uploading original video via multipart
            parts: List of object containing part number with ETag received as a response header while uploading each part
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MultipartUploadCompleteResponse: 200

        Example:
            ```python
            multipart_upload = client.multipart_upload.complete(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/video/assets/{asset_id}/multipartupload/complete", **{"asset_id": asset_id}),
            body=maybe_transform(
                {"parts": parts},
                multipart_upload_complete_params.MultipartUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadCompleteResponse,
        )


class AsyncMultipartUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMultipartUploadResourceWithRawResponse:
        return AsyncMultipartUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultipartUploadResourceWithStreamingResponse:
        return AsyncMultipartUploadResourceWithStreamingResponse(self)

    async def retrieve_part_url(
        self,
        part_number: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadRetrievePartURLResponse:
        """
        Use this endpoint to retrieve a pre-signed upload URL for the given part number.

        Args:
            part_number: Part number of multiple parts of the original video which you you are uploading
            asset_id: An asset id of the created asset for which you are uploading parts
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MultipartUploadRetrievePartURLResponse: 200

        Example:
            ```python
            multipart_upload = await client.multipart_upload.retrieve_part_url(
                asset_id="assetId",
                part_number="partNumber",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if part_number is None or (isinstance(part_number, str) and not part_number):
            raise ValueError(f"Expected a non-empty value for `part_number` but received {part_number!r}")
        return await self._get(
            path_template(
                "/video/assets/{asset_id}/multipartupload/{part_number}/sign",
                **{"asset_id": asset_id, "part_number": part_number},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadRetrievePartURLResponse,
        )

    async def complete(
        self,
        asset_id: str,
        *,
        parts: Iterable[multipart_upload_complete_params.Part] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartUploadCompleteResponse:
        """
        Once you upload all parts to S3 bucket via pre-signed URL, use this endpoint to complete the multipart upload.

        Args:
            asset_id: An asset id for which you are uploading original video via multipart
            parts: List of object containing part number with ETag received as a response header while uploading each part
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MultipartUploadCompleteResponse: 200

        Example:
            ```python
            multipart_upload = await client.multipart_upload.complete(
                asset_id="assetId",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/video/assets/{asset_id}/multipartupload/complete", **{"asset_id": asset_id}),
            body=await async_maybe_transform(
                {"parts": parts},
                multipart_upload_complete_params.MultipartUploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartUploadCompleteResponse,
        )


class MultipartUploadResourceWithRawResponse:
    def __init__(self, multipart_upload: MultipartUploadResource) -> None:
        self._multipart_upload = multipart_upload

        self.retrieve_part_url = to_raw_response_wrapper(
            multipart_upload.retrieve_part_url,
        )
        self.complete = to_raw_response_wrapper(
            multipart_upload.complete,
        )


class AsyncMultipartUploadResourceWithRawResponse:
    def __init__(self, multipart_upload: AsyncMultipartUploadResource) -> None:
        self._multipart_upload = multipart_upload

        self.retrieve_part_url = async_to_raw_response_wrapper(
            multipart_upload.retrieve_part_url,
        )
        self.complete = async_to_raw_response_wrapper(
            multipart_upload.complete,
        )


class MultipartUploadResourceWithStreamingResponse:
    def __init__(self, multipart_upload: MultipartUploadResource) -> None:
        self._multipart_upload = multipart_upload

        self.retrieve_part_url = to_streamed_response_wrapper(
            multipart_upload.retrieve_part_url,
        )
        self.complete = to_streamed_response_wrapper(
            multipart_upload.complete,
        )


class AsyncMultipartUploadResourceWithStreamingResponse:
    def __init__(self, multipart_upload: AsyncMultipartUploadResource) -> None:
        self._multipart_upload = multipart_upload

        self.retrieve_part_url = async_to_streamed_response_wrapper(
            multipart_upload.retrieve_part_url,
        )
        self.complete = async_to_streamed_response_wrapper(
            multipart_upload.complete,
        )
