# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable
from typing_extensions import Literal
from .._types import SequenceNotStr

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
from ..types.video_analytic_chart_data_response import VideoAnalyticChartDataResponse
from ..types import (
    video_analytic_chart_data_params,
    video_analytic_breakdown_data_params,
    video_analytic_aggregated_data_params,
)
from ..types.video_analytic_breakdown_data_response import VideoAnalyticBreakdownDataResponse
from ..types.video_analytic_aggregated_data_response import VideoAnalyticAggregatedDataResponse

__all__ = ["VideoAnalyticsResource", "AsyncVideoAnalyticsResource"]


class VideoAnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoAnalyticsResourceWithRawResponse:
        return VideoAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoAnalyticsResourceWithStreamingResponse:
        return VideoAnalyticsResourceWithStreamingResponse(self)

    def chart_data(
        self,
        *,
        metrics: SequenceNotStr[str],
        workspace_id: str,
        date_range: video_analytic_chart_data_params.DateRange,
        filters: Iterable[video_analytic_chart_data_params.Filter] | Omit = omit,
        group_by: Literal["daily", "weekly", "monthly"] | Omit = omit,
        chart_dimension: video_analytic_chart_data_params.ChartDimension | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAnalyticChartDataResponse:
        """
        This endpoint retrieves viewer analytics data. This endpoint is use for deep insights on the analytics data.

        Args:
            metrics: Get data for one or more `metrics` in the same request. Please add any of these metrics. `views`, `unique_views`, `impressions`. `completion_percent_by_views`, `playing_time`, `concurrent_users`, `widget_form_submitted`, `cta_clicks`
            workspace_id: The five to ten character unique identifier of the Gumlet workspace ID available on the Video Workspaces.
            date_range: The timeframe to get the data for.
            filters: Build *segments* of users using multiple filters on the data, `value` should be an *exact match*
            group_by: Data can be grouped by `daily`, `weekly` or `monthly`.
            chart_dimension: Metrics result Group by selected dimension, You can select upto 3 dimensions to get nested category result. result will follow selection orders.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAnalyticChartDataResponse: 200

        Example:
            ```python
            video_analytic = client.video_analytics.chart_data(
                metrics=[""],
                workspace_id="",
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                group_by="daily",
            )
            ```
        """
        return self._post(
            "/insights/viewer-analytics",
            body=maybe_transform(
                {
                    "metrics": metrics,
                    "workspace_id": workspace_id,
                    "date_range": date_range,
                    "filters": filters,
                    "group_by": group_by,
                    "chart_dimension": chart_dimension,
                },
                video_analytic_chart_data_params.VideoAnalyticChartDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAnalyticChartDataResponse,
        )

    def breakdown_data(
        self,
        *,
        date_range: video_analytic_breakdown_data_params.DateRange,
        filters: Iterable[video_analytic_breakdown_data_params.Filter] | Omit = omit,
        breakdowns: Iterable[video_analytic_breakdown_data_params.Breakdown],
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAnalyticBreakdownDataResponse:
        """
        This endpoint retrieves breakdown data of the given metrics by given breakdown field

        Args:
            date_range: The timeframe to get the data for.
            filters: Build *segments* of users using multiple filters on the data, `value` should be an *exact match*
            breakdowns: Breakdown fields and metrics to retrieve data for. Supports 1 to 3 breakdowns per request.
            workspace_id: The five to ten character unique identifier of the Gumlet workspace ID available on the Video Workspaces.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAnalyticBreakdownDataResponse: 200

        Example:
            ```python
            video_analytic = client.video_analytics.breakdown_data(
                date_range={"start_at": "2026-07-20", "end_at": "2026-08-20"},
                filters=[],
                breakdowns=[
                    {"name": "custom_video_id", "metric": "views", "page": 1, "page_size": 10},
                    {"name": "custom_video_title", "metric": "completion_percent_by_views", "page": 1, "page_size": 10},
                ],
                workspace_id="6694c405e63913eecf3cf5fb",
            )
            ```
        """
        return self._post(
            "/insights/breakdown-data",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "filters": filters,
                    "breakdowns": breakdowns,
                    "workspace_id": workspace_id,
                },
                video_analytic_breakdown_data_params.VideoAnalyticBreakdownDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAnalyticBreakdownDataResponse,
        )

    def aggregated_data(
        self,
        *,
        aggregate: Iterable[video_analytic_aggregated_data_params.Aggregate],
        workspace_id: str,
        timeframe: video_analytic_aggregated_data_params.Timeframe,
        filters: Iterable[video_analytic_aggregated_data_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAnalyticAggregatedDataResponse:
        """
        This endpoint retrieves aggregated data of the given metrics.

        Args:
            aggregate: Aggregate multiple metrics at the same time
            workspace_id: The unique identifier of the Gumlet workspace ID available on the Video Workspaces.
            timeframe: The timeframe to get the data for. Currently we only support maximum difference between `start_at` and `end_at` to be *60 days*
            filters: Get aggregations for metrics with multiple filters, `value` should be an exact match
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAnalyticAggregatedDataResponse: 200

        Example:
            ```python
            video_analytic = client.video_analytics.aggregated_data(
                aggregate=[{"metric": "views", "function": "sum"}],
                workspace_id="",
                timeframe={},
            )
            ```
        """
        return self._post(
            "/insights/aggregated-data",
            body=maybe_transform(
                {
                    "aggregate": aggregate,
                    "workspace_id": workspace_id,
                    "timeframe": timeframe,
                    "filters": filters,
                },
                video_analytic_aggregated_data_params.VideoAnalyticAggregatedDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAnalyticAggregatedDataResponse,
        )


class AsyncVideoAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoAnalyticsResourceWithRawResponse:
        return AsyncVideoAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoAnalyticsResourceWithStreamingResponse:
        return AsyncVideoAnalyticsResourceWithStreamingResponse(self)

    async def chart_data(
        self,
        *,
        metrics: SequenceNotStr[str],
        workspace_id: str,
        date_range: video_analytic_chart_data_params.DateRange,
        filters: Iterable[video_analytic_chart_data_params.Filter] | Omit = omit,
        group_by: Literal["daily", "weekly", "monthly"] | Omit = omit,
        chart_dimension: video_analytic_chart_data_params.ChartDimension | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAnalyticChartDataResponse:
        """
        This endpoint retrieves viewer analytics data. This endpoint is use for deep insights on the analytics data.

        Args:
            metrics: Get data for one or more `metrics` in the same request. Please add any of these metrics. `views`, `unique_views`, `impressions`. `completion_percent_by_views`, `playing_time`, `concurrent_users`, `widget_form_submitted`, `cta_clicks`
            workspace_id: The five to ten character unique identifier of the Gumlet workspace ID available on the Video Workspaces.
            date_range: The timeframe to get the data for.
            filters: Build *segments* of users using multiple filters on the data, `value` should be an *exact match*
            group_by: Data can be grouped by `daily`, `weekly` or `monthly`.
            chart_dimension: Metrics result Group by selected dimension, You can select upto 3 dimensions to get nested category result. result will follow selection orders.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAnalyticChartDataResponse: 200

        Example:
            ```python
            video_analytic = await client.video_analytics.chart_data(
                metrics=[""],
                workspace_id="",
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                group_by="daily",
            )
            ```
        """
        return await self._post(
            "/insights/viewer-analytics",
            body=await async_maybe_transform(
                {
                    "metrics": metrics,
                    "workspace_id": workspace_id,
                    "date_range": date_range,
                    "filters": filters,
                    "group_by": group_by,
                    "chart_dimension": chart_dimension,
                },
                video_analytic_chart_data_params.VideoAnalyticChartDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAnalyticChartDataResponse,
        )

    async def breakdown_data(
        self,
        *,
        date_range: video_analytic_breakdown_data_params.DateRange,
        filters: Iterable[video_analytic_breakdown_data_params.Filter] | Omit = omit,
        breakdowns: Iterable[video_analytic_breakdown_data_params.Breakdown],
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAnalyticBreakdownDataResponse:
        """
        This endpoint retrieves breakdown data of the given metrics by given breakdown field

        Args:
            date_range: The timeframe to get the data for.
            filters: Build *segments* of users using multiple filters on the data, `value` should be an *exact match*
            breakdowns: Breakdown fields and metrics to retrieve data for. Supports 1 to 3 breakdowns per request.
            workspace_id: The five to ten character unique identifier of the Gumlet workspace ID available on the Video Workspaces.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAnalyticBreakdownDataResponse: 200

        Example:
            ```python
            video_analytic = await client.video_analytics.breakdown_data(
                date_range={"start_at": "2026-07-20", "end_at": "2026-08-20"},
                filters=[],
                breakdowns=[
                    {"name": "custom_video_id", "metric": "views", "page": 1, "page_size": 10},
                    {"name": "custom_video_title", "metric": "completion_percent_by_views", "page": 1, "page_size": 10},
                ],
                workspace_id="6694c405e63913eecf3cf5fb",
            )
            ```
        """
        return await self._post(
            "/insights/breakdown-data",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "filters": filters,
                    "breakdowns": breakdowns,
                    "workspace_id": workspace_id,
                },
                video_analytic_breakdown_data_params.VideoAnalyticBreakdownDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAnalyticBreakdownDataResponse,
        )

    async def aggregated_data(
        self,
        *,
        aggregate: Iterable[video_analytic_aggregated_data_params.Aggregate],
        workspace_id: str,
        timeframe: video_analytic_aggregated_data_params.Timeframe,
        filters: Iterable[video_analytic_aggregated_data_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VideoAnalyticAggregatedDataResponse:
        """
        This endpoint retrieves aggregated data of the given metrics.

        Args:
            aggregate: Aggregate multiple metrics at the same time
            workspace_id: The unique identifier of the Gumlet workspace ID available on the Video Workspaces.
            timeframe: The timeframe to get the data for. Currently we only support maximum difference between `start_at` and `end_at` to be *60 days*
            filters: Get aggregations for metrics with multiple filters, `value` should be an exact match
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VideoAnalyticAggregatedDataResponse: 200

        Example:
            ```python
            video_analytic = await client.video_analytics.aggregated_data(
                aggregate=[{"metric": "views", "function": "sum"}],
                workspace_id="",
                timeframe={},
            )
            ```
        """
        return await self._post(
            "/insights/aggregated-data",
            body=await async_maybe_transform(
                {
                    "aggregate": aggregate,
                    "workspace_id": workspace_id,
                    "timeframe": timeframe,
                    "filters": filters,
                },
                video_analytic_aggregated_data_params.VideoAnalyticAggregatedDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoAnalyticAggregatedDataResponse,
        )


class VideoAnalyticsResourceWithRawResponse:
    def __init__(self, video_analytics: VideoAnalyticsResource) -> None:
        self._video_analytics = video_analytics

        self.chart_data = to_raw_response_wrapper(
            video_analytics.chart_data,
        )
        self.breakdown_data = to_raw_response_wrapper(
            video_analytics.breakdown_data,
        )
        self.aggregated_data = to_raw_response_wrapper(
            video_analytics.aggregated_data,
        )


class AsyncVideoAnalyticsResourceWithRawResponse:
    def __init__(self, video_analytics: AsyncVideoAnalyticsResource) -> None:
        self._video_analytics = video_analytics

        self.chart_data = async_to_raw_response_wrapper(
            video_analytics.chart_data,
        )
        self.breakdown_data = async_to_raw_response_wrapper(
            video_analytics.breakdown_data,
        )
        self.aggregated_data = async_to_raw_response_wrapper(
            video_analytics.aggregated_data,
        )


class VideoAnalyticsResourceWithStreamingResponse:
    def __init__(self, video_analytics: VideoAnalyticsResource) -> None:
        self._video_analytics = video_analytics

        self.chart_data = to_streamed_response_wrapper(
            video_analytics.chart_data,
        )
        self.breakdown_data = to_streamed_response_wrapper(
            video_analytics.breakdown_data,
        )
        self.aggregated_data = to_streamed_response_wrapper(
            video_analytics.aggregated_data,
        )


class AsyncVideoAnalyticsResourceWithStreamingResponse:
    def __init__(self, video_analytics: AsyncVideoAnalyticsResource) -> None:
        self._video_analytics = video_analytics

        self.chart_data = async_to_streamed_response_wrapper(
            video_analytics.chart_data,
        )
        self.breakdown_data = async_to_streamed_response_wrapper(
            video_analytics.breakdown_data,
        )
        self.aggregated_data = async_to_streamed_response_wrapper(
            video_analytics.aggregated_data,
        )
