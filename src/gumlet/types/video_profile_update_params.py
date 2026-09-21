# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = [
    "VideoProfileUpdateParams",
    "Crop",
    "Pad",
    "Trim",
    "ImageOverlay",
    "TextOverlay",
    "AnimatedGif",
    "GenerateSubtitles",
]


class VideoProfileUpdateParams(TypedDict, total=False):
    body_profile_id: Required[Annotated[str, PropertyInfo(alias="profile_id")]]
    """Profile id of the profile which needs to be deleted."""

    name: str
    """Profile name or identifier."""

    format: Literal["ABR", "MP4"]
    """Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`."""

    width: str
    """Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Only applicable when specified `format` is `MP4`."""

    height: str
    """Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`."""

    resolution: str
    """Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`."""

    crop: Crop
    """This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video."""

    pad: Pad
    """This transformation can be used to add padding to the video."""

    trim: Trim
    """Trim transformation can be used to trim videos based on time duration."""

    image_overlay: ImageOverlay
    """Image overlay can be used to brand a video or add a visual label in the form of an image."""

    text_overlay: TextOverlay
    """Text overlay can be used to brand a video or add a label in the form of text."""

    animated_gif: AnimatedGif
    """Create an animated GIF from a video."""

    generate_subtitles: GenerateSubtitles
    """Gumlet allows you to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes). You can remove this object if you don't want to generate AI subtitles."""

    mp4_access: bool
    """Creates `mp4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**"""

    per_title_encoding: bool
    """Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**"""

    process_low_resolution_input: bool
    """Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**"""

    audio_only: bool
    """This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case,This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**"""

    enable_drm: bool
    """Enable DRM encryption for transcoded videos. Gumlet supports Widevine and FairPlay DRMs."""

    vc: SequenceNotStr[str]
    """Video Codecs"""

    generate_chapters: bool
    """Whether Gumlet should generate chapters."""

    generate_description: bool
    """Whether Gumlet should generate descriptions."""


class GenerateSubtitles(TypedDict, total=False):
    subtitle_languages: SequenceNotStr[str]
    """Array of string of language codes for which subtitle needs to be generated. Maximum four language codes are allowed."""

    transcribe: bool
    """This is by default true to generate the subtitles in the native audio."""


class AnimatedGif(TypedDict, total=False):
    start_offset: str
    """The time (in seconds or `HH:MM:SS` format) of the video timeline where the animated gif should begin. **Default: `0`**"""

    end_offset: str
    """The time (in seconds or `HH:MM:SS` format) of the video timeline where the GIF ends. Defaults to `10` seconds after the start_offset. Maximum duration of GIF is limited to `10` seconds."""

    width: str
    """The width in pixels (or in percentage value of asset width) of the animated GIF. Max width is `640px`."""

    height: str
    """The height in pixels (or in percentage value of asset height) of the animated GIF. Max height is `640px`."""

    fps: str
    """The frame rate of the generated GIF. Defaults to `15` fps. Max `30` fps."""


class TextOverlay(TypedDict, total=False):
    text: Required[str]
    """Text to be overlaid on video."""

    horizontal_align: str
    """This parameter specifies the horizontal alignment of the overlaid text and can be either `left` or `right`. **Default: `right`**"""

    vertical_align: str
    """This parameter specifies the vertical alignment of the overlaid text and can be either `top` or `bottom`. **Default: `bottom`**"""

    horizontal_margin: str
    """This parameter defines the horizontal coordinate value of the corner (determined by `horizontal_align`) of the overlay area. Values can be an absolute number of pixels relative to the video width. **Default: `0`**"""

    vertical_margin: str
    """This parameter defines the vertical coordinate value of the corner (determined by vertical_align) of the overlay area. Values can be an absolute number of pixels relative to the video height. **Default: `0`**"""

    color: str
    """Font color for text. **Default: `black`**"""

    font: str
    """Font family type for text. **Default: `sans`**"""

    font_size: str
    """Font size in pixels. **Default: `16`**"""

    opacity: str
    """Overlay text opacity can be specified with opacity parameter where value can be between `0` and `100` where `0` is considered completely transparent and `100` is considered completely opaque. **Default: `100`**"""

    box: bool
    """This parameter allows drawing a rectangular box over the overlaid text. **Default: `false`**"""

    box_color: str
    """Box color can be specified with this parameter. **Default: `white`**"""

    box_opacity: str
    """Box opacity can be specified with this parameter. **Default: `100`**"""

    box_border: str
    """Padding between the box border and the text can be specified with this parameter in pixels. **Default: `0`**"""


class ImageOverlay(TypedDict, total=False):
    url: Required[str]
    """This is the required parameter for image overlay; it can be a URL to an image that needs to be overlaid."""

    horizontal_margin: str
    """This parameter defines the horizontal coordinate value of the corner (determined by `horizontal_align`) of the overlay area. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`**"""

    vertical_margin: str
    """This parameter defines the vertical coordinate value of the corner (determined by `vertical_align`) of the overlay area. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `0`**"""

    horizontal_align: str
    """This parameter specifies the horizontal alignment of the overlaid image and can be either `left` or `right`. **Default: `right`**"""

    vertical_align: str
    """This parameter specifies the vertical alignment of the overlaid image and can be either `top` or `bottom`. **Default: `bottom`**"""

    width: str
    """Width of the overlaid image. **Default: `image width`**"""

    height: str
    """Height of the overlaid image. **Default: `image height`**"""


class Trim(TypedDict, total=False):
    start_offset: Required[float]
    """Start offset in number of seconds or in `HH:MM:SS` format."""

    end_offset: Required[float]
    """End offset in number of seconds or in `HH:MM:SS` format."""

    duration: float
    """Duration can be used in conjunction with `start_offset` parameter, can be specified in number of seconds."""


class Pad(TypedDict, total=False):
    top: str
    """Width of padding on the top side. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `%5`**"""

    left: str
    """Width of padding on the left side. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`**"""

    bottom: str
    """Width of padding on the bottom side. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `%5`**"""

    right: str
    """Width of padding on the right side. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`**"""

    color: str
    """Color of padding area. **Default: `black`**"""


class Crop(TypedDict, total=False):
    horizontal_margin: str
    """This parameter defines the horizontal coordinate value of the upper-left corner of the cropping area. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`**"""

    vertical_margin: str
    """This parameter defines the vertical coordinate value of the upper-left corner of the cropping area. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `0`**"""

    width: Required[str]
    """Width of the cropping area in pixels."""

    height: Required[str]
    """Height of the cropping area in pixels."""
