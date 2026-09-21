# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.video_usage_analytic_retrieve_response import VideoUsageAnalyticRetrieveResponse
from ..types import video_usage_analytic_retrieve_params, video_usage_analytic_top_assets_params
from ..types.video_usage_analytic_top_assets_response import VideoUsageAnalyticTopAssetsResponse

__all__ = ["VideoUsageAnalyticsResource", "AsyncVideoUsageAnalyticsResource"]


class VideoUsageAnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoUsageAnalyticsResourceWithRawResponse:
        return VideoUsageAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoUsageAnalyticsResourceWithStreamingResponse:
        return VideoUsageAnalyticsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        metrics: List[
            Literal[
                "bandwidth_consumption",
                "asset_duration",
                "storage_unit",
                "top_assets",
                "drm_requests",
                "ai_credit_usage",
                "errored_videos",
            ]
        ],
        date_range: video_usage_analytic_retrieve_params.DateRange,
        filters: video_usage_analytic_retrieve_params.Filters | Omit = omit,
        top_assets_count: str | Omit = omit,
        top_assets_page: str | Omit = omit,
        group_by: Literal["hourly", "daily", "monthly"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoUsageAnalyticRetrieveResponse:
        """
        This endpoint gives usage analytics data of your videos. Ex - top assets, bandwidth consumption

        Args:
            metrics: Define the metric you need the data for. Currently we only support `bandwidth_consumption`, `asset_duration`, `storage_unit`, `top_assets`, `bandwidth_consumption_by_collection`, `errored_videos` and `widget_data`
            date_range: The timeframe to get the data for. Currently we only support a maximum of 60 days between `start_at` and `end_at`.
            filters: Body parameter.
            top_assets_count: Count of video assets that should be returned. Max assets count is 1000 per page.
            top_assets_page: top_assets metric may get paginated response. Iterate this parameter to get more data.
            group_by: Group by hourly, daily or monthly. If you don't specify anything it's `hourly` by default.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoUsageAnalyticRetrieveResponse: 200

        Example:
            ```python
            video_usage_analytic = client.video_usage_analytics.retrieve(
                metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
                date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
                top_assets_count="5",
                top_assets_page="0",
                group_by="hourly",
            )
            ```
        """
        return self._post(
            "/video/analytics",
            body=maybe_transform(
                {
                    "metrics": metrics,
                    "date_range": date_range,
                    "filters": filters,
                    "top_assets_count": top_assets_count,
                    "top_assets_page": top_assets_page,
                    "group_by": group_by,
                },
                video_usage_analytic_retrieve_params.VideoUsageAnalyticRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoUsageAnalyticRetrieveResponse,
        )

    def top_assets(
        self,
        *,
        start_at: str,
        end_at: str,
        collection_id: str | Omit = omit,
        page: str | Omit = omit,
        page_size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoUsageAnalyticTopAssetsResponse:
        """
        This endpoint lists top streamed assets in a video collection

        Args:
            start_at: Date string in "yyyy-mm-dd" format
            end_at: Date string in "yyyy-mm-dd" format
            collection_id: Gumlet workspace ID
            page: Page number of the response.
            page_size: Assets to list per page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoUsageAnalyticTopAssetsResponse: 200

        Example:
            ```python
            video_usage_analytic = client.video_usage_analytics.top_assets(
                start_at="2026-06-21",
                end_at="2026-06-30",
                page="1",
                page_size="1000",
            )
            ```
        """
        return self._get(
            "/video/streaming-duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_at": start_at,
                        "end_at": end_at,
                        "collection_id": collection_id,
                        "page": page,
                        "page_size": page_size,
                    },
                    video_usage_analytic_top_assets_params.VideoUsageAnalyticTopAssetsParams,
                ),
            ),
            cast_to=VideoUsageAnalyticTopAssetsResponse,
        )


class AsyncVideoUsageAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoUsageAnalyticsResourceWithRawResponse:
        return AsyncVideoUsageAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoUsageAnalyticsResourceWithStreamingResponse:
        return AsyncVideoUsageAnalyticsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        metrics: List[
            Literal[
                "bandwidth_consumption",
                "asset_duration",
                "storage_unit",
                "top_assets",
                "drm_requests",
                "ai_credit_usage",
                "errored_videos",
            ]
        ],
        date_range: video_usage_analytic_retrieve_params.DateRange,
        filters: video_usage_analytic_retrieve_params.Filters | Omit = omit,
        top_assets_count: str | Omit = omit,
        top_assets_page: str | Omit = omit,
        group_by: Literal["hourly", "daily", "monthly"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoUsageAnalyticRetrieveResponse:
        """
        This endpoint gives usage analytics data of your videos. Ex - top assets, bandwidth consumption

        Args:
            metrics: Define the metric you need the data for. Currently we only support `bandwidth_consumption`, `asset_duration`, `storage_unit`, `top_assets`, `bandwidth_consumption_by_collection`, `errored_videos` and `widget_data`
            date_range: The timeframe to get the data for. Currently we only support a maximum of 60 days between `start_at` and `end_at`.
            filters: Body parameter.
            top_assets_count: Count of video assets that should be returned. Max assets count is 1000 per page.
            top_assets_page: top_assets metric may get paginated response. Iterate this parameter to get more data.
            group_by: Group by hourly, daily or monthly. If you don't specify anything it's `hourly` by default.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoUsageAnalyticRetrieveResponse: 200

        Example:
            ```python
            video_usage_analytic = await client.video_usage_analytics.retrieve(
                metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
                date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
                top_assets_count="5",
                top_assets_page="0",
                group_by="hourly",
            )
            ```
        """
        return await self._post(
            "/video/analytics",
            body=await async_maybe_transform(
                {
                    "metrics": metrics,
                    "date_range": date_range,
                    "filters": filters,
                    "top_assets_count": top_assets_count,
                    "top_assets_page": top_assets_page,
                    "group_by": group_by,
                },
                video_usage_analytic_retrieve_params.VideoUsageAnalyticRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoUsageAnalyticRetrieveResponse,
        )

    async def top_assets(
        self,
        *,
        start_at: str,
        end_at: str,
        collection_id: str | Omit = omit,
        page: str | Omit = omit,
        page_size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoUsageAnalyticTopAssetsResponse:
        """
        This endpoint lists top streamed assets in a video collection

        Args:
            start_at: Date string in "yyyy-mm-dd" format
            end_at: Date string in "yyyy-mm-dd" format
            collection_id: Gumlet workspace ID
            page: Page number of the response.
            page_size: Assets to list per page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoUsageAnalyticTopAssetsResponse: 200

        Example:
            ```python
            video_usage_analytic = await client.video_usage_analytics.top_assets(
                start_at="2026-06-21",
                end_at="2026-06-30",
                page="1",
                page_size="1000",
            )
            ```
        """
        return await self._get(
            "/video/streaming-duration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_at": start_at,
                        "end_at": end_at,
                        "collection_id": collection_id,
                        "page": page,
                        "page_size": page_size,
                    },
                    video_usage_analytic_top_assets_params.VideoUsageAnalyticTopAssetsParams,
                ),
            ),
            cast_to=VideoUsageAnalyticTopAssetsResponse,
        )


class VideoUsageAnalyticsResourceWithRawResponse:
    def __init__(self, video_usage_analytics: VideoUsageAnalyticsResource) -> None:
        self._video_usage_analytics = video_usage_analytics

        self.retrieve = to_raw_response_wrapper(
            video_usage_analytics.retrieve,
        )
        self.top_assets = to_raw_response_wrapper(
            video_usage_analytics.top_assets,
        )


class AsyncVideoUsageAnalyticsResourceWithRawResponse:
    def __init__(self, video_usage_analytics: AsyncVideoUsageAnalyticsResource) -> None:
        self._video_usage_analytics = video_usage_analytics

        self.retrieve = async_to_raw_response_wrapper(
            video_usage_analytics.retrieve,
        )
        self.top_assets = async_to_raw_response_wrapper(
            video_usage_analytics.top_assets,
        )


class VideoUsageAnalyticsResourceWithStreamingResponse:
    def __init__(self, video_usage_analytics: VideoUsageAnalyticsResource) -> None:
        self._video_usage_analytics = video_usage_analytics

        self.retrieve = to_streamed_response_wrapper(
            video_usage_analytics.retrieve,
        )
        self.top_assets = to_streamed_response_wrapper(
            video_usage_analytics.top_assets,
        )


class AsyncVideoUsageAnalyticsResourceWithStreamingResponse:
    def __init__(self, video_usage_analytics: AsyncVideoUsageAnalyticsResource) -> None:
        self._video_usage_analytics = video_usage_analytics

        self.retrieve = async_to_streamed_response_wrapper(
            video_usage_analytics.retrieve,
        )
        self.top_assets = async_to_streamed_response_wrapper(
            video_usage_analytics.top_assets,
        )
