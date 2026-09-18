# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable
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
from ..types.image_source_create_response import ImageSourceCreateResponse
from ..types import (
    image_source_create_params,
    image_source_list_params,
    image_source_update_params,
    image_source_purge_cache_params,
    image_source_purge_params,
)
from ..types.image_source_list_response import ImageSourceListResponse
from ..types.image_source_retrieve_response import ImageSourceRetrieveResponse
from ..types.image_source_update_response import ImageSourceUpdateResponse
from ..types.image_source_delete_response import ImageSourceDeleteResponse
from ..types.image_source_purge_cache_response import ImageSourcePurgeCacheResponse
from ..types.image_source_purge_response import ImageSourcePurgeResponse

__all__ = ["ImageSourcesResource", "AsyncImageSourcesResource"]


class ImageSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageSourcesResourceWithRawResponse:
        return ImageSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageSourcesResourceWithStreamingResponse:
        return ImageSourcesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        namespace: str,
        type: Literal[
            "proxy",
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
        aws: image_source_create_params.Aws | Omit = omit,
        proxy: image_source_create_params.Proxy | Omit = omit,
        gcs: image_source_create_params.Gcs | Omit = omit,
        dostorage: image_source_create_params.Dostorage | Omit = omit,
        wasabi: image_source_create_params.Wasabi | Omit = omit,
        cloudinary: image_source_create_params.Cloudinary | Omit = omit,
        azure: image_source_create_params.Azure | Omit = omit,
        linode: image_source_create_params.Linode | Omit = omit,
        backblaze: image_source_create_params.Backblaze | Omit = omit,
        cloudflare: image_source_create_params.Cloudflare | Omit = omit,
        webfolder: image_source_create_params.Webfolder | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceCreateResponse:
        """
        This endpoint allows users to create image source.

        Args:
            namespace: unique subdomain associated with the image source
            type: Body parameter.
            aws: This is a required field if source type is aws.
            proxy: This is a required field if source type is proxy.
            gcs: This is a required field if source type is gcs.
            dostorage: This is a required field if source type is dostorage.
            wasabi: This is a required field if source type is wasabi.
            cloudinary: This is a required field if source type is cloudinary.
            azure: This is a required field if source type is azure.
            linode: This is a required field if source type is linode.
            backblaze: This is a required field if source type is backblaze.
            cloudflare: This is a required field if source type is cloudflare.
            webfolder: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceCreateResponse: 200

        Example:
            ```python
            image_source = client.image_sources.create(
                namespace="google-demo",
                type="webfolder",
                webfolder={"base_url": "https://www.google.com"},
            )
            ```
        """
        return self._post(
            "/image/sources",
            body=maybe_transform(
                {
                    "namespace": namespace,
                    "type": type,
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
                    "webfolder": webfolder,
                },
                image_source_create_params.ImageSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceCreateResponse,
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
    ) -> ImageSourceListResponse:
        """
        This endpoint list image sources which are assigned to the user or token.

        Args:
            offset: Skip number of items. Helpful for pagination.
            size: Results per page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceListResponse: List all image sources

        Example:
            ```python
            image_source = client.image_sources.list(
                offset=0,
                size=20,
            )
            ```
        """
        return self._get(
            "/image/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"offset": offset, "size": size}, image_source_list_params.ImageSourceListParams),
            ),
            cast_to=ImageSourceListResponse,
        )

    def retrieve(
        self,
        image_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceRetrieveResponse:
        """
        Get all details about image source.

        Args:
            image_source_id: Image source id. You can get it on Gumlet dashboard or using list sources API endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceRetrieveResponse

        Example:
            ```python
            image_source = client.image_sources.retrieve(
                image_source_id="imageSourceId",
            )
            ```
        """
        if image_source_id is None or (isinstance(image_source_id, str) and not image_source_id):
            raise ValueError(f"Expected a non-empty value for `image_source_id` but received {image_source_id!r}")
        return self._get(
            path_template("/image/sources/{image_source_id}", **{"image_source_id": image_source_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceRetrieveResponse,
        )

    def update(
        self,
        image_source_id: str,
        *,
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
        ]
        | Omit = omit,
        webfolder: image_source_update_params.Webfolder | Omit = omit,
        aws: image_source_update_params.Aws | Omit = omit,
        proxy: image_source_update_params.Proxy | Omit = omit,
        gcs: image_source_update_params.Gcs | Omit = omit,
        dostorage: image_source_update_params.Dostorage | Omit = omit,
        wasabi: image_source_update_params.Wasabi | Omit = omit,
        linode: image_source_update_params.Linode | Omit = omit,
        backblaze: image_source_update_params.Backblaze | Omit = omit,
        cloudflare: image_source_update_params.Cloudflare | Omit = omit,
        cloudinary: image_source_update_params.Cloudinary | Omit = omit,
        azure: image_source_update_params.Azure | Omit = omit,
        default_params: object | Omit = omit,
        error_image: str | Omit = omit,
        request_headers: Iterable[object] | Omit = omit,
        response_headers: Iterable[object] | Omit = omit,
        temp_cname: SequenceNotStr[str] | Omit = omit,
        browser_cache_time: int | Omit = omit,
        cdn_cache_time: int | Omit = omit,
        is_active: bool | Omit = omit,
        cname: SequenceNotStr[str] | Omit = omit,
        fallback_origins: Iterable[image_source_update_params.FallbackOrigin] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceUpdateResponse:
        """
        This endpoint allows users to update image source that has previously been created.

        Args:
            image_source_id: image source id which you want to update
            type: Body parameter.
            webfolder: This is a required field if source type is webfolder.
            aws: This is a required field if source type is aws.
            proxy: This is a required field if source type is proxy.
            gcs: This is a required field if source type is gcs.
            dostorage: This is a required field if source type is dostorage.
            wasabi: This is a required field if source type is wasabi.
            linode: This is a required field if source type is linode.
            backblaze: This is a required field if source type is backblaze.
            cloudflare: This is a required field if source type is cloudflare.
            cloudinary: This is a required field if source type is cloudinary.
            azure: This is a required field if source type is azure.
            default_params: Body parameter.
            error_image: URL for error image to display when we get broken image from your origin.
            request_headers: Body parameter.
            response_headers: Body parameter.
            temp_cname: Body parameter.
            browser_cache_time: Browser cache time in seconds. For example setting this to 3600 caches the image in browser for 3600 seconds (1 hour)
            cdn_cache_time: CDN cache time in seconds.
            is_active: Enable / disable source.
            cname: List of verified CNAMEs
            fallback_origins: List of fallback origins
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceUpdateResponse: 200

        Example:
            ```python
            image_source = client.image_sources.update(
                image_source_id="imageSourceId",
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
        if image_source_id is None or (isinstance(image_source_id, str) and not image_source_id):
            raise ValueError(f"Expected a non-empty value for `image_source_id` but received {image_source_id!r}")
        return self._post(
            path_template("/image/sources/{image_source_id}", **{"image_source_id": image_source_id}),
            body=maybe_transform(
                {
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
                    "default_params": default_params,
                    "error_image": error_image,
                    "request_headers": request_headers,
                    "response_headers": response_headers,
                    "temp_cname": temp_cname,
                    "browser_cache_time": browser_cache_time,
                    "cdn_cache_time": cdn_cache_time,
                    "is_active": is_active,
                    "cname": cname,
                    "fallback_origins": fallback_origins,
                },
                image_source_update_params.ImageSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceUpdateResponse,
        )

    def delete(
        self,
        image_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceDeleteResponse:
        """
        This endpoint removes a image source. All image delivery using this subdomain will be stopped.

        Args:
            image_source_id: Image source ID to delete. You can get this on Gumlet dashboard or in list source API.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceDeleteResponse

        Example:
            ```python
            image_source = client.image_sources.delete(
                image_source_id="imageSourceId",
            )
            ```
        """
        if image_source_id is None or (isinstance(image_source_id, str) and not image_source_id):
            raise ValueError(f"Expected a non-empty value for `image_source_id` but received {image_source_id!r}")
        return self._delete(
            path_template("/image/sources/{image_source_id}", **{"image_source_id": image_source_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceDeleteResponse,
        )

    def purge_cache(
        self,
        subdomain: str,
        *,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourcePurgeCacheResponse:
        """
        You can purge cache for any image by using our cache purge API.

        Args:
            subdomain: Subdomain is same subdomain you created while creating source. If you serve image from example.gumlet.com, please enter only 'example' for this parameter.
            paths: An array of path of images to purge. It should be provided without any query parameters.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourcePurgeCacheResponse: 200

        Example:
            ```python
            image_source = client.image_sources.purge_cache(
                subdomain="subdomain",
                paths=["image.jpeg", "image2.png"],
            )
            ```

        Deprecated: this method is deprecated.
        """
        if subdomain is None or (isinstance(subdomain, str) and not subdomain):
            raise ValueError(f"Expected a non-empty value for `subdomain` but received {subdomain!r}")
        return self._post(
            path_template("/purge/{subdomain}", **{"subdomain": subdomain}),
            body=maybe_transform(
                {"paths": paths},
                image_source_purge_cache_params.ImageSourcePurgeCacheParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourcePurgeCacheResponse,
        )

    def purge(
        self,
        source_id: str,
        *,
        paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourcePurgeResponse:
        """
        You can purge the cache for any image path by using this cache purge API.

        Args:
            source_id: Image Source ID
            paths: An array of path of images to purge. It should be provided without any query parameters.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourcePurgeResponse: Successful response

        Example:
            ```python
            image_source = client.image_sources.purge(
                source_id="sourceId",
                paths=["image.jpeg", "image2.png"],
            )
            ```
        """
        if source_id is None or (isinstance(source_id, str) and not source_id):
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._post(
            path_template("/image/purge/{source_id}", **{"source_id": source_id}),
            body=maybe_transform(
                {"paths": paths},
                image_source_purge_params.ImageSourcePurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourcePurgeResponse,
        )


class AsyncImageSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageSourcesResourceWithRawResponse:
        return AsyncImageSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageSourcesResourceWithStreamingResponse:
        return AsyncImageSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        namespace: str,
        type: Literal[
            "proxy",
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
        aws: image_source_create_params.Aws | Omit = omit,
        proxy: image_source_create_params.Proxy | Omit = omit,
        gcs: image_source_create_params.Gcs | Omit = omit,
        dostorage: image_source_create_params.Dostorage | Omit = omit,
        wasabi: image_source_create_params.Wasabi | Omit = omit,
        cloudinary: image_source_create_params.Cloudinary | Omit = omit,
        azure: image_source_create_params.Azure | Omit = omit,
        linode: image_source_create_params.Linode | Omit = omit,
        backblaze: image_source_create_params.Backblaze | Omit = omit,
        cloudflare: image_source_create_params.Cloudflare | Omit = omit,
        webfolder: image_source_create_params.Webfolder | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceCreateResponse:
        """
        This endpoint allows users to create image source.

        Args:
            namespace: unique subdomain associated with the image source
            type: Body parameter.
            aws: This is a required field if source type is aws.
            proxy: This is a required field if source type is proxy.
            gcs: This is a required field if source type is gcs.
            dostorage: This is a required field if source type is dostorage.
            wasabi: This is a required field if source type is wasabi.
            cloudinary: This is a required field if source type is cloudinary.
            azure: This is a required field if source type is azure.
            linode: This is a required field if source type is linode.
            backblaze: This is a required field if source type is backblaze.
            cloudflare: This is a required field if source type is cloudflare.
            webfolder: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceCreateResponse: 200

        Example:
            ```python
            image_source = await client.image_sources.create(
                namespace="google-demo",
                type="webfolder",
                webfolder={"base_url": "https://www.google.com"},
            )
            ```
        """
        return await self._post(
            "/image/sources",
            body=await async_maybe_transform(
                {
                    "namespace": namespace,
                    "type": type,
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
                    "webfolder": webfolder,
                },
                image_source_create_params.ImageSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceCreateResponse,
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
    ) -> ImageSourceListResponse:
        """
        This endpoint list image sources which are assigned to the user or token.

        Args:
            offset: Skip number of items. Helpful for pagination.
            size: Results per page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceListResponse: List all image sources

        Example:
            ```python
            image_source = await client.image_sources.list(
                offset=0,
                size=20,
            )
            ```
        """
        return await self._get(
            "/image/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"offset": offset, "size": size}, image_source_list_params.ImageSourceListParams
                ),
            ),
            cast_to=ImageSourceListResponse,
        )

    async def retrieve(
        self,
        image_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceRetrieveResponse:
        """
        Get all details about image source.

        Args:
            image_source_id: Image source id. You can get it on Gumlet dashboard or using list sources API endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceRetrieveResponse

        Example:
            ```python
            image_source = await client.image_sources.retrieve(
                image_source_id="imageSourceId",
            )
            ```
        """
        if image_source_id is None or (isinstance(image_source_id, str) and not image_source_id):
            raise ValueError(f"Expected a non-empty value for `image_source_id` but received {image_source_id!r}")
        return await self._get(
            path_template("/image/sources/{image_source_id}", **{"image_source_id": image_source_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceRetrieveResponse,
        )

    async def update(
        self,
        image_source_id: str,
        *,
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
        ]
        | Omit = omit,
        webfolder: image_source_update_params.Webfolder | Omit = omit,
        aws: image_source_update_params.Aws | Omit = omit,
        proxy: image_source_update_params.Proxy | Omit = omit,
        gcs: image_source_update_params.Gcs | Omit = omit,
        dostorage: image_source_update_params.Dostorage | Omit = omit,
        wasabi: image_source_update_params.Wasabi | Omit = omit,
        linode: image_source_update_params.Linode | Omit = omit,
        backblaze: image_source_update_params.Backblaze | Omit = omit,
        cloudflare: image_source_update_params.Cloudflare | Omit = omit,
        cloudinary: image_source_update_params.Cloudinary | Omit = omit,
        azure: image_source_update_params.Azure | Omit = omit,
        default_params: object | Omit = omit,
        error_image: str | Omit = omit,
        request_headers: Iterable[object] | Omit = omit,
        response_headers: Iterable[object] | Omit = omit,
        temp_cname: SequenceNotStr[str] | Omit = omit,
        browser_cache_time: int | Omit = omit,
        cdn_cache_time: int | Omit = omit,
        is_active: bool | Omit = omit,
        cname: SequenceNotStr[str] | Omit = omit,
        fallback_origins: Iterable[image_source_update_params.FallbackOrigin] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceUpdateResponse:
        """
        This endpoint allows users to update image source that has previously been created.

        Args:
            image_source_id: image source id which you want to update
            type: Body parameter.
            webfolder: This is a required field if source type is webfolder.
            aws: This is a required field if source type is aws.
            proxy: This is a required field if source type is proxy.
            gcs: This is a required field if source type is gcs.
            dostorage: This is a required field if source type is dostorage.
            wasabi: This is a required field if source type is wasabi.
            linode: This is a required field if source type is linode.
            backblaze: This is a required field if source type is backblaze.
            cloudflare: This is a required field if source type is cloudflare.
            cloudinary: This is a required field if source type is cloudinary.
            azure: This is a required field if source type is azure.
            default_params: Body parameter.
            error_image: URL for error image to display when we get broken image from your origin.
            request_headers: Body parameter.
            response_headers: Body parameter.
            temp_cname: Body parameter.
            browser_cache_time: Browser cache time in seconds. For example setting this to 3600 caches the image in browser for 3600 seconds (1 hour)
            cdn_cache_time: CDN cache time in seconds.
            is_active: Enable / disable source.
            cname: List of verified CNAMEs
            fallback_origins: List of fallback origins
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceUpdateResponse: 200

        Example:
            ```python
            image_source = await client.image_sources.update(
                image_source_id="imageSourceId",
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
        if image_source_id is None or (isinstance(image_source_id, str) and not image_source_id):
            raise ValueError(f"Expected a non-empty value for `image_source_id` but received {image_source_id!r}")
        return await self._post(
            path_template("/image/sources/{image_source_id}", **{"image_source_id": image_source_id}),
            body=await async_maybe_transform(
                {
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
                    "default_params": default_params,
                    "error_image": error_image,
                    "request_headers": request_headers,
                    "response_headers": response_headers,
                    "temp_cname": temp_cname,
                    "browser_cache_time": browser_cache_time,
                    "cdn_cache_time": cdn_cache_time,
                    "is_active": is_active,
                    "cname": cname,
                    "fallback_origins": fallback_origins,
                },
                image_source_update_params.ImageSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceUpdateResponse,
        )

    async def delete(
        self,
        image_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourceDeleteResponse:
        """
        This endpoint removes a image source. All image delivery using this subdomain will be stopped.

        Args:
            image_source_id: Image source ID to delete. You can get this on Gumlet dashboard or in list source API.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourceDeleteResponse

        Example:
            ```python
            image_source = await client.image_sources.delete(
                image_source_id="imageSourceId",
            )
            ```
        """
        if image_source_id is None or (isinstance(image_source_id, str) and not image_source_id):
            raise ValueError(f"Expected a non-empty value for `image_source_id` but received {image_source_id!r}")
        return await self._delete(
            path_template("/image/sources/{image_source_id}", **{"image_source_id": image_source_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourceDeleteResponse,
        )

    async def purge_cache(
        self,
        subdomain: str,
        *,
        paths: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourcePurgeCacheResponse:
        """
        You can purge cache for any image by using our cache purge API.

        Args:
            subdomain: Subdomain is same subdomain you created while creating source. If you serve image from example.gumlet.com, please enter only 'example' for this parameter.
            paths: An array of path of images to purge. It should be provided without any query parameters.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourcePurgeCacheResponse: 200

        Example:
            ```python
            image_source = await client.image_sources.purge_cache(
                subdomain="subdomain",
                paths=["image.jpeg", "image2.png"],
            )
            ```

        Deprecated: this method is deprecated.
        """
        if subdomain is None or (isinstance(subdomain, str) and not subdomain):
            raise ValueError(f"Expected a non-empty value for `subdomain` but received {subdomain!r}")
        return await self._post(
            path_template("/purge/{subdomain}", **{"subdomain": subdomain}),
            body=await async_maybe_transform(
                {"paths": paths},
                image_source_purge_cache_params.ImageSourcePurgeCacheParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourcePurgeCacheResponse,
        )

    async def purge(
        self,
        source_id: str,
        *,
        paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageSourcePurgeResponse:
        """
        You can purge the cache for any image path by using this cache purge API.

        Args:
            source_id: Image Source ID
            paths: An array of path of images to purge. It should be provided without any query parameters.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageSourcePurgeResponse: Successful response

        Example:
            ```python
            image_source = await client.image_sources.purge(
                source_id="sourceId",
                paths=["image.jpeg", "image2.png"],
            )
            ```
        """
        if source_id is None or (isinstance(source_id, str) and not source_id):
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._post(
            path_template("/image/purge/{source_id}", **{"source_id": source_id}),
            body=await async_maybe_transform(
                {"paths": paths},
                image_source_purge_params.ImageSourcePurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageSourcePurgeResponse,
        )


class ImageSourcesResourceWithRawResponse:
    def __init__(self, image_sources: ImageSourcesResource) -> None:
        self._image_sources = image_sources

        self.create = to_raw_response_wrapper(
            image_sources.create,
        )
        self.list = to_raw_response_wrapper(
            image_sources.list,
        )
        self.retrieve = to_raw_response_wrapper(
            image_sources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            image_sources.update,
        )
        self.delete = to_raw_response_wrapper(
            image_sources.delete,
        )
        self.purge_cache = to_raw_response_wrapper(
            image_sources.purge_cache,
        )
        self.purge = to_raw_response_wrapper(
            image_sources.purge,
        )


class AsyncImageSourcesResourceWithRawResponse:
    def __init__(self, image_sources: AsyncImageSourcesResource) -> None:
        self._image_sources = image_sources

        self.create = async_to_raw_response_wrapper(
            image_sources.create,
        )
        self.list = async_to_raw_response_wrapper(
            image_sources.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            image_sources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            image_sources.update,
        )
        self.delete = async_to_raw_response_wrapper(
            image_sources.delete,
        )
        self.purge_cache = async_to_raw_response_wrapper(
            image_sources.purge_cache,
        )
        self.purge = async_to_raw_response_wrapper(
            image_sources.purge,
        )


class ImageSourcesResourceWithStreamingResponse:
    def __init__(self, image_sources: ImageSourcesResource) -> None:
        self._image_sources = image_sources

        self.create = to_streamed_response_wrapper(
            image_sources.create,
        )
        self.list = to_streamed_response_wrapper(
            image_sources.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            image_sources.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            image_sources.update,
        )
        self.delete = to_streamed_response_wrapper(
            image_sources.delete,
        )
        self.purge_cache = to_streamed_response_wrapper(
            image_sources.purge_cache,
        )
        self.purge = to_streamed_response_wrapper(
            image_sources.purge,
        )


class AsyncImageSourcesResourceWithStreamingResponse:
    def __init__(self, image_sources: AsyncImageSourcesResource) -> None:
        self._image_sources = image_sources

        self.create = async_to_streamed_response_wrapper(
            image_sources.create,
        )
        self.list = async_to_streamed_response_wrapper(
            image_sources.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            image_sources.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            image_sources.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            image_sources.delete,
        )
        self.purge_cache = async_to_streamed_response_wrapper(
            image_sources.purge_cache,
        )
        self.purge = async_to_streamed_response_wrapper(
            image_sources.purge,
        )
