# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["VideoAssetUpdateParams", "CallToAction"]


class VideoAssetUpdateParams(TypedDict, total=False):
    asset_id: Required[str]
    """Asset Id"""

    title: str
    """Specify a text string or identifier which can be used for filtering or searching the asset."""

    description: str
    """Attach some textual data with the asset. This field is neither searchable nor filterable."""

    tag: str
    """Specify a text string or identifier which can identify an asset or bunch of assets later. You can pass multiple comma separated values."""

    call_to_actions: Iterable[CallToAction]
    """CTA, is an explicit prompt within the video content encouraging viewers to take a particular action."""

    metadata: str
    """Set of key-value pairs that you can attach to this Asset. This can be useful for storing additional information.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>"""

    remove_subtitles: SequenceNotStr[str]
    """Comma separated string of language codes."""

    input: str
    """
    For replacing videos, pass this along with `asset_id`
    
    `{workspace_id}/{asset_id}/origin-{asset_id}`
    """

    reprocess: bool
    """To reprocess same video, pass this as true."""


class CallToAction(TypedDict, total=False):
    text: str

    url: str

    start_time: int

    end_time: int

    font_color: str
    """hex value of color"""

    background_color: str
    """hex code of color"""

    position_from_top: int
    """number of pixels from top"""

    position_from_right: str
    """number of pixels from right"""
