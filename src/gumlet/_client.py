# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, GumletError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import (
        video_assets,
        subtitle_upload,
        audio_upload,
        video_usage_analytics,
        multipart_upload,
        video_profiles,
        video_playlists,
        webhooks,
        image_sources,
        image_usage_analytics,
        live_stream_assets,
        recycle_bin,
        video_workspaces,
        folders,
        channel_viewers,
        video_analytics,
        organization_data,
        user_data,
        audit_logs,
        billing,
        live_stream_workspaces,
    )
    from .resources.video_assets import VideoAssetsResource, AsyncVideoAssetsResource
    from .resources.subtitle_upload import SubtitleUploadResource, AsyncSubtitleUploadResource
    from .resources.audio_upload import AudioUploadResource, AsyncAudioUploadResource
    from .resources.video_usage_analytics import VideoUsageAnalyticsResource, AsyncVideoUsageAnalyticsResource
    from .resources.multipart_upload import MultipartUploadResource, AsyncMultipartUploadResource
    from .resources.video_profiles import VideoProfilesResource, AsyncVideoProfilesResource
    from .resources.video_playlists import VideoPlaylistsResource, AsyncVideoPlaylistsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.image_sources import ImageSourcesResource, AsyncImageSourcesResource
    from .resources.image_usage_analytics import ImageUsageAnalyticsResource, AsyncImageUsageAnalyticsResource
    from .resources.live_stream_assets import LiveStreamAssetsResource, AsyncLiveStreamAssetsResource
    from .resources.recycle_bin import RecycleBinResource, AsyncRecycleBinResource
    from .resources.video_workspaces import VideoWorkspacesResource, AsyncVideoWorkspacesResource
    from .resources.folders import FoldersResource, AsyncFoldersResource
    from .resources.channel_viewers import ChannelViewersResource, AsyncChannelViewersResource
    from .resources.video_analytics import VideoAnalyticsResource, AsyncVideoAnalyticsResource
    from .resources.organization_data import OrganizationDataResource, AsyncOrganizationDataResource
    from .resources.user_data import UserDataResource, AsyncUserDataResource
    from .resources.audit_logs import AuditLogsResource, AsyncAuditLogsResource
    from .resources.billing import BillingResource, AsyncBillingResource
    from .resources.live_stream_workspaces import LiveStreamWorkspacesResource, AsyncLiveStreamWorkspacesResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = ["Gumlet", "AsyncGumlet", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class Gumlet(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Gumlet client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise GumletError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key
        if base_url is None:
            base_url = os.environ.get("GUMLET_BASE_URL")
        if base_url is None:
            base_url = "https://api.gumlet.com/v1"
        custom_headers_env = os.environ.get("GUMLET_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def video_assets(self) -> "VideoAssetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_assets import VideoAssetsResource
        return VideoAssetsResource(self)

    @cached_property
    def subtitle_upload(self) -> "SubtitleUploadResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.subtitle_upload import SubtitleUploadResource
        return SubtitleUploadResource(self)

    @cached_property
    def audio_upload(self) -> "AudioUploadResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audio_upload import AudioUploadResource
        return AudioUploadResource(self)

    @cached_property
    def video_usage_analytics(self) -> "VideoUsageAnalyticsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_usage_analytics import VideoUsageAnalyticsResource
        return VideoUsageAnalyticsResource(self)

    @cached_property
    def multipart_upload(self) -> "MultipartUploadResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.multipart_upload import MultipartUploadResource
        return MultipartUploadResource(self)

    @cached_property
    def video_profiles(self) -> "VideoProfilesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_profiles import VideoProfilesResource
        return VideoProfilesResource(self)

    @cached_property
    def video_playlists(self) -> "VideoPlaylistsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_playlists import VideoPlaylistsResource
        return VideoPlaylistsResource(self)

    @cached_property
    def webhooks(self) -> "WebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResource
        return WebhooksResource(self)

    @cached_property
    def image_sources(self) -> "ImageSourcesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_sources import ImageSourcesResource
        return ImageSourcesResource(self)

    @cached_property
    def image_usage_analytics(self) -> "ImageUsageAnalyticsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_usage_analytics import ImageUsageAnalyticsResource
        return ImageUsageAnalyticsResource(self)

    @cached_property
    def live_stream_assets(self) -> "LiveStreamAssetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_assets import LiveStreamAssetsResource
        return LiveStreamAssetsResource(self)

    @cached_property
    def recycle_bin(self) -> "RecycleBinResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.recycle_bin import RecycleBinResource
        return RecycleBinResource(self)

    @cached_property
    def video_workspaces(self) -> "VideoWorkspacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_workspaces import VideoWorkspacesResource
        return VideoWorkspacesResource(self)

    @cached_property
    def folders(self) -> "FoldersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.folders import FoldersResource
        return FoldersResource(self)

    @cached_property
    def channel_viewers(self) -> "ChannelViewersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.channel_viewers import ChannelViewersResource
        return ChannelViewersResource(self)

    @cached_property
    def video_analytics(self) -> "VideoAnalyticsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_analytics import VideoAnalyticsResource
        return VideoAnalyticsResource(self)

    @cached_property
    def organization_data(self) -> "OrganizationDataResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization_data import OrganizationDataResource
        return OrganizationDataResource(self)

    @cached_property
    def user_data(self) -> "UserDataResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.user_data import UserDataResource
        return UserDataResource(self)

    @cached_property
    def audit_logs(self) -> "AuditLogsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audit_logs import AuditLogsResource
        return AuditLogsResource(self)

    @cached_property
    def billing(self) -> "BillingResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import BillingResource
        return BillingResource(self)

    @cached_property
    def live_stream_workspaces(self) -> "LiveStreamWorkspacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_workspaces import LiveStreamWorkspacesResource
        return LiveStreamWorkspacesResource(self)

    @cached_property
    def with_raw_response(self) -> GumletWithRawResponse:
        return GumletWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GumletWithStreamedResponse:
        return GumletWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGumlet(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGumlet client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise GumletError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key
        if base_url is None:
            base_url = os.environ.get("GUMLET_BASE_URL")
        if base_url is None:
            base_url = "https://api.gumlet.com/v1"
        custom_headers_env = os.environ.get("GUMLET_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def video_assets(self) -> "AsyncVideoAssetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_assets import AsyncVideoAssetsResource
        return AsyncVideoAssetsResource(self)

    @cached_property
    def subtitle_upload(self) -> "AsyncSubtitleUploadResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.subtitle_upload import AsyncSubtitleUploadResource
        return AsyncSubtitleUploadResource(self)

    @cached_property
    def audio_upload(self) -> "AsyncAudioUploadResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audio_upload import AsyncAudioUploadResource
        return AsyncAudioUploadResource(self)

    @cached_property
    def video_usage_analytics(self) -> "AsyncVideoUsageAnalyticsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_usage_analytics import AsyncVideoUsageAnalyticsResource
        return AsyncVideoUsageAnalyticsResource(self)

    @cached_property
    def multipart_upload(self) -> "AsyncMultipartUploadResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.multipart_upload import AsyncMultipartUploadResource
        return AsyncMultipartUploadResource(self)

    @cached_property
    def video_profiles(self) -> "AsyncVideoProfilesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_profiles import AsyncVideoProfilesResource
        return AsyncVideoProfilesResource(self)

    @cached_property
    def video_playlists(self) -> "AsyncVideoPlaylistsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_playlists import AsyncVideoPlaylistsResource
        return AsyncVideoPlaylistsResource(self)

    @cached_property
    def webhooks(self) -> "AsyncWebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResource
        return AsyncWebhooksResource(self)

    @cached_property
    def image_sources(self) -> "AsyncImageSourcesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_sources import AsyncImageSourcesResource
        return AsyncImageSourcesResource(self)

    @cached_property
    def image_usage_analytics(self) -> "AsyncImageUsageAnalyticsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_usage_analytics import AsyncImageUsageAnalyticsResource
        return AsyncImageUsageAnalyticsResource(self)

    @cached_property
    def live_stream_assets(self) -> "AsyncLiveStreamAssetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_assets import AsyncLiveStreamAssetsResource
        return AsyncLiveStreamAssetsResource(self)

    @cached_property
    def recycle_bin(self) -> "AsyncRecycleBinResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.recycle_bin import AsyncRecycleBinResource
        return AsyncRecycleBinResource(self)

    @cached_property
    def video_workspaces(self) -> "AsyncVideoWorkspacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_workspaces import AsyncVideoWorkspacesResource
        return AsyncVideoWorkspacesResource(self)

    @cached_property
    def folders(self) -> "AsyncFoldersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.folders import AsyncFoldersResource
        return AsyncFoldersResource(self)

    @cached_property
    def channel_viewers(self) -> "AsyncChannelViewersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.channel_viewers import AsyncChannelViewersResource
        return AsyncChannelViewersResource(self)

    @cached_property
    def video_analytics(self) -> "AsyncVideoAnalyticsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_analytics import AsyncVideoAnalyticsResource
        return AsyncVideoAnalyticsResource(self)

    @cached_property
    def organization_data(self) -> "AsyncOrganizationDataResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization_data import AsyncOrganizationDataResource
        return AsyncOrganizationDataResource(self)

    @cached_property
    def user_data(self) -> "AsyncUserDataResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.user_data import AsyncUserDataResource
        return AsyncUserDataResource(self)

    @cached_property
    def audit_logs(self) -> "AsyncAuditLogsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audit_logs import AsyncAuditLogsResource
        return AsyncAuditLogsResource(self)

    @cached_property
    def billing(self) -> "AsyncBillingResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import AsyncBillingResource
        return AsyncBillingResource(self)

    @cached_property
    def live_stream_workspaces(self) -> "AsyncLiveStreamWorkspacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_workspaces import AsyncLiveStreamWorkspacesResource
        return AsyncLiveStreamWorkspacesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGumletWithRawResponse:
        return AsyncGumletWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGumletWithStreamedResponse:
        return AsyncGumletWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GumletWithRawResponse:
    _client: Gumlet

    def __init__(self, client: Gumlet) -> None:
        self._client = client

    @cached_property
    def video_assets(self) -> video_assets.VideoAssetsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_assets import VideoAssetsResourceWithRawResponse
        return VideoAssetsResourceWithRawResponse(self._client.video_assets)

    @cached_property
    def subtitle_upload(self) -> subtitle_upload.SubtitleUploadResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.subtitle_upload import SubtitleUploadResourceWithRawResponse
        return SubtitleUploadResourceWithRawResponse(self._client.subtitle_upload)

    @cached_property
    def audio_upload(self) -> audio_upload.AudioUploadResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audio_upload import AudioUploadResourceWithRawResponse
        return AudioUploadResourceWithRawResponse(self._client.audio_upload)

    @cached_property
    def video_usage_analytics(self) -> video_usage_analytics.VideoUsageAnalyticsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_usage_analytics import VideoUsageAnalyticsResourceWithRawResponse
        return VideoUsageAnalyticsResourceWithRawResponse(self._client.video_usage_analytics)

    @cached_property
    def multipart_upload(self) -> multipart_upload.MultipartUploadResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.multipart_upload import MultipartUploadResourceWithRawResponse
        return MultipartUploadResourceWithRawResponse(self._client.multipart_upload)

    @cached_property
    def video_profiles(self) -> video_profiles.VideoProfilesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_profiles import VideoProfilesResourceWithRawResponse
        return VideoProfilesResourceWithRawResponse(self._client.video_profiles)

    @cached_property
    def video_playlists(self) -> video_playlists.VideoPlaylistsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_playlists import VideoPlaylistsResourceWithRawResponse
        return VideoPlaylistsResourceWithRawResponse(self._client.video_playlists)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResourceWithRawResponse
        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def image_sources(self) -> image_sources.ImageSourcesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_sources import ImageSourcesResourceWithRawResponse
        return ImageSourcesResourceWithRawResponse(self._client.image_sources)

    @cached_property
    def image_usage_analytics(self) -> image_usage_analytics.ImageUsageAnalyticsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_usage_analytics import ImageUsageAnalyticsResourceWithRawResponse
        return ImageUsageAnalyticsResourceWithRawResponse(self._client.image_usage_analytics)

    @cached_property
    def live_stream_assets(self) -> live_stream_assets.LiveStreamAssetsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_assets import LiveStreamAssetsResourceWithRawResponse
        return LiveStreamAssetsResourceWithRawResponse(self._client.live_stream_assets)

    @cached_property
    def recycle_bin(self) -> recycle_bin.RecycleBinResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.recycle_bin import RecycleBinResourceWithRawResponse
        return RecycleBinResourceWithRawResponse(self._client.recycle_bin)

    @cached_property
    def video_workspaces(self) -> video_workspaces.VideoWorkspacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_workspaces import VideoWorkspacesResourceWithRawResponse
        return VideoWorkspacesResourceWithRawResponse(self._client.video_workspaces)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.folders import FoldersResourceWithRawResponse
        return FoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def channel_viewers(self) -> channel_viewers.ChannelViewersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.channel_viewers import ChannelViewersResourceWithRawResponse
        return ChannelViewersResourceWithRawResponse(self._client.channel_viewers)

    @cached_property
    def video_analytics(self) -> video_analytics.VideoAnalyticsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_analytics import VideoAnalyticsResourceWithRawResponse
        return VideoAnalyticsResourceWithRawResponse(self._client.video_analytics)

    @cached_property
    def organization_data(self) -> organization_data.OrganizationDataResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization_data import OrganizationDataResourceWithRawResponse
        return OrganizationDataResourceWithRawResponse(self._client.organization_data)

    @cached_property
    def user_data(self) -> user_data.UserDataResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.user_data import UserDataResourceWithRawResponse
        return UserDataResourceWithRawResponse(self._client.user_data)

    @cached_property
    def audit_logs(self) -> audit_logs.AuditLogsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audit_logs import AuditLogsResourceWithRawResponse
        return AuditLogsResourceWithRawResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.BillingResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import BillingResourceWithRawResponse
        return BillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def live_stream_workspaces(self) -> live_stream_workspaces.LiveStreamWorkspacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_workspaces import LiveStreamWorkspacesResourceWithRawResponse
        return LiveStreamWorkspacesResourceWithRawResponse(self._client.live_stream_workspaces)


class AsyncGumletWithRawResponse:
    _client: AsyncGumlet

    def __init__(self, client: AsyncGumlet) -> None:
        self._client = client

    @cached_property
    def video_assets(self) -> video_assets.AsyncVideoAssetsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_assets import AsyncVideoAssetsResourceWithRawResponse
        return AsyncVideoAssetsResourceWithRawResponse(self._client.video_assets)

    @cached_property
    def subtitle_upload(self) -> subtitle_upload.AsyncSubtitleUploadResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.subtitle_upload import AsyncSubtitleUploadResourceWithRawResponse
        return AsyncSubtitleUploadResourceWithRawResponse(self._client.subtitle_upload)

    @cached_property
    def audio_upload(self) -> audio_upload.AsyncAudioUploadResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audio_upload import AsyncAudioUploadResourceWithRawResponse
        return AsyncAudioUploadResourceWithRawResponse(self._client.audio_upload)

    @cached_property
    def video_usage_analytics(self) -> video_usage_analytics.AsyncVideoUsageAnalyticsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_usage_analytics import AsyncVideoUsageAnalyticsResourceWithRawResponse
        return AsyncVideoUsageAnalyticsResourceWithRawResponse(self._client.video_usage_analytics)

    @cached_property
    def multipart_upload(self) -> multipart_upload.AsyncMultipartUploadResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.multipart_upload import AsyncMultipartUploadResourceWithRawResponse
        return AsyncMultipartUploadResourceWithRawResponse(self._client.multipart_upload)

    @cached_property
    def video_profiles(self) -> video_profiles.AsyncVideoProfilesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_profiles import AsyncVideoProfilesResourceWithRawResponse
        return AsyncVideoProfilesResourceWithRawResponse(self._client.video_profiles)

    @cached_property
    def video_playlists(self) -> video_playlists.AsyncVideoPlaylistsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_playlists import AsyncVideoPlaylistsResourceWithRawResponse
        return AsyncVideoPlaylistsResourceWithRawResponse(self._client.video_playlists)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResourceWithRawResponse
        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def image_sources(self) -> image_sources.AsyncImageSourcesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_sources import AsyncImageSourcesResourceWithRawResponse
        return AsyncImageSourcesResourceWithRawResponse(self._client.image_sources)

    @cached_property
    def image_usage_analytics(self) -> image_usage_analytics.AsyncImageUsageAnalyticsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_usage_analytics import AsyncImageUsageAnalyticsResourceWithRawResponse
        return AsyncImageUsageAnalyticsResourceWithRawResponse(self._client.image_usage_analytics)

    @cached_property
    def live_stream_assets(self) -> live_stream_assets.AsyncLiveStreamAssetsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_assets import AsyncLiveStreamAssetsResourceWithRawResponse
        return AsyncLiveStreamAssetsResourceWithRawResponse(self._client.live_stream_assets)

    @cached_property
    def recycle_bin(self) -> recycle_bin.AsyncRecycleBinResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.recycle_bin import AsyncRecycleBinResourceWithRawResponse
        return AsyncRecycleBinResourceWithRawResponse(self._client.recycle_bin)

    @cached_property
    def video_workspaces(self) -> video_workspaces.AsyncVideoWorkspacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_workspaces import AsyncVideoWorkspacesResourceWithRawResponse
        return AsyncVideoWorkspacesResourceWithRawResponse(self._client.video_workspaces)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.folders import AsyncFoldersResourceWithRawResponse
        return AsyncFoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def channel_viewers(self) -> channel_viewers.AsyncChannelViewersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.channel_viewers import AsyncChannelViewersResourceWithRawResponse
        return AsyncChannelViewersResourceWithRawResponse(self._client.channel_viewers)

    @cached_property
    def video_analytics(self) -> video_analytics.AsyncVideoAnalyticsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_analytics import AsyncVideoAnalyticsResourceWithRawResponse
        return AsyncVideoAnalyticsResourceWithRawResponse(self._client.video_analytics)

    @cached_property
    def organization_data(self) -> organization_data.AsyncOrganizationDataResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization_data import AsyncOrganizationDataResourceWithRawResponse
        return AsyncOrganizationDataResourceWithRawResponse(self._client.organization_data)

    @cached_property
    def user_data(self) -> user_data.AsyncUserDataResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.user_data import AsyncUserDataResourceWithRawResponse
        return AsyncUserDataResourceWithRawResponse(self._client.user_data)

    @cached_property
    def audit_logs(self) -> audit_logs.AsyncAuditLogsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audit_logs import AsyncAuditLogsResourceWithRawResponse
        return AsyncAuditLogsResourceWithRawResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import AsyncBillingResourceWithRawResponse
        return AsyncBillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def live_stream_workspaces(self) -> live_stream_workspaces.AsyncLiveStreamWorkspacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_workspaces import AsyncLiveStreamWorkspacesResourceWithRawResponse
        return AsyncLiveStreamWorkspacesResourceWithRawResponse(self._client.live_stream_workspaces)


class GumletWithStreamedResponse:
    _client: Gumlet

    def __init__(self, client: Gumlet) -> None:
        self._client = client

    @cached_property
    def video_assets(self) -> video_assets.VideoAssetsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_assets import VideoAssetsResourceWithStreamingResponse
        return VideoAssetsResourceWithStreamingResponse(self._client.video_assets)

    @cached_property
    def subtitle_upload(self) -> subtitle_upload.SubtitleUploadResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.subtitle_upload import SubtitleUploadResourceWithStreamingResponse
        return SubtitleUploadResourceWithStreamingResponse(self._client.subtitle_upload)

    @cached_property
    def audio_upload(self) -> audio_upload.AudioUploadResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audio_upload import AudioUploadResourceWithStreamingResponse
        return AudioUploadResourceWithStreamingResponse(self._client.audio_upload)

    @cached_property
    def video_usage_analytics(self) -> video_usage_analytics.VideoUsageAnalyticsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_usage_analytics import VideoUsageAnalyticsResourceWithStreamingResponse
        return VideoUsageAnalyticsResourceWithStreamingResponse(self._client.video_usage_analytics)

    @cached_property
    def multipart_upload(self) -> multipart_upload.MultipartUploadResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.multipart_upload import MultipartUploadResourceWithStreamingResponse
        return MultipartUploadResourceWithStreamingResponse(self._client.multipart_upload)

    @cached_property
    def video_profiles(self) -> video_profiles.VideoProfilesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_profiles import VideoProfilesResourceWithStreamingResponse
        return VideoProfilesResourceWithStreamingResponse(self._client.video_profiles)

    @cached_property
    def video_playlists(self) -> video_playlists.VideoPlaylistsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_playlists import VideoPlaylistsResourceWithStreamingResponse
        return VideoPlaylistsResourceWithStreamingResponse(self._client.video_playlists)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResourceWithStreamingResponse
        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def image_sources(self) -> image_sources.ImageSourcesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_sources import ImageSourcesResourceWithStreamingResponse
        return ImageSourcesResourceWithStreamingResponse(self._client.image_sources)

    @cached_property
    def image_usage_analytics(self) -> image_usage_analytics.ImageUsageAnalyticsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_usage_analytics import ImageUsageAnalyticsResourceWithStreamingResponse
        return ImageUsageAnalyticsResourceWithStreamingResponse(self._client.image_usage_analytics)

    @cached_property
    def live_stream_assets(self) -> live_stream_assets.LiveStreamAssetsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_assets import LiveStreamAssetsResourceWithStreamingResponse
        return LiveStreamAssetsResourceWithStreamingResponse(self._client.live_stream_assets)

    @cached_property
    def recycle_bin(self) -> recycle_bin.RecycleBinResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.recycle_bin import RecycleBinResourceWithStreamingResponse
        return RecycleBinResourceWithStreamingResponse(self._client.recycle_bin)

    @cached_property
    def video_workspaces(self) -> video_workspaces.VideoWorkspacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_workspaces import VideoWorkspacesResourceWithStreamingResponse
        return VideoWorkspacesResourceWithStreamingResponse(self._client.video_workspaces)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.folders import FoldersResourceWithStreamingResponse
        return FoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def channel_viewers(self) -> channel_viewers.ChannelViewersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.channel_viewers import ChannelViewersResourceWithStreamingResponse
        return ChannelViewersResourceWithStreamingResponse(self._client.channel_viewers)

    @cached_property
    def video_analytics(self) -> video_analytics.VideoAnalyticsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_analytics import VideoAnalyticsResourceWithStreamingResponse
        return VideoAnalyticsResourceWithStreamingResponse(self._client.video_analytics)

    @cached_property
    def organization_data(self) -> organization_data.OrganizationDataResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization_data import OrganizationDataResourceWithStreamingResponse
        return OrganizationDataResourceWithStreamingResponse(self._client.organization_data)

    @cached_property
    def user_data(self) -> user_data.UserDataResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.user_data import UserDataResourceWithStreamingResponse
        return UserDataResourceWithStreamingResponse(self._client.user_data)

    @cached_property
    def audit_logs(self) -> audit_logs.AuditLogsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audit_logs import AuditLogsResourceWithStreamingResponse
        return AuditLogsResourceWithStreamingResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.BillingResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import BillingResourceWithStreamingResponse
        return BillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def live_stream_workspaces(self) -> live_stream_workspaces.LiveStreamWorkspacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_workspaces import LiveStreamWorkspacesResourceWithStreamingResponse
        return LiveStreamWorkspacesResourceWithStreamingResponse(self._client.live_stream_workspaces)


class AsyncGumletWithStreamedResponse:
    _client: AsyncGumlet

    def __init__(self, client: AsyncGumlet) -> None:
        self._client = client

    @cached_property
    def video_assets(self) -> video_assets.AsyncVideoAssetsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_assets import AsyncVideoAssetsResourceWithStreamingResponse
        return AsyncVideoAssetsResourceWithStreamingResponse(self._client.video_assets)

    @cached_property
    def subtitle_upload(self) -> subtitle_upload.AsyncSubtitleUploadResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.subtitle_upload import AsyncSubtitleUploadResourceWithStreamingResponse
        return AsyncSubtitleUploadResourceWithStreamingResponse(self._client.subtitle_upload)

    @cached_property
    def audio_upload(self) -> audio_upload.AsyncAudioUploadResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audio_upload import AsyncAudioUploadResourceWithStreamingResponse
        return AsyncAudioUploadResourceWithStreamingResponse(self._client.audio_upload)

    @cached_property
    def video_usage_analytics(self) -> video_usage_analytics.AsyncVideoUsageAnalyticsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_usage_analytics import AsyncVideoUsageAnalyticsResourceWithStreamingResponse
        return AsyncVideoUsageAnalyticsResourceWithStreamingResponse(self._client.video_usage_analytics)

    @cached_property
    def multipart_upload(self) -> multipart_upload.AsyncMultipartUploadResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.multipart_upload import AsyncMultipartUploadResourceWithStreamingResponse
        return AsyncMultipartUploadResourceWithStreamingResponse(self._client.multipart_upload)

    @cached_property
    def video_profiles(self) -> video_profiles.AsyncVideoProfilesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_profiles import AsyncVideoProfilesResourceWithStreamingResponse
        return AsyncVideoProfilesResourceWithStreamingResponse(self._client.video_profiles)

    @cached_property
    def video_playlists(self) -> video_playlists.AsyncVideoPlaylistsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_playlists import AsyncVideoPlaylistsResourceWithStreamingResponse
        return AsyncVideoPlaylistsResourceWithStreamingResponse(self._client.video_playlists)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse
        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def image_sources(self) -> image_sources.AsyncImageSourcesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_sources import AsyncImageSourcesResourceWithStreamingResponse
        return AsyncImageSourcesResourceWithStreamingResponse(self._client.image_sources)

    @cached_property
    def image_usage_analytics(self) -> image_usage_analytics.AsyncImageUsageAnalyticsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.image_usage_analytics import AsyncImageUsageAnalyticsResourceWithStreamingResponse
        return AsyncImageUsageAnalyticsResourceWithStreamingResponse(self._client.image_usage_analytics)

    @cached_property
    def live_stream_assets(self) -> live_stream_assets.AsyncLiveStreamAssetsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_assets import AsyncLiveStreamAssetsResourceWithStreamingResponse
        return AsyncLiveStreamAssetsResourceWithStreamingResponse(self._client.live_stream_assets)

    @cached_property
    def recycle_bin(self) -> recycle_bin.AsyncRecycleBinResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.recycle_bin import AsyncRecycleBinResourceWithStreamingResponse
        return AsyncRecycleBinResourceWithStreamingResponse(self._client.recycle_bin)

    @cached_property
    def video_workspaces(self) -> video_workspaces.AsyncVideoWorkspacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_workspaces import AsyncVideoWorkspacesResourceWithStreamingResponse
        return AsyncVideoWorkspacesResourceWithStreamingResponse(self._client.video_workspaces)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.folders import AsyncFoldersResourceWithStreamingResponse
        return AsyncFoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def channel_viewers(self) -> channel_viewers.AsyncChannelViewersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.channel_viewers import AsyncChannelViewersResourceWithStreamingResponse
        return AsyncChannelViewersResourceWithStreamingResponse(self._client.channel_viewers)

    @cached_property
    def video_analytics(self) -> video_analytics.AsyncVideoAnalyticsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.video_analytics import AsyncVideoAnalyticsResourceWithStreamingResponse
        return AsyncVideoAnalyticsResourceWithStreamingResponse(self._client.video_analytics)

    @cached_property
    def organization_data(self) -> organization_data.AsyncOrganizationDataResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organization_data import AsyncOrganizationDataResourceWithStreamingResponse
        return AsyncOrganizationDataResourceWithStreamingResponse(self._client.organization_data)

    @cached_property
    def user_data(self) -> user_data.AsyncUserDataResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.user_data import AsyncUserDataResourceWithStreamingResponse
        return AsyncUserDataResourceWithStreamingResponse(self._client.user_data)

    @cached_property
    def audit_logs(self) -> audit_logs.AsyncAuditLogsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.audit_logs import AsyncAuditLogsResourceWithStreamingResponse
        return AsyncAuditLogsResourceWithStreamingResponse(self._client.audit_logs)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.billing import AsyncBillingResourceWithStreamingResponse
        return AsyncBillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def live_stream_workspaces(self) -> live_stream_workspaces.AsyncLiveStreamWorkspacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.live_stream_workspaces import AsyncLiveStreamWorkspacesResourceWithStreamingResponse
        return AsyncLiveStreamWorkspacesResourceWithStreamingResponse(self._client.live_stream_workspaces)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Gumlet
AsyncClient = AsyncGumlet
