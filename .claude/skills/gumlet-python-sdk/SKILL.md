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
    collection_id="646df1c9173a4a2fcac180b4",
    profile_id="646df1c9173a4a2fcac180b7",
    format="ABR",
    tag=["ball"],
    description="some description",
    metadata={"headermeta": "metavalue"},
    call_to_actions=[
        {
            "start_time": 1,
            "end_time": 90,
            "text": "some test",
            "url": "https://some-url.com",
            "position_from_top": 11,
            "position_from_right": 23,
            "border_radius": "11",
            "font_color": "#000001",
            "background_color": "#ffffff",
        }
    ],
    playlist_id="6597acd5ed6f26a9c5ca9633",
    folder="697375fbfa2d1037283140e4",
)

print(video_asset)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](../../../api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from gumlet import APIStatusError

try:
    video_asset = client.video_assets.create(
        input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
        collection_id="646df1c9173a4a2fcac180b4",
        profile_id="646df1c9173a4a2fcac180b7",
        format="ABR",
        tag=["ball"],
        description="some description",
        metadata={"headermeta": "metavalue"},
        call_to_actions=[
            {
                "start_time": 1,
                "end_time": 90,
                "text": "some test",
                "url": "https://some-url.com",
                "position_from_top": 11,
                "position_from_right": 23,
                "border_radius": "11",
                "font_color": "#000001",
                "background_color": "#ffffff",
            }
        ],
        playlist_id="6597acd5ed6f26a9c5ca9633",
        folder="697375fbfa2d1037283140e4",
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](../../../README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](../../../api.md) — complete catalogue of every operation with request and response types.
