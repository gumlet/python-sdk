# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
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
from ..types.audit_log_fetch_response import AuditLogFetchResponse
from ..types import audit_log_fetch_params

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self)

    def fetch(
        self,
        *,
        date_range: audit_log_fetch_params.DateRange,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        user_email: SequenceNotStr[str] | Omit = omit,
        activity_type: List[
            Literal[
                "workspace_created",
                "video_uploaded",
                "video_details_updated",
                "video_deleted",
                "thumbnail_updated",
                "subtitles_updated",
                "audio_updated",
                "processing_settings_updated",
                "player_settings_updated",
                "workspace_updated",
                "team_member_invited",
                "team_member_removed",
                "import_started",
                "playlist_created",
                "playlist_updated",
                "playlist_asset_changed",
                "security_settings_updated",
                "channel_updated",
                "video_alert_changed",
                "video_report_changed",
                "live_stream_created",
                "live_stream_started",
                "live_stream_thumbnail_updated",
                "live_stream_completed",
                "live_stream_collection_created",
                "live_stream_collection_updated",
                "live_stream_deleted",
                "image_source_created",
                "image_source_updated",
                "image_report_changed",
                "image_alert_changed",
                "user_profile_updated",
                "api_key_changed",
                "webhook_created",
                "webhook_updated",
                "webhook_deleted",
                "drm_credentials_changed",
                "plan_changed",
                "billing_details_updated",
                "playlist_deleted",
                "payment_method_added",
                "billing_alert_changed",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditLogFetchResponse:
        """
        Get audit logs for the user activity in your organisation. Please note that this endpoint can only be accessed by `owner` and `admin` role users.

        Args:
            date_range: Body parameter.
            page_number: Page number of results.
            page_size: Body parameter.
            user_email: Array of user emails to filter the activity logs.
            activity_type: Array of activity types to filter the audit logs
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AuditLogFetchResponse: Successful response

        Example:
            ```python
            audit_log = client.audit_logs.fetch(
                date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
                page_number=1,
                page_size=100,
            )
            ```
        """
        return self._post(
            "/user/audit-log",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "page_number": page_number,
                    "page_size": page_size,
                    "user_email": user_email,
                    "activity_type": activity_type,
                },
                audit_log_fetch_params.AuditLogFetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditLogFetchResponse,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    async def fetch(
        self,
        *,
        date_range: audit_log_fetch_params.DateRange,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        user_email: SequenceNotStr[str] | Omit = omit,
        activity_type: List[
            Literal[
                "workspace_created",
                "video_uploaded",
                "video_details_updated",
                "video_deleted",
                "thumbnail_updated",
                "subtitles_updated",
                "audio_updated",
                "processing_settings_updated",
                "player_settings_updated",
                "workspace_updated",
                "team_member_invited",
                "team_member_removed",
                "import_started",
                "playlist_created",
                "playlist_updated",
                "playlist_asset_changed",
                "security_settings_updated",
                "channel_updated",
                "video_alert_changed",
                "video_report_changed",
                "live_stream_created",
                "live_stream_started",
                "live_stream_thumbnail_updated",
                "live_stream_completed",
                "live_stream_collection_created",
                "live_stream_collection_updated",
                "live_stream_deleted",
                "image_source_created",
                "image_source_updated",
                "image_report_changed",
                "image_alert_changed",
                "user_profile_updated",
                "api_key_changed",
                "webhook_created",
                "webhook_updated",
                "webhook_deleted",
                "drm_credentials_changed",
                "plan_changed",
                "billing_details_updated",
                "playlist_deleted",
                "payment_method_added",
                "billing_alert_changed",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditLogFetchResponse:
        """
        Get audit logs for the user activity in your organisation. Please note that this endpoint can only be accessed by `owner` and `admin` role users.

        Args:
            date_range: Body parameter.
            page_number: Page number of results.
            page_size: Body parameter.
            user_email: Array of user emails to filter the activity logs.
            activity_type: Array of activity types to filter the audit logs
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AuditLogFetchResponse: Successful response

        Example:
            ```python
            audit_log = await client.audit_logs.fetch(
                date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
                page_number=1,
                page_size=100,
            )
            ```
        """
        return await self._post(
            "/user/audit-log",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "page_number": page_number,
                    "page_size": page_size,
                    "user_email": user_email,
                    "activity_type": activity_type,
                },
                audit_log_fetch_params.AuditLogFetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditLogFetchResponse,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.fetch = to_raw_response_wrapper(
            audit_logs.fetch,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.fetch = async_to_raw_response_wrapper(
            audit_logs.fetch,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.fetch = to_streamed_response_wrapper(
            audit_logs.fetch,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.fetch = async_to_streamed_response_wrapper(
            audit_logs.fetch,
        )
