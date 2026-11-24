# Gumlet

This library provides convenient access to the Gumlet REST API from Python.

The REST API documentation can be found on [docs.gumlet.com](https://docs.gumlet.com/reference). The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [File uploads](#file-uploads)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Webhooks](#webhooks)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install gumlet
```

<br />

## Usage

```python
import os

from gumlet import Gumlet

client = Gumlet(
    api_key=os.environ.get("API_KEY"),
)

video_asset = client.video_assets.create(
    input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
    format="ABR",
    title="Example Title",
    workspace_id="<your workspace id>",
    idempotency_key="",
)

print(video_asset)
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncGumlet`) exposing the same resource tree with `await`.

```python
import asyncio

from gumlet import AsyncGumlet


async def main() -> None:
    client = AsyncGumlet()
    video_asset = await client.video_assets.create(
        input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        format="ABR",
        title="Example Title",
        workspace_id="<your workspace id>",
        idempotency_key="",
    )


asyncio.run(main())
```

<br />

## File uploads

Some methods upload a file to a pre-signed URL the API returns, usually on another host, then confirm the upload where the API asks for that. The upload goes out on a short-lived HTTP client of its own, carrying only the file, its content type and the headers the API named for it: none of the client's credentials, default headers, default query or cookies, and none of the `auth`, headers, cookies, params or event hooks of a custom `http_client`. The client's retries and timeout apply. The upload URL must be `https:` (plain `http:` only to this machine), and a redirect from the upload host is refused rather than followed.

Without an `http_client`, the upload goes out on httpx's defaults: it takes its proxy and CA settings from the environment (`HTTPS_PROXY`, `SSL_CERT_FILE` and the like) when it is sent. With one you pass, the upload uses that client's proxy and TLS settings — `proxy=`, `mounts=`, `verify=` (`verify=False` included) and `cert=`, so a corporate proxy or a private CA works for uploads too, and a client certificate is presented to the upload host — when the transport the client would send the upload URL through is httpx's own `httpx.HTTPTransport` (`httpx.AsyncHTTPTransport` on the async client). Any other transport class, such as a subclass of your own or `DefaultAioHttpClient`'s, sends the request itself and could add headers, credentials or cookies, so with one the upload falls back to httpx's defaults as if no `http_client` were passed. So does an httpx transport bound to a Unix socket (`uds=`).

When your proxy or TLS setup lives only in a transport class of your own, opt that transport in by inheriting `SignedUploadTransport` (`from gumlet import SignedUploadTransport`), as in `class CorporateTransport(SignedUploadTransport, httpx.HTTPTransport)`. Inheriting it declares that the transport sends a request as handed over: it adds no credentials, cookies or headers of its own, keeps no session or cookie jar that would, is bound to no Unix socket, follows no redirects and honours the timeout httpx hands it with each request, which is the only way the upload's timeout reaches it. The upload then goes through it, still carrying only the file, its type and the headers the API named. The SDK checks the marker, not what it promises, and reads it off the transport the client routes the upload URL to, so a wrapper around another transport has to inherit it itself.

The same goes the other way: an `http_client` that trusts only a private CA, or whose proxy reaches only the API, applies that to the upload host too. Mount the transport the upload host needs, such as `mounts={"https://uploads.example.com": httpx.HTTPTransport()}` (`httpx.AsyncHTTPTransport()` on the async client) for httpx's default CA bundle and no proxy, and the upload uses that mount.

A transport the upload borrows this way is used as the client built it. Its proxy routing and its trusted CAs are the ones the client settled on when it was created, environment variables included, as for its API calls, so a change to `HTTPS_PROXY`, `NO_PROXY`, `SSL_CERT_FILE` or `SSL_CERT_DIR` after that does not reach the upload. The upload also takes a connection from the client's pool, so it counts against the client's `limits` and, when the pool is full, waits for a free connection within its timeout like any other request. The timeout counts time without progress while the file goes out, but once the operating system has accepted the last of it, the wait for the upload host's answer is a single read. On a slow link that read can include the seconds the system still needs to send what it buffered, so keep an upload's timeout well above a few seconds.

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str \| None` | - | Credential for the API_KEY scheme. Defaults to API_KEY. |

Declared schemes:

- `API_KEY` bearer token

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from gumlet import APIStatusError

try:
    video_asset = client.video_assets.create(
        input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        format="ABR",
        title="Example Title",
        workspace_id="<your workspace id>",
        idempotency_key="",
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `400`, `401`, `402`, `403`, `404`, `413`, `422`, `500`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from gumlet import Gumlet

client = Gumlet(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str \| None` | `os.environ.get("API_KEY")` | Credential for the API_KEY scheme. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Webhooks

The webhook helper verifies the signature of each delivery your server receives, then decodes its body into a typed event. Pass it the request body exactly as it arrived, before any JSON parsing, together with the request headers: the signature covers the raw body, so one that was parsed and re-serialized fails verification. A delivery whose signature does not verify is rejected before it is decoded.

```python
# `payload` is the raw request body; `headers` holds the request headers.
event = client.webhooks.unwrap(payload, headers=headers)
```

The signing secret comes from the client's `webhook_secret` option, which defaults to the `GUMLET_WEBHOOK_SECRET` environment variable. Pass `key` to use a different secret for one call.

The same resource also has:

- `client.webhooks.verify_signature(payload, headers)` checks a delivery's signature, and fails when it does not verify.
- `client.webhooks.parse_unsafe(payload)` decodes a body into a typed event without checking its signature. Use it only for a body verified elsewhere, or in tests.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `GUMLET_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `gumlet` logger.
- Importing the SDK wraps the process's log record factory: records from the SDK, `httpx`, `httpcore`, `hpack` and `websockets` loggers have credential headers, credential query parameters and URL userinfo logged as `***`. A record factory installed later that does not chain to the previous one turns this off.

<br />

## Requirements

- Python 3.9 or newer
