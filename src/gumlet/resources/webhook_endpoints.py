# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
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
from ..types.webhook_endpoint_create_response import WebhookEndpointCreateResponse
from ..types import webhook_endpoint_create_params, webhook_endpoint_update_params
from ..types.webhook_endpoint_list_response import WebhookEndpointListResponse
from ..types.webhook_endpoint_update_response import WebhookEndpointUpdateResponse
from ..types.webhook_endpoint_delete_response import WebhookEndpointDeleteResponse
from ..types.webhook_endpoint_history_response import WebhookEndpointHistoryResponse

__all__ = ["WebhookEndpointsResource", "AsyncWebhookEndpointsResource"]


class WebhookEndpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookEndpointsResourceWithRawResponse:
        return WebhookEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookEndpointsResourceWithStreamingResponse:
        return WebhookEndpointsResourceWithStreamingResponse(self)

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
    ) -> WebhookEndpointCreateResponse:
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
            WebhookEndpointCreateResponse: 200

        Example:
            ```python
            webhook_endpoint = client.webhook_endpoints.create(
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
                webhook_endpoint_create_params.WebhookEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpointCreateResponse,
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
    ) -> WebhookEndpointListResponse:
        """
        List all webhooks.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookEndpointListResponse: Successful response

        Example:
            ```python
            webhook_endpoint = client.webhook_endpoints.list()
            ```
        """
        return self._get(
            "/org/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpointListResponse,
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
    ) -> WebhookEndpointUpdateResponse:
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
            WebhookEndpointUpdateResponse: 200

        Example:
            ```python
            webhook_endpoint = client.webhook_endpoints.update(
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
                webhook_endpoint_update_params.WebhookEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpointUpdateResponse,
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
    ) -> WebhookEndpointDeleteResponse:
        """
        Delete webhook listener endpoint.

        Args:
            webhook_id: Unique identifier for the Gumlet Webhook which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookEndpointDeleteResponse: 204

        Example:
            ```python
            webhook_endpoint = client.webhook_endpoints.delete(
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
            cast_to=WebhookEndpointDeleteResponse,
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
    ) -> WebhookEndpointHistoryResponse:
        """
        Get logs history for a given webhook.

        Args:
            webhook_id: Webhook ID. You can get it using list webhook endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookEndpointHistoryResponse: Successful response

        Example:
            ```python
            webhook_endpoint = client.webhook_endpoints.history(
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
            cast_to=WebhookEndpointHistoryResponse,
        )


class AsyncWebhookEndpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookEndpointsResourceWithRawResponse:
        return AsyncWebhookEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookEndpointsResourceWithStreamingResponse:
        return AsyncWebhookEndpointsResourceWithStreamingResponse(self)

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
    ) -> WebhookEndpointCreateResponse:
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
            WebhookEndpointCreateResponse: 200

        Example:
            ```python
            webhook_endpoint = await client.webhook_endpoints.create(
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
                webhook_endpoint_create_params.WebhookEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpointCreateResponse,
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
    ) -> WebhookEndpointListResponse:
        """
        List all webhooks.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookEndpointListResponse: Successful response

        Example:
            ```python
            webhook_endpoint = await client.webhook_endpoints.list()
            ```
        """
        return await self._get(
            "/org/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpointListResponse,
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
    ) -> WebhookEndpointUpdateResponse:
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
            WebhookEndpointUpdateResponse: 200

        Example:
            ```python
            webhook_endpoint = await client.webhook_endpoints.update(
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
                webhook_endpoint_update_params.WebhookEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpointUpdateResponse,
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
    ) -> WebhookEndpointDeleteResponse:
        """
        Delete webhook listener endpoint.

        Args:
            webhook_id: Unique identifier for the Gumlet Webhook which needs to be deleted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookEndpointDeleteResponse: 204

        Example:
            ```python
            webhook_endpoint = await client.webhook_endpoints.delete(
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
            cast_to=WebhookEndpointDeleteResponse,
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
    ) -> WebhookEndpointHistoryResponse:
        """
        Get logs history for a given webhook.

        Args:
            webhook_id: Webhook ID. You can get it using list webhook endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookEndpointHistoryResponse: Successful response

        Example:
            ```python
            webhook_endpoint = await client.webhook_endpoints.history(
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
            cast_to=WebhookEndpointHistoryResponse,
        )


class WebhookEndpointsResourceWithRawResponse:
    def __init__(self, webhook_endpoints: WebhookEndpointsResource) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = to_raw_response_wrapper(
            webhook_endpoints.create,
        )
        self.list = to_raw_response_wrapper(
            webhook_endpoints.list,
        )
        self.update = to_raw_response_wrapper(
            webhook_endpoints.update,
        )
        self.delete = to_raw_response_wrapper(
            webhook_endpoints.delete,
        )
        self.history = to_raw_response_wrapper(
            webhook_endpoints.history,
        )


class AsyncWebhookEndpointsResourceWithRawResponse:
    def __init__(self, webhook_endpoints: AsyncWebhookEndpointsResource) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = async_to_raw_response_wrapper(
            webhook_endpoints.create,
        )
        self.list = async_to_raw_response_wrapper(
            webhook_endpoints.list,
        )
        self.update = async_to_raw_response_wrapper(
            webhook_endpoints.update,
        )
        self.delete = async_to_raw_response_wrapper(
            webhook_endpoints.delete,
        )
        self.history = async_to_raw_response_wrapper(
            webhook_endpoints.history,
        )


class WebhookEndpointsResourceWithStreamingResponse:
    def __init__(self, webhook_endpoints: WebhookEndpointsResource) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = to_streamed_response_wrapper(
            webhook_endpoints.create,
        )
        self.list = to_streamed_response_wrapper(
            webhook_endpoints.list,
        )
        self.update = to_streamed_response_wrapper(
            webhook_endpoints.update,
        )
        self.delete = to_streamed_response_wrapper(
            webhook_endpoints.delete,
        )
        self.history = to_streamed_response_wrapper(
            webhook_endpoints.history,
        )


class AsyncWebhookEndpointsResourceWithStreamingResponse:
    def __init__(self, webhook_endpoints: AsyncWebhookEndpointsResource) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = async_to_streamed_response_wrapper(
            webhook_endpoints.create,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_endpoints.list,
        )
        self.update = async_to_streamed_response_wrapper(
            webhook_endpoints.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhook_endpoints.delete,
        )
        self.history = async_to_streamed_response_wrapper(
            webhook_endpoints.history,
        )
