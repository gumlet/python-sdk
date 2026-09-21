---
name: gumlet-python-sdk
description: "Python SDK for Gumlet API. Use when writing Python code that calls Gumlet API with the gumlet package: installing it, constructing and authenticating the client, and calling API operations."
---

# Gumlet Python SDK

Generated Python client for Gumlet API, published as `gumlet`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install gumlet
```

## Client setup and authentication

```python
import os

from gumlet import Gumlet

client = Gumlet(
    api_key=os.environ.get("API_KEY"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `api_key` (env: `API_KEY`) — Credential for the API_KEY scheme.

## Calling operations

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
)

print(video_asset)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](./api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from gumlet import APIStatusError

try:
    video_asset = client.video_assets.create(
        input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        format="ABR",
        title="Example Title",
        workspace_id="<your workspace id>",
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](./README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](./api.md) — complete catalogue of every operation with request and response types.
