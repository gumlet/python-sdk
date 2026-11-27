# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import json
import httpx

from typing import Mapping, cast

from .._types import Body, Query, Headers, NotGiven, not_given, HeadersLike
from .._utils import path_template, get_required_header
from .._compat import cached_property
from .._models import construct_type
from .._webhook_verify import verify_webhook_signature
from .._exceptions import EmptyWebhookSecretError
from ..types.parsed_webhook_event import ParsedWebhookEvent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_retrieve_response import WebhookRetrieveResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self)

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise EmptyWebhookSecretError("Cannot verify a webhook with a key that decodes to an empty key")

        if not isinstance(headers, dict):
            headers = dict(headers)

        verify_webhook_signature(payload, headers, key)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def verify_signature(self, payload: str | bytes, headers: HeadersLike, *, key: str | bytes | None = None) -> None:
        """Verifies that `payload` was signed with the webhook key, raising when it was not.

        `key` defaults to the client's `webhook_secret`. A missing signature header raises too.
        """
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise EmptyWebhookSecretError("Cannot verify a webhook with a key that decodes to an empty key")

        signed_headers = {
            "webhook-id": get_required_header(headers, "webhook-id"),
            "webhook-timestamp": get_required_header(headers, "webhook-timestamp"),
            "webhook-signature": get_required_header(headers, "webhook-signature"),
        }
        verify_webhook_signature(payload, signed_headers, key)

    def parse_unsafe(self, payload: str) -> ParsedWebhookEvent:
        """Parses `payload` into a typed event without verifying its signature.

        Only use this for a payload whose signature was already verified, or in tests.
        """
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        """
        Retrieve details of a single webhook by ID.

        Args:
            webhook_id: Webhook ID. You can get it using the list webhooks endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookRetrieveResponse: Successful response

        Example:
            ```python
            webhook = client.webhooks.retrieve(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            path_template("/org/webhooks/{webhook_id}", **{"webhook_id": webhook_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self)

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise EmptyWebhookSecretError("Cannot verify a webhook with a key that decodes to an empty key")

        if not isinstance(headers, dict):
            headers = dict(headers)

        verify_webhook_signature(payload, headers, key)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def verify_signature(self, payload: str | bytes, headers: HeadersLike, *, key: str | bytes | None = None) -> None:
        """Verifies that `payload` was signed with the webhook key, raising when it was not.

        `key` defaults to the client's `webhook_secret`. A missing signature header raises too.
        """
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise EmptyWebhookSecretError("Cannot verify a webhook with a key that decodes to an empty key")

        signed_headers = {
            "webhook-id": get_required_header(headers, "webhook-id"),
            "webhook-timestamp": get_required_header(headers, "webhook-timestamp"),
            "webhook-signature": get_required_header(headers, "webhook-signature"),
        }
        verify_webhook_signature(payload, signed_headers, key)

    def parse_unsafe(self, payload: str) -> ParsedWebhookEvent:
        """Parses `payload` into a typed event without verifying its signature.

        Only use this for a payload whose signature was already verified, or in tests.
        """
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    async def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        """
        Retrieve details of a single webhook by ID.

        Args:
            webhook_id: Webhook ID. You can get it using the list webhooks endpoint.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            WebhookRetrieveResponse: Successful response

        Example:
            ```python
            webhook = await client.webhooks.retrieve(
                webhook_id="webhookId",
            )
            ```
        """
        if webhook_id is None or (isinstance(webhook_id, str) and not webhook_id):
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            path_template("/org/webhooks/{webhook_id}", **{"webhook_id": webhook_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
