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
from ..types.image_usage_analytic_retrieve_response import ImageUsageAnalyticRetrieveResponse
from ..types import image_usage_analytic_retrieve_params

__all__ = ["ImageUsageAnalyticsResource", "AsyncImageUsageAnalyticsResource"]


class ImageUsageAnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageUsageAnalyticsResourceWithRawResponse:
        return ImageUsageAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageUsageAnalyticsResourceWithStreamingResponse:
        return ImageUsageAnalyticsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        metrics: List[
            Literal[
                "bandwidth_consumption",
                "requests_count",
                "transformations_count",
                "bandwidth_savings",
                "origin_hit_rate",
                "avg_transformation_response_time",
                "status_4xx",
                "status_5xx",
                "cdn_hit_rate",
                "content_type",
                "status_2xx",
                "avg_response_time",
                "top_assets",
                "bandwidth_consumption_by_source",
                "ai_credit_usage",
            ]
        ],
        date_range: image_usage_analytic_retrieve_params.DateRange,
        group_by: Literal["daily", "weekly", "monthly", "hourly"] | Omit = omit,
        filters: image_usage_analytic_retrieve_params.Filters | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageUsageAnalyticRetrieveResponse:
        """
        This endpoint helps you get image analytics data like bandwidth consumption, request count, CDN hit ratio, etc.

        Args:
            metrics: Define the metric you need the data for, currently we support "bandwidth_consumption", "requests_count","status_4xx","status_5xx","avg_response_time""
            date_range: The timeframe to get the data for. Currently we only support a maximum of 30 days between `start_at` and `end_at`.
            group_by: Body parameter.
            filters: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageUsageAnalyticRetrieveResponse: 200

        Example:
            ```python
            image_usage_analytic = client.image_usage_analytics.retrieve(
                metrics=["bandwidth_consumption"],
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                group_by="daily",
            )
            ```
        """
        return self._post(
            "/image/analytics",
            body=maybe_transform(
                {
                    "metrics": metrics,
                    "date_range": date_range,
                    "group_by": group_by,
                    "filters": filters,
                },
                image_usage_analytic_retrieve_params.ImageUsageAnalyticRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUsageAnalyticRetrieveResponse,
        )


class AsyncImageUsageAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageUsageAnalyticsResourceWithRawResponse:
        return AsyncImageUsageAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageUsageAnalyticsResourceWithStreamingResponse:
        return AsyncImageUsageAnalyticsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        metrics: List[
            Literal[
                "bandwidth_consumption",
                "requests_count",
                "transformations_count",
                "bandwidth_savings",
                "origin_hit_rate",
                "avg_transformation_response_time",
                "status_4xx",
                "status_5xx",
                "cdn_hit_rate",
                "content_type",
                "status_2xx",
                "avg_response_time",
                "top_assets",
                "bandwidth_consumption_by_source",
                "ai_credit_usage",
            ]
        ],
        date_range: image_usage_analytic_retrieve_params.DateRange,
        group_by: Literal["daily", "weekly", "monthly", "hourly"] | Omit = omit,
        filters: image_usage_analytic_retrieve_params.Filters | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageUsageAnalyticRetrieveResponse:
        """
        This endpoint helps you get image analytics data like bandwidth consumption, request count, CDN hit ratio, etc.

        Args:
            metrics: Define the metric you need the data for, currently we support "bandwidth_consumption", "requests_count","status_4xx","status_5xx","avg_response_time""
            date_range: The timeframe to get the data for. Currently we only support a maximum of 30 days between `start_at` and `end_at`.
            group_by: Body parameter.
            filters: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageUsageAnalyticRetrieveResponse: 200

        Example:
            ```python
            image_usage_analytic = await client.image_usage_analytics.retrieve(
                metrics=["bandwidth_consumption"],
                date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
                group_by="daily",
            )
            ```
        """
        return await self._post(
            "/image/analytics",
            body=await async_maybe_transform(
                {
                    "metrics": metrics,
                    "date_range": date_range,
                    "group_by": group_by,
                    "filters": filters,
                },
                image_usage_analytic_retrieve_params.ImageUsageAnalyticRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUsageAnalyticRetrieveResponse,
        )


class ImageUsageAnalyticsResourceWithRawResponse:
    def __init__(self, image_usage_analytics: ImageUsageAnalyticsResource) -> None:
        self._image_usage_analytics = image_usage_analytics

        self.retrieve = to_raw_response_wrapper(
            image_usage_analytics.retrieve,
        )


class AsyncImageUsageAnalyticsResourceWithRawResponse:
    def __init__(self, image_usage_analytics: AsyncImageUsageAnalyticsResource) -> None:
        self._image_usage_analytics = image_usage_analytics

        self.retrieve = async_to_raw_response_wrapper(
            image_usage_analytics.retrieve,
        )


class ImageUsageAnalyticsResourceWithStreamingResponse:
    def __init__(self, image_usage_analytics: ImageUsageAnalyticsResource) -> None:
        self._image_usage_analytics = image_usage_analytics

        self.retrieve = to_streamed_response_wrapper(
            image_usage_analytics.retrieve,
        )


class AsyncImageUsageAnalyticsResourceWithStreamingResponse:
    def __init__(self, image_usage_analytics: AsyncImageUsageAnalyticsResource) -> None:
        self._image_usage_analytics = image_usage_analytics

        self.retrieve = async_to_streamed_response_wrapper(
            image_usage_analytics.retrieve,
        )
