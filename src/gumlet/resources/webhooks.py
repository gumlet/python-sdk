# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import json
import httpx

from typing import List
from typing_extensions import Literal
from .._types import SequenceNotStr
from typing import Mapping, cast

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._models import construct_type
from .._exceptions import GumletError
from ..types.parsed_webhook_event import ParsedWebhookEvent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_create_response import WebhookCreateResponse
from ..types import webhook_create_params, webhook_update_params
from ..types.webhook_list_response import WebhookListResponse
from ..types.webhook_update_response import WebhookUpdateResponse
from ..types.webhook_delete_response import WebhookDeleteResponse
from ..types.webhook_history_response import WebhookHistoryResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self)

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise GumletError("You need to install `gumlet[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def create(
        self,
        *,
        url: str,
        secret_token: str,
        triggers: List[
            Literal[
                "status",
                "live-video-status",
                "video.status.created",
                "video.status.downloaded",
                "video.status.optimized",
                "video.status.ready",
                "video.status.errored",
                "video.status.deleted",
                "video.status.repackaged",
                "video.status.stream_ready",
                "live.video.status.created",
                "live.video.status.ready",
                "live.video.status.preparing",
                "live.video.status.connected",
                "live.video.status.active",
                "live.video.status.complete",
                "live.video.status.disconnected",
                "event.embed.viewed",
                "event.embed.cta_clicked",
                "event.video.updated",
                "event.video.uploaded",
                "event.playlist.created",
                "event.playlist.asset",
                "event.playlist.deleted",
                "event.video.analytics",
                "event.image.analytics",
                "event.embed.form_submitted",
                "event.comment.all",
                "event.channel.member_joined",
            ]
        ],
        sources: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Creates a new webhook listener. Gumlet POSTs JSON to `url` for each matching event and sends `secret_token` in the `x-gumlet-token` header. Payload schemas are documented in the webhooks section.

        Args:
            url: URL from the application you want to send data to.
            secret_token: Secret sent back in the `x-gumlet-token` header of each webhook POST so you can confirm the request came from Gumlet.
            triggers: Events that invoke this webhook. `status` subscribes to every video asset status event. `live-video-status` subscribes to every live video status event. Any other value subscribes to that event only.
            sources: List of video collection identifiers for which webhooks are needed to be invoked.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookCreateResponse: 200

        Example:
            ```python
            webhook = client.webhooks.create(
                url="",
                secret_token="",
                triggers=["status"],
                sources=[""],
            )
            ```
        """
        return self._post(
            "/org/webhooks",
            body=maybe_transform(
                {
                    "url": url,
                    "secret_token": secret_token,
                    "triggers": triggers,
                    "sources": sources,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        List all webhooks.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookListResponse: Successful response

        Example:
            ```python
            webhook = client.webhooks.list()
            ```
        """
        return self._get(
            "/org/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    def update(
        self,
        webhook_id: str,
        *,
        url: str | Omit = omit,
        secret_token: str | Omit = omit,
        triggers: List[
            Literal[
                "status",
                "live-video-status",
                "video.status.created",
                "video.status.downloaded",
                "video.status.optimized",
                "video.status.ready",
                "video.status.errored",
                "video.status.deleted",
                "video.status.repackaged",
                "video.status.stream_ready",
                "live.video.status.created",
                "live.video.status.ready",
                "live.video.status.preparing",
                "live.video.status.connected",
                "live.video.status.active",
                "live.video.status.complete",
                "live.video.status.disconnected",
                "event.embed.viewed",
                "event.embed.cta_clicked",
                "event.video.updated",
                "event.video.uploaded",
                "event.playlist.created",
                "event.playlist.asset",
                "event.playlist.deleted",
                "event.video.analytics",
                "event.image.analytics",
                "event.embed.form_submitted",
                "event.comment.all",
                "event.channel.member_joined",
            ]
        ]
        | Omit = omit,
        sources: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Update a webhook listener.

        Args:
            webhook_id: Unique identifier for the Gumlet Webhook which needs to be updated.
            url: URL from the application you want to send data to.
            secret_token: Secret sent back in the `x-gumlet-token` header of each webhook POST so you can confirm the request came from Gumlet.
            triggers: Events that invoke this webhook. `status` subscribes to every video asset status event. `live-video-status` subscribes to every live video status event. Any other value subscribes to that event only.
            sources: List of video collection identifiers for which webhooks are needed to be invoked.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookUpdateResponse: 200

        Example:
            ```python
            webhook = client.webhooks.update(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._post(
            path_template("/org/webhooks/{webhook_id}", **{"webhook_id": webhook_id}),
            body=maybe_transform(
                {
                    "url": url,
                    "secret_token": secret_token,
                    "triggers": triggers,
                    "sources": sources,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    def delete(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """
        Delete webhook listener endpoint.

        Args:
            webhook_id: Unique identifier for the Gumlet Webhook which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookDeleteResponse: 204

        Example:
            ```python
            webhook = client.webhooks.delete(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._delete(
            path_template("/org/webhooks/{webhook_id}", **{"webhook_id": webhook_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def history(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookHistoryResponse:
        """
        Get logs history for a given webhook.

        Args:
            webhook_id: Webhook ID. You can get it using list webhook endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookHistoryResponse: Successful response

        Example:
            ```python
            webhook = client.webhooks.history(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            path_template("/org/webhook/{webhook_id}/history", **{"webhook_id": webhook_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookHistoryResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self)

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise GumletError("You need to install `gumlet[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    async def create(
        self,
        *,
        url: str,
        secret_token: str,
        triggers: List[
            Literal[
                "status",
                "live-video-status",
                "video.status.created",
                "video.status.downloaded",
                "video.status.optimized",
                "video.status.ready",
                "video.status.errored",
                "video.status.deleted",
                "video.status.repackaged",
                "video.status.stream_ready",
                "live.video.status.created",
                "live.video.status.ready",
                "live.video.status.preparing",
                "live.video.status.connected",
                "live.video.status.active",
                "live.video.status.complete",
                "live.video.status.disconnected",
                "event.embed.viewed",
                "event.embed.cta_clicked",
                "event.video.updated",
                "event.video.uploaded",
                "event.playlist.created",
                "event.playlist.asset",
                "event.playlist.deleted",
                "event.video.analytics",
                "event.image.analytics",
                "event.embed.form_submitted",
                "event.comment.all",
                "event.channel.member_joined",
            ]
        ],
        sources: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Creates a new webhook listener. Gumlet POSTs JSON to `url` for each matching event and sends `secret_token` in the `x-gumlet-token` header. Payload schemas are documented in the webhooks section.

        Args:
            url: URL from the application you want to send data to.
            secret_token: Secret sent back in the `x-gumlet-token` header of each webhook POST so you can confirm the request came from Gumlet.
            triggers: Events that invoke this webhook. `status` subscribes to every video asset status event. `live-video-status` subscribes to every live video status event. Any other value subscribes to that event only.
            sources: List of video collection identifiers for which webhooks are needed to be invoked.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookCreateResponse: 200

        Example:
            ```python
            webhook = await client.webhooks.create(
                url="",
                secret_token="",
                triggers=["status"],
                sources=[""],
            )
            ```
        """
        return await self._post(
            "/org/webhooks",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "secret_token": secret_token,
                    "triggers": triggers,
                    "sources": sources,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        List all webhooks.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookListResponse: Successful response

        Example:
            ```python
            webhook = await client.webhooks.list()
            ```
        """
        return await self._get(
            "/org/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    async def update(
        self,
        webhook_id: str,
        *,
        url: str | Omit = omit,
        secret_token: str | Omit = omit,
        triggers: List[
            Literal[
                "status",
                "live-video-status",
                "video.status.created",
                "video.status.downloaded",
                "video.status.optimized",
                "video.status.ready",
                "video.status.errored",
                "video.status.deleted",
                "video.status.repackaged",
                "video.status.stream_ready",
                "live.video.status.created",
                "live.video.status.ready",
                "live.video.status.preparing",
                "live.video.status.connected",
                "live.video.status.active",
                "live.video.status.complete",
                "live.video.status.disconnected",
                "event.embed.viewed",
                "event.embed.cta_clicked",
                "event.video.updated",
                "event.video.uploaded",
                "event.playlist.created",
                "event.playlist.asset",
                "event.playlist.deleted",
                "event.video.analytics",
                "event.image.analytics",
                "event.embed.form_submitted",
                "event.comment.all",
                "event.channel.member_joined",
            ]
        ]
        | Omit = omit,
        sources: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Update a webhook listener.

        Args:
            webhook_id: Unique identifier for the Gumlet Webhook which needs to be updated.
            url: URL from the application you want to send data to.
            secret_token: Secret sent back in the `x-gumlet-token` header of each webhook POST so you can confirm the request came from Gumlet.
            triggers: Events that invoke this webhook. `status` subscribes to every video asset status event. `live-video-status` subscribes to every live video status event. Any other value subscribes to that event only.
            sources: List of video collection identifiers for which webhooks are needed to be invoked.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookUpdateResponse: 200

        Example:
            ```python
            webhook = await client.webhooks.update(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._post(
            path_template("/org/webhooks/{webhook_id}", **{"webhook_id": webhook_id}),
            body=await async_maybe_transform(
                {
                    "url": url,
                    "secret_token": secret_token,
                    "triggers": triggers,
                    "sources": sources,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    async def delete(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """
        Delete webhook listener endpoint.

        Args:
            webhook_id: Unique identifier for the Gumlet Webhook which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookDeleteResponse: 204

        Example:
            ```python
            webhook = await client.webhooks.delete(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._delete(
            path_template("/org/webhooks/{webhook_id}", **{"webhook_id": webhook_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    async def history(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookHistoryResponse:
        """
        Get logs history for a given webhook.

        Args:
            webhook_id: Webhook ID. You can get it using list webhook endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookHistoryResponse: Successful response

        Example:
            ```python
            webhook = await client.webhooks.history(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            path_template("/org/webhook/{webhook_id}/history", **{"webhook_id": webhook_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookHistoryResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.history = to_raw_response_wrapper(
            webhooks.history,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.history = async_to_raw_response_wrapper(
            webhooks.history,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.history = to_streamed_response_wrapper(
            webhooks.history,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.history = async_to_streamed_response_wrapper(
            webhooks.history,
        )
