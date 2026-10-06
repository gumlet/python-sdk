# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .video_asset_status_webhook_event import VideoAssetStatusWebhookEvent
from .live_video_status_webhook_event import LiveVideoStatusWebhookEvent
from .product_event_webhook_event import ProductEventWebhookEvent

__all__ = ["ParsedWebhookEvent"]


ParsedWebhookEvent: TypeAlias = Union[
    VideoAssetStatusWebhookEvent,
    LiveVideoStatusWebhookEvent,
    ProductEventWebhookEvent,
]
