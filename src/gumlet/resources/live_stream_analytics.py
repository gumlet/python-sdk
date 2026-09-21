# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
from typing_extensions import Literal

from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.live_stream_analytic_usage_response import LiveStreamAnalyticUsageResponse
from ..types import live_stream_analytic_usage_params

__all__ = ["LiveStreamAnalyticsResource", "AsyncLiveStreamAnalyticsResource"]


class LiveStreamAnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveStreamAnalyticsResourceWithRawResponse:
        return LiveStreamAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveStreamAnalyticsResourceWithStreamingResponse:
        return LiveStreamAnalyticsResourceWithStreamingResponse(self)

    def usage(
        self,
        *,
        date_range: live_stream_analytic_usage_params.DateRange,
        group_by: Literal["daily", "weekly", "monthly"],
        metrics: List[Literal["bandwidth_consumption", "asset_duration", "storage_unit"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAnalyticUsageResponse:
        """
        Get usage analytics for your live streams.

        Args:
            date_range: Body parameter.
            group_by: Group the data either weekly, daily or monthly
            metrics: List of metrics required in response
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAnalyticUsageResponse: Successful response

        Example:
            ```python
            live_stream_analytic = client.live_stream_analytics.usage(
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                group_by="daily",
                metrics=["bandwidth_consumption"],
            )
            ```
        """
        return self._post(
            "/video/live/analytics",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "group_by": group_by,
                    "metrics": metrics,
                },
                live_stream_analytic_usage_params.LiveStreamAnalyticUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAnalyticUsageResponse,
        )


class AsyncLiveStreamAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveStreamAnalyticsResourceWithRawResponse:
        return AsyncLiveStreamAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveStreamAnalyticsResourceWithStreamingResponse:
        return AsyncLiveStreamAnalyticsResourceWithStreamingResponse(self)

    async def usage(
        self,
        *,
        date_range: live_stream_analytic_usage_params.DateRange,
        group_by: Literal["daily", "weekly", "monthly"],
        metrics: List[Literal["bandwidth_consumption", "asset_duration", "storage_unit"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveStreamAnalyticUsageResponse:
        """
        Get usage analytics for your live streams.

        Args:
            date_range: Body parameter.
            group_by: Group the data either weekly, daily or monthly
            metrics: List of metrics required in response
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveStreamAnalyticUsageResponse: Successful response

        Example:
            ```python
            live_stream_analytic = await client.live_stream_analytics.usage(
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                group_by="daily",
                metrics=["bandwidth_consumption"],
            )
            ```
        """
        return await self._post(
            "/video/live/analytics",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "group_by": group_by,
                    "metrics": metrics,
                },
                live_stream_analytic_usage_params.LiveStreamAnalyticUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveStreamAnalyticUsageResponse,
        )


class LiveStreamAnalyticsResourceWithRawResponse:
    def __init__(self, live_stream_analytics: LiveStreamAnalyticsResource) -> None:
        self._live_stream_analytics = live_stream_analytics

        self.usage = to_raw_response_wrapper(
            live_stream_analytics.usage,
        )


class AsyncLiveStreamAnalyticsResourceWithRawResponse:
    def __init__(self, live_stream_analytics: AsyncLiveStreamAnalyticsResource) -> None:
        self._live_stream_analytics = live_stream_analytics

        self.usage = async_to_raw_response_wrapper(
            live_stream_analytics.usage,
        )


class LiveStreamAnalyticsResourceWithStreamingResponse:
    def __init__(self, live_stream_analytics: LiveStreamAnalyticsResource) -> None:
        self._live_stream_analytics = live_stream_analytics

        self.usage = to_streamed_response_wrapper(
            live_stream_analytics.usage,
        )


class AsyncLiveStreamAnalyticsResourceWithStreamingResponse:
    def __init__(self, live_stream_analytics: AsyncLiveStreamAnalyticsResource) -> None:
        self._live_stream_analytics = live_stream_analytics

        self.usage = async_to_streamed_response_wrapper(
            live_stream_analytics.usage,
        )
