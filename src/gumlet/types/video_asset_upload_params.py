# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr

__all__ = [
    "VideoAssetUploadParams",
    "Crop",
    "Pad",
    "Trim",
    "ImageOverlay",
    "TextOverlay",
    "AnimatedGif",
    "AdditionalTrack",
    "GenerateSubtitles",
    "CallToAction",
]


class VideoAssetUploadParams(TypedDict, total=False):
    collection_id: Required[str]
    """Gumlet video workspace id."""

    profile_id: str
    """Provide `profile_id` of the previously created video profile. This parameter will override all the parameters (except `input` and `collection_id`) from the video profile."""

    format: Literal["ABR", "MP4"]
    """Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and`MP4`."""

    tag: SequenceNotStr[str]
    """Specify a text string or identifier which can identify an asset or bunch of assets later."""

    title: str
    """Specify a text string or identifier which can be used for filtering or searching the asset."""

    description: str
    """Attach some textual data with the asset. This field is neither searchable nor filterable."""

    metadata: Dict[str, object]
    """Add your metadata you want to associate with this asset.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code>"""

    width: str
    """Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Applicable only when specified format is `MP4`."""

    height: str
    """Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Applicable only when specified format is `MP4`."""

    resolution: str
    """Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values: `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio."""

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
    """Create an animated GIF from the video."""

    additional_tracks: Iterable[AdditionalTrack]
    """Add additional Audio / Subtitle tracks to Gumlet for transcoding and delivery along with video asset track."""

    generate_subtitles: GenerateSubtitles
    """Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)"""

    mp4_access: bool
    """Creates `MP4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`**"""

    per_title_encoding: bool
    """Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`**"""

    process_low_resolution_input: bool
    """Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`**"""

    audio_only: bool
    """This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`**"""

    enable_drm: bool
    """Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs."""

    call_to_actions: Iterable[CallToAction]
    """CTA, is an explicit prompt within the video content encouraging viewers to take a particular action."""

    playlist_id: str
    """Add this asset to a playlist."""

    folder: str
    """Add this asset to an existing folder by `folder_id`."""


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

    position_from_right: int
    """number of pixels from right"""


class GenerateSubtitles(TypedDict, total=False):
    audio_language: str
    """Language code for native language of the audio."""

    subtitle_languages: str
    """Comma separated string of language codes for which subtitle needs to be generated. Maximum four language codes are allowed."""


class AdditionalTrack(TypedDict, total=False):
    url: Required[str]
    """URL or web address of a file that Gumlet should download to add a stream."""

    type: Required[str]
    """Type of additional track. Value can be either audio or subtitle."""

    language_code: Required[str]
    """The language code value represents BCP 47 specification compliant value. For example, en for English."""

    name: str
    """The name of the track containing a human-readable description."""


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
    """Text to be overlayed on video."""

    horizontal_align: str
    """This parameter specifies the horizontal alignment of the overlayed image and can be either `left` or `right`. **Default: `right`**"""

    vertical_align: str
    """This parameter specifies the vertical alignment of the overlayed image and can be either `top` or `bottom`. **Default: `bottom`**"""

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
    """This parameter allows rectangular drawing a box over the overlayed text. **Default: `false`**"""

    box_color: str
    """Box color can be specified with this parameter. **Default: `white`**"""

    box_opacity: str
    """Box opacity can be specified with this parameter. **Default: `100`**"""

    box_border: str
    """Padding between the box border and the text can be specified with this parameter in pixels. **Default: `0`**"""


class ImageOverlay(TypedDict, total=False):
    url: Required[str]
    """This is the required parameter for image overlay, it can be a URL to an image that needs to be overlayed."""

    horizontal_margin: str
    """This parameter defines the horizontal coordinate value of the corner (determined by `horizontal_align`) of the overlay area. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`**"""

    vertical_margin: str
    """This parameter defines the vertical coordinate value of the corner (determined by `vertical_align`) of the overlay area. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `0`**"""

    horizontal_align: str
    """This parameter specifies the horizontal alignment of the overlayed image and can be either `left` or `right`. **Default: `right`**"""

    vertical_align: str
    """This parameter specifies the vertical alignment of the overlayed image and can be either `top` or `bottom`. **Default: `bottom`**"""

    width: str
    """Width of the overlayed image. **Default: `image width`**"""

    height: str
    """Height of the overlayed image. **Default: `image height`**"""


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
