# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["AuditLogFetchParams", "DateRange"]


class AuditLogFetchParams(TypedDict, total=False):
    date_range: Required[DateRange]

    page_number: int
    """Page number of results."""

    page_size: int

    user_email: SequenceNotStr[str]
    """Array of user emails to filter the activity logs."""

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
    """Array of activity types to filter the audit logs"""


class DateRange(TypedDict, total=False):
    start_at: Required[str]
    """Starting date for audit logs. It's a string in YYYY-MM-DD format."""

    end_at: Required[str]
    """Ending date for audit logs. It's a string in YYYY-MM-DD format."""
