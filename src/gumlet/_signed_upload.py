"""Uploads to pre-signed URLs for the SDK's signed-upload methods.

A signed-upload method calls an operation that answers with a pre-signed URL, sends a file to that
URL, then optionally confirms. The upload is deliberately *not* sent through the SDK client: the
client's requests carry its credentials (auth headers, query auth, cookies) and default headers, and
its `httpx` client may be one the caller configured with `auth=`, headers, cookies, params or event
hooks of its own. None of that may reach the upload host, which is usually a different host with the
authorization already signed into the URL. So each upload uses a fresh, short-lived `httpx` client
and sends exactly the file, `Content-Type`, and the headers the initiating response itself names.
Only the SDK client's timeout and retry budget are reused, and the transport of an `http_client`
the caller passed.

That transport is borrowed so the caller's proxy and TLS settings (`proxy=`, `mounts=`, `verify=`,
`cert=`, or the same given to an `httpx.HTTPTransport`) reach the upload: a corporate proxy or a
private CA would otherwise make every upload fail. Only the one transport the caller's client would
route the upload URL to is borrowed, and by default only when it is exactly httpx's own
`HTTPTransport` (or `AsyncHTTPTransport`), which sends a request as given. Any other transport
class sends the request itself and can add headers, credentials or cookies the SDK cannot see, so
with one the upload falls back to a fresh client of httpx's defaults, where proxy and CA settings
come from the environment (`HTTPS_PROXY`, `SSL_CERT_FILE`, ...) only.

A caller whose proxy or TLS setup lives only in a transport class of its own opts that transport in
by inheriting `SignedUploadTransport`. That is the caller's declaration, never a guess: the SDK
reads it off the routed transport itself, so a wrapper is lent only if it inherits the marker too.

The upload is never handed to the caller's client itself (`http_client.send`): that would run its
event hooks, whose request hooks can add headers (an `Authorization` meant for the API among them) and
whose response hooks can raise for a status the upload retries, and it would file the upload host's
cookies in the client's jar. On the fresh client none of that exists, so only the routing, proxy, TLS
and connection pool of the borrowed transport reach the upload host, and the request carries
nothing but what `_request_kwargs` names.

A client the SDK built itself, because the caller passed none, carries no such settings, so its
uploads keep a fresh client of httpx's defaults, which reads the environment at upload time and leaves
the client's connection pool alone. A borrowed transport is never closed here: the caller's client
owns it.
"""

from __future__ import annotations

import os
import json
import time
import email.utils
import random
import pathlib
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Type,
    Tuple,
    Union,
    Mapping,
    TypeVar,
    Iterator,
    Optional,
    Sequence,
    NamedTuple,
    AsyncIterator,
)
from typing_extensions import Literal, TypedDict

import anyio
import httpx

from ._types import NotGiven, FileTypes
from ._models import BaseModel
from ._constants import MAX_RETRY_DELAY, INITIAL_RETRY_DELAY
from ._exceptions import APITimeoutError, APIConnectionError, GumletError
from ._base_client import SyncHttpxClientWrapper, AsyncHttpxClientWrapper

if TYPE_CHECKING:
    from ._base_client import SyncAPIClient, AsyncAPIClient

__all__ = [
    "SignedUploadTransport",
    "SignedUploadFile",
    "SignedUploadSpec",
    "read_signed_upload_file",
    "async_read_signed_upload_file",
    "read_signed_upload_field",
    "signed_upload_path_param",
    "upload_to_signed_url",
    "async_upload_to_signed_url",
]

_DEFAULT_CONTENT_TYPE = "application/octet-stream"

# How much of the body goes out per write. httpx's write timeout covers one write, so this is the
# progress that restarts it: small enough that a slow link still gets a chunk out within the timeout.
_UPLOAD_CHUNK_BYTES = 16 * 1024


class SignedUploadSpec(TypedDict, total=False):
    """How a generated signed-upload method sends its file; fixed when the SDK is generated."""

    url_field: Sequence[str]
    """Wire-name path to the upload URL in the initiating response."""

    method: Literal["PUT", "POST"]

    body: Literal["binary", "multipart"]
    """`binary` sends the raw bytes; `multipart` sends `multipart/form-data` with the file as one part."""

    multipart_field: str
    """Form field the file is sent under, for a `multipart` upload."""

    content_type: str
    """Configured `Content-Type` of a `binary` upload."""

    headers_field: Sequence[str]
    """Wire-name path to a string map of headers the upload must carry, in the initiating response."""


class SignedUploadTransport:
    """A marker a transport of your own inherits so the SDK's signed uploads go through it.

    By default a signed upload borrows only httpx's own `HTTPTransport` (or `AsyncHTTPTransport`)
    from a custom `http_client`, and any other transport class falls back to a fresh client of
    httpx's defaults, since a class of its own may add headers, credentials or cookies as it sends.
    Inheriting this marker declares that the transport sends a request as handed over: it adds no
    credentials, cookies or headers of its own, keeps no session or cookie jar that would, is bound
    to no Unix socket, follows no redirects, and honours the timeout httpx hands it with each request
    (`request.extensions["timeout"]`). The upload then goes through it, for a caller whose
    proxy or TLS setup lives only in that transport:

        class CorporateTransport(SignedUploadTransport, httpx.HTTPTransport): ...

    The SDK reads the marker off the transport the client routes the upload URL to, not off the client
    or anything it wraps, so a wrapper is lent only if it inherits the marker itself. The upload still
    carries only the file, its content type and the headers the API named, on a client with no auth,
    cookies or event hooks, and the `https:` rule, the retries and the redirect refusal still apply.
    The upload's timeout reaches the transport only as that request extension: by design the SDK runs
    no watchdog of its own around a marked transport, so honouring it is part of the declaration. The
    marker is checked, never what it promises: a marked transport that
    adds a credential sends it to the upload host, and one that ignores the timeout can hang the call.
    """


def read_signed_upload_field(value: object, path: Sequence[str]) -> object:
    """Reads a value out of a decoded response body by wire-name path, or `None` when a step is missing.

    A response the SDK already decoded into a model is read through its wire-name dump, because the
    path is spelled in wire names and a model's attributes may be spelled differently. One decoded as
    text, because the API labelled its JSON with another media type or with none, is parsed first.
    """
    current = _decoded_body(value)
    for segment in path:
        if not isinstance(current, Mapping):
            return None
        mapping: Mapping[Any, object] = current
        if segment not in mapping:
            return None
        current = mapping[segment]
    return current


def _decoded_body(value: object) -> object:
    """The initiating response as a plain value: a model's wire-name dump, or a raw body parsed as JSON.

    With a confirm step the initiating request hands back the raw `httpx.Response`, because the SDK
    decodes a body to text (or, under strict response validation, refuses it) when its `Content-Type`
    does not end in `json` — `text/plain`, `application/x-amz-json-1.1`, or none at all — which an API
    that issues upload URLs does not always get right. A body that is not JSON is returned as is and
    reads as a missing field.
    """
    if isinstance(value, BaseModel):
        return value.to_dict(use_api_names=True, exclude_unset=False)
    if isinstance(value, httpx.Response):
        value = value.content
    if isinstance(value, (str, bytes, bytearray)):
        try:
            decoded: object = json.loads(value)
        except ValueError:
            return value
        return decoded
    return value


class SignedUploadFile(NamedTuple):
    """The file a signed upload sends, read into memory once, before the initiating request."""

    filename: Optional[str]
    content: bytes
    content_type: Optional[str]
    headers: Mapping[str, str]
    """The headers a `(name, content, type, headers)` file tuple carries; empty for any other form."""


def read_signed_upload_file(file: FileTypes) -> SignedUploadFile:
    """Reads the file a signed upload sends, before the initiating request is made.

    A file that cannot be read (a missing path, a text-mode handle, an unsupported type) then fails
    the call before the API has created an upload that would never receive its file.
    """
    filename, content, content_type = _read_file(file)
    return SignedUploadFile(filename, content, content_type, _file_headers(file))


async def async_read_signed_upload_file(file: FileTypes) -> SignedUploadFile:
    """The async twin of `read_signed_upload_file`, reading paths without blocking the event loop."""
    filename, content, content_type = await _async_read_file(file)
    return SignedUploadFile(filename, content, content_type, _file_headers(file))


def signed_upload_path_param(value: object, path: Sequence[str]) -> str:
    """Reads a confirm-step path parameter off the initiating response.

    Raises rather than filling the path with `None`: a confirm request sent to `/files/None` would at
    best 404 and at worst act on a resource nobody named. A `.` or `..` segment is refused too: it would
    send the confirm to another endpoint. `path_template` refuses one only once the confirm is built,
    after the file is sent, so the call reads this before the upload.
    """
    found = read_signed_upload_field(value, path)
    if isinstance(found, str) and found:
        segment = next((part for part in found.split("/") if part in (".", "..")), None)
        if segment is not None:
            raise GumletError(
                f'The upload response\'s `{".".join(path)}` contains a "{segment}" segment, so the upload cannot be confirmed.'
            )
        return found
    if isinstance(found, int) and not isinstance(found, bool):
        return str(found)
    raise GumletError(
        f"Expected the upload response to carry a non-empty `{'.'.join(path)}` to confirm the upload with."
    )


def upload_to_signed_url(
    client: SyncAPIClient,
    initiated: object,
    spec: SignedUploadSpec,
    file: SignedUploadFile,
    *,
    timeout: Union[float, httpx.Timeout, None, NotGiven],
) -> httpx.Response:
    """Sends `file` to the pre-signed URL in `initiated` and returns the upload host's success response.

    Retries connection errors (whatever a lent transport raises for one, as the base client does),
    timeouts, 408, 409, 429 and 5xx (or whatever `x-should-retry` says),
    waiting as `Retry-After`/`retry-after-ms` asks up to a minute and otherwise backing off
    exponentially, within the client's `max_retries`; safe because the file was read once (see
    `read_signed_upload_file`) and every attempt sends the same bytes. A redirect is not followed: it
    would re-send the file and the named headers to a host the API's response did not name.

    `timeout` (the client's when not given) bounds each phase rather than the whole upload: connecting,
    each chunk of the file going out, and each read of the answer. A slow upload that keeps moving is
    not cut off; a host that stops reading, or never answers, is. `None` means no timeout.
    """
    url = _upload_url(initiated, spec)
    headers, body = _encode_request(spec, url, _request_kwargs(initiated, spec, file))
    effective_timeout = client.timeout if isinstance(timeout, NotGiven) else timeout
    max_retries = client.max_retries
    with _upload_client(client._client, url, effective_timeout) as http:
        attempt = 0
        while True:
            remaining = max_retries - attempt
            request = http.build_request(spec.get("method", "PUT"), url, headers=headers, content=_ChunkedBody(body))
            try:
                response = http.send(request, auth=_upload_auth(request))
            except httpx.TimeoutException as err:
                if remaining > 0:
                    time.sleep(_retry_delay(attempt))
                    attempt += 1
                    continue
                raise APITimeoutError(request=request) from err
            # Any other failure of the send, as the base client treats one: a lent transport of the
            # caller's need not raise httpx's own errors for a dropped connection.
            except Exception as err:
                if remaining > 0:
                    time.sleep(_retry_delay(attempt))
                    attempt += 1
                    continue
                raise APIConnectionError(request=request) from err
            if response.is_success:
                return response
            if response.is_redirect:
                response.close()
                raise _redirect_error(response)
            if remaining > 0 and _should_retry(response):
                response.close()
                time.sleep(_retry_after(response.headers) or _retry_delay(attempt))
                attempt += 1
                continue
            response.read()
            raise client._make_status_error_from_response(response)


async def async_upload_to_signed_url(
    client: AsyncAPIClient,
    initiated: object,
    spec: SignedUploadSpec,
    file: SignedUploadFile,
    *,
    timeout: Union[float, httpx.Timeout, None, NotGiven],
) -> httpx.Response:
    """The async twin of `upload_to_signed_url`."""
    url = _upload_url(initiated, spec)
    headers, body = _encode_request(spec, url, _request_kwargs(initiated, spec, file))
    effective_timeout = client.timeout if isinstance(timeout, NotGiven) else timeout
    max_retries = client.max_retries
    async with _async_upload_client(client._client, url, effective_timeout) as http:
        attempt = 0
        while True:
            remaining = max_retries - attempt
            request = http.build_request(
                spec.get("method", "PUT"), url, headers=headers, content=_AsyncChunkedBody(body)
            )
            try:
                response = await http.send(request, auth=_upload_auth(request))
            except httpx.TimeoutException as err:
                if remaining > 0:
                    await anyio.sleep(_retry_delay(attempt))
                    attempt += 1
                    continue
                raise APITimeoutError(request=request) from err
            # Any other failure of the send, as the base client treats one: a lent transport of the
            # caller's need not raise httpx's own errors for a dropped connection.
            except Exception as err:
                if remaining > 0:
                    await anyio.sleep(_retry_delay(attempt))
                    attempt += 1
                    continue
                raise APIConnectionError(request=request) from err
            if response.is_success:
                return response
            if response.is_redirect:
                await response.aclose()
                raise _redirect_error(response)
            if remaining > 0 and _should_retry(response):
                await response.aclose()
                await anyio.sleep(_retry_after(response.headers) or _retry_delay(attempt))
                attempt += 1
                continue
            await response.aread()
            raise client._make_status_error_from_response(response)


def _upload_client(source: httpx.Client, url: str, timeout: Union[float, httpx.Timeout, None]) -> httpx.Client:
    """A fresh client for one upload, on the caller's transport for `url` when that may be lent.

    The fresh client brings no auth, headers, cookies, params or event hooks, so none of the caller's
    client's own reaches the upload; `follow_redirects=False` keeps a redirect from re-sending the file
    to a host the API's response did not name. Given a transport, httpx skips its environment proxies:
    the borrowed transport already is the caller's routing for this URL, environment proxies included
    when the caller's client trusted them.
    """
    transport = _caller_transport(source, url, httpx.HTTPTransport, httpx.BaseTransport)
    if transport is None:
        return httpx.Client(timeout=timeout, follow_redirects=False)
    return httpx.Client(timeout=timeout, follow_redirects=False, transport=_BorrowedTransport(transport))


def _async_upload_client(
    source: httpx.AsyncClient, url: str, timeout: Union[float, httpx.Timeout, None]
) -> httpx.AsyncClient:
    """The async twin of `_upload_client`."""
    transport = _caller_transport(source, url, httpx.AsyncHTTPTransport, httpx.AsyncBaseTransport)
    if transport is None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=False)
    return httpx.AsyncClient(timeout=timeout, follow_redirects=False, transport=_AsyncBorrowedTransport(transport))


_T = TypeVar("_T")
_B = TypeVar("_B")


def _caller_transport(source: object, url: str, httpx_type: Type[_T], base_type: Type[_B]) -> Optional[Union[_T, _B]]:
    """The transport the caller's client would send `url` through, when it may be lent to the upload.

    That is the client's mount for the URL (a `proxy=`, a `mounts=` entry, or an environment proxy
    the client picked up), else its default transport. It is lent when it is exactly `httpx_type`
    (an exact type check, not `isinstance`: a subclass can override `handle_request` to add headers,
    as any other transport class can, and those would reach the upload host) and bound to no Unix
    socket, or when it inherits `SignedUploadTransport` and is a `base_type`, the flavour the fresh
    upload client takes. A marked transport is lent as the caller declared, with nothing else checked:
    detecting what a transport does from its class would miss whatever a wrapper delegates to. httpx
    keeps the routing private (`_transport_for_url`, in every release the SDK supports), so a client
    without it gets `None` and the upload a fresh transport.

    So does the client the SDK built because the caller passed no `http_client` (the
    `HttpxClientWrapper` classes, which only the SDK creates). It holds no proxy or TLS setting of the
    caller's to honour, and borrowing it would only fix the environment's proxy and CA settings at
    client creation, take a slot in its pool, and send uploads on connections whose kernel buffers
    an earlier upload grew.
    """
    if type(source) is SyncHttpxClientWrapper or type(source) is AsyncHttpxClientWrapper:
        return None
    pick = getattr(source, "_transport_for_url", None)
    if not callable(pick):
        return None
    # `_upload_url` already parsed and checked `url`, so this cannot raise for it.
    transport: object = pick(httpx.URL(url))
    if isinstance(transport, SignedUploadTransport):
        return transport if isinstance(transport, base_type) else None
    # `isinstance` narrows the type; the exact check is the one that refuses a subclass.
    if not isinstance(transport, httpx_type) or type(transport) is not httpx_type:
        return None
    # Fails closed: a transport is borrowed only when its pool is there and says it is bound to no
    # Unix socket. An httpcore release that renamed `_pool` or `_uds` would otherwise read as "not
    # bound" and send the file to whatever socket the caller's transport was built for.
    pool = getattr(transport, "_pool", None)
    if pool is None or not hasattr(pool, "_uds") or getattr(pool, "_uds") is not None:
        return None
    return transport


class _BorrowedTransport(httpx.BaseTransport):
    """The caller's `httpx.HTTPTransport` or marked transport, lent to one upload client and left open when it closes."""

    def __init__(self, transport: httpx.BaseTransport) -> None:
        """Wraps `transport`, which stays the caller's to close."""
        self._transport = transport

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        """Sends `request` through the caller's transport: its proxy, TLS settings and connection pool."""
        return self._transport.handle_request(request)

    def close(self) -> None:
        """Leaves the transport open: the caller's client owns its connection pool and closes it."""


class _AsyncBorrowedTransport(httpx.AsyncBaseTransport):
    """The async twin of `_BorrowedTransport`, lending an `httpx.AsyncHTTPTransport` or a marked async transport."""

    def __init__(self, transport: httpx.AsyncBaseTransport) -> None:
        """Wraps `transport`, which stays the caller's to close."""
        self._transport = transport

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        """Sends `request` through the caller's transport: its proxy, TLS settings and connection pool."""
        return await self._transport.handle_async_request(request)

    async def aclose(self) -> None:
        """Leaves the transport open: the caller's client owns its connection pool and closes it."""


def _upload_url(initiated: object, spec: SignedUploadSpec) -> str:
    """Reads and validates the upload URL, refusing a missing value or one that is not https.

    The URL came from a response rather than from the caller, so a `file:` or `data:` URL is refused
    before any request is made, and so is plain `http:` to anything but a loopback host: it would send
    the file, the signature in the query and the named headers in cleartext, for anyone on the path
    to replay until the URL expires.
    """
    path = spec.get("url_field", ())
    value = read_signed_upload_field(initiated, path)
    if not isinstance(value, str) or not value:
        raise GumletError(f"Expected the upload response to carry an upload URL in `{'.'.join(path)}`.")
    try:
        parsed = httpx.URL(value)
    except Exception as err:
        raise GumletError(f"The upload URL in `{'.'.join(path)}` is not a valid URL.") from err
    if parsed.scheme not in ("http", "https") or not parsed.host:
        raise GumletError(f"Refusing to upload to `{'.'.join(path)}`: expected an absolute https: URL.")
    if parsed.scheme == "http" and not _is_loopback(parsed.host):
        raise GumletError(f"Refusing to upload to `{'.'.join(path)}` over plain http:; expected an https: URL.")
    return value


def _is_loopback(host: str) -> bool:
    """Whether `host` is this machine: exactly `localhost`, `127.0.0.1` or `::1`.

    The loopback hosts the CLI's OAuth runtime accepts plain `http:` for. A `*.localhost` name is not
    one: not every resolver sends it to loopback.
    """
    return host.lower().strip("[]") in ("localhost", "127.0.0.1", "::1")


def _upload_auth(request: httpx.Request) -> httpx.Auth:
    """The only auth an upload carries: Basic credentials the pre-signed URL itself names, else none.

    Passed on every send so httpx never chooses one: httpx < 0.24 (the dependency floor admits
    0.23) signs a request to any host listed in `~/.netrc` with that entry's password by default, so
    a fresh client would hand the caller's machine credentials to whatever host the API's response
    named. `trust_env` stays on so environment proxies still apply on a fallback client (see
    `_upload_client`); a borrowed transport already carries the caller's own proxy routing.
    """
    username, password = request.url.username, request.url.password
    if username or password:
        return httpx.BasicAuth(username=username, password=password)
    return httpx.Auth()


def _redirect_error(response: httpx.Response) -> GumletError:
    """The error a redirect from the upload host raises: it is not followed, since following it would
    re-send the file and the named headers to a host the API's response did not name."""
    return GumletError(f"The upload host answered with a redirect ({response.status_code}), which is not followed.")


def _request_kwargs(initiated: object, spec: SignedUploadSpec, file: SignedUploadFile) -> Dict[str, Any]:
    """The headers and body of the upload request: nothing from the SDK client, by construction.

    The headers are the ones the initiating response names, plus — for a `(name, content, type,
    headers)` file tuple — the caller's own: on the part itself in a multipart upload, on the request
    in a binary one, where a header the response names wins because the URL may be signed for it.
    """
    filename, content, file_content_type, file_headers = file
    headers: Dict[str, str] = {}
    headers_field = spec.get("headers_field")
    if headers_field is not None:
        named = read_signed_upload_field(initiated, headers_field)
        if isinstance(named, Mapping):
            named_headers: Mapping[Any, object] = named
            for name, value in named_headers.items():
                if isinstance(name, str) and isinstance(value, str):
                    headers[name] = value

    if spec.get("body", "binary") == "multipart":
        # httpx writes the multipart `Content-Type` with its boundary; a named one would break it.
        headers = {name: value for name, value in headers.items() if name.lower() != "content-type"}
        _check_headers(headers)
        _check_headers(file_headers)
        field = spec.get("multipart_field", "file")
        part: Tuple[Any, ...] = (filename or "file", content, file_content_type or _DEFAULT_CONTENT_TYPE)
        if file_headers:
            part = (*part, dict(file_headers))
        return {"headers": headers, "files": {field: part}}

    named_names = {name.lower() for name in headers}
    for name, value in file_headers.items():
        if name.lower() not in named_names:
            headers[name] = value
    # A header the initiating response names wins: a pre-signed URL can sign the type it was issued for.
    if not any(name.lower() == "content-type" for name in headers):
        headers["Content-Type"] = spec.get("content_type") or file_content_type or _DEFAULT_CONTENT_TYPE
    _check_headers(headers)
    return {"headers": headers, "content": content}


def _encode_request(spec: SignedUploadSpec, url: str, request_kwargs: Dict[str, Any]) -> Tuple[httpx.Headers, bytes]:
    """Encodes the upload once, into the headers and the exact bytes every attempt sends.

    The body is then sent in chunks (see `_ChunkedBody`), and httpx would send an iterated body with
    chunked transfer encoding, which object stores refuse. So `Content-Length` is set here, along
    with the multipart `Content-Type` and its boundary, which httpx only writes when it encodes.
    """
    encoded = httpx.Request(spec.get("method", "PUT"), url, **request_kwargs)
    body = encoded.read()
    headers = httpx.Headers(request_kwargs["headers"])
    content_type = encoded.headers.get("Content-Type")
    if content_type is not None:
        headers.setdefault("Content-Type", content_type)
    headers.setdefault("Content-Length", str(len(body)))
    return headers, body


class _ChunkedBody:
    """The body, sent a chunk at a time, so the write timeout counts time without progress.

    httpx applies its write timeout to each write, and a body given whole is one write on some
    backends: a large file on a slow link would then time out while still going out. An iterable
    rather than a generator: httpx refuses to read a generator body twice (`StreamConsumed`), and a
    transport the caller lends, such as one that retries a request itself, may send the same request
    again, which would then fail on every attempt and never upload.
    """

    def __init__(self, body: bytes) -> None:
        """Holds the encoded body every pass sends."""
        self._body = body

    def __iter__(self) -> Iterator[bytes]:
        """Yields the whole body again on every pass, `_UPLOAD_CHUNK_BYTES` at a time."""
        for start in range(0, len(self._body), _UPLOAD_CHUNK_BYTES):
            yield self._body[start : start + _UPLOAD_CHUNK_BYTES]


class _AsyncChunkedBody:
    """The async twin of `_ChunkedBody`; only async-iterable, so httpx sends it on an `AsyncClient`."""

    def __init__(self, body: bytes) -> None:
        """Holds the encoded body every pass sends."""
        self._chunks = _ChunkedBody(body)

    async def __aiter__(self) -> AsyncIterator[bytes]:
        """Yields the whole body again on every pass, as `_ChunkedBody` does."""
        for chunk in self._chunks:
            yield chunk


def _check_headers(headers: Mapping[str, str]) -> None:
    """Refuses a header no HTTP request can carry, once, rather than on every retried attempt.

    A CR, LF or NUL in a name or value would otherwise fail inside the transport, which reads as a
    connection error and is retried with backoff although every attempt fails the same way.
    """
    for name, value in headers.items():
        if not name or any(char in name for char in "\r\n\0:") or any(char in value for char in "\r\n\0"):
            raise GumletError(f"The upload header {name!r} is not a valid HTTP header.")


def _file_headers(file: FileTypes) -> Mapping[str, str]:
    """The headers a `(name, content, type, headers)` file tuple carries, or none for any other form."""
    if isinstance(file, tuple):
        parts: Tuple[Any, ...] = file
        if len(parts) > 3 and isinstance(parts[3], Mapping):
            given: Mapping[Any, Any] = parts[3]
            return {str(name): str(value) for name, value in given.items()}
    return {}


def _split_file(file: FileTypes) -> Tuple[Optional[str], object, Optional[str]]:
    """Splits the SDK's file input forms into filename, content and content type."""
    if isinstance(file, tuple):
        parts: Tuple[Any, ...] = file
        filename = parts[0] if len(parts) > 0 else None
        content = parts[1] if len(parts) > 1 else b""
        content_type = parts[2] if len(parts) > 2 else None
        return filename, content, content_type
    return None, file, None


def _read_file(file: FileTypes) -> Tuple[Optional[str], bytes, Optional[str]]:
    """Reads the whole file once, so every retry sends the same bytes."""
    filename, content, content_type = _split_file(file)
    if isinstance(content, os.PathLike):
        path = pathlib.Path(content)
        return filename or path.name, path.read_bytes(), content_type
    if isinstance(content, (bytes, bytearray)):
        return filename, bytes(content), content_type
    read = getattr(content, "read", None)
    if callable(read):
        data = read()
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("Expected the file to be opened in binary mode")
        name = getattr(content, "name", None)
        return filename or (os.path.basename(name) if isinstance(name, str) else None), bytes(data), content_type
    raise TypeError(f"Expected a file path, bytes or a binary file object, got {type(content)}")


async def _async_read_file(file: FileTypes) -> Tuple[Optional[str], bytes, Optional[str]]:
    """The async twin of `_read_file`, reading paths without blocking the event loop."""
    filename, content, content_type = _split_file(file)
    if isinstance(content, os.PathLike):
        path = anyio.Path(content)
        return filename or path.name, await path.read_bytes(), content_type
    return _read_file((filename, content, content_type))  # type: ignore[arg-type]


def _should_retry(response: httpx.Response) -> bool:
    """Whether the SDK client itself would retry this response: `x-should-retry` first, then its statuses."""
    should_retry = response.headers.get("x-should-retry")
    if should_retry == "true":
        return True
    if should_retry == "false":
        return False
    return response.status_code in (408, 409, 429) or response.status_code >= 500


def _retry_after(headers: httpx.Headers) -> Optional[float]:
    """The wait in seconds a `retry-after-ms` or `Retry-After` header asks for, when it is a sane one (under a minute)."""
    try:
        millis = float(headers.get("retry-after-ms", ""))
        if 0 < millis < 60_000:
            return millis / 1000
    except ValueError:
        pass
    retry_after = headers.get("retry-after")
    if not retry_after:
        return None
    try:
        seconds = float(retry_after)
    except ValueError:
        parsed = email.utils.parsedate_tz(retry_after)
        if parsed is None:
            return None
        seconds = float(email.utils.mktime_tz(parsed) - time.time())
    return seconds if 0 < seconds < 60 else None


def _retry_delay(attempt: int) -> float:
    """Exponential backoff with jitter, capped at the client's ceiling."""
    delay: float = min(INITIAL_RETRY_DELAY * pow(2.0, min(attempt, 1000)), MAX_RETRY_DELAY)
    return delay * (1 - 0.25 * random.random())
