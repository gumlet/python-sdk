# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "VideoAssetRetrieveDetailsResponse",
    "Input",
    "InputTransformations",
    "InputTransformationsImageOverlay",
    "InputTransformationsGenerateSubtitles",
    "InputTransformationsPreviewThumbnails",
    "InputTransformationsDrm",
    "InputChapter",
    "Output",
    "OutputStorageDetails",
    "OutputStorageDetailsVideo",
    "OutputStorageDetailsAudio",
    "OutputStorageDetailsPlaylist",
    "OutputStorageDetailsThumbnail",
    "OutputStorageDetailsSubtitle",
    "OutputStorageDetailsPreviewThumbnail",
    "Warning",
    "VideoProtection",
    "AccessControls",
]


class AccessControls(BaseModel):
    password: Optional[str] = None
    """Hidden password field"""


class VideoProtection(BaseModel):
    signed_url: Optional[bool] = None
    """Flag is signed URL is enabled for this asset"""


class Warning(BaseModel):
    code: str
    """Warning code for the asset"""

    message: str
    """Human friendly warning message"""


class OutputStorageDetailsPreviewThumbnail(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    size: Optional[int] = None


class OutputStorageDetailsSubtitle(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    size: Optional[int] = None


class OutputStorageDetailsThumbnail(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    size: Optional[int] = None

    resolution: Optional[str] = None


class OutputStorageDetailsPlaylist(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    size: Optional[int] = None


class OutputStorageDetailsAudio(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    size: Optional[int] = None

    duration: Optional[int] = None


class OutputStorageDetailsVideo(BaseModel):
    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    size: Optional[int] = None

    resolution: Optional[str] = None

    duration: Optional[int] = None


class OutputStorageDetails(BaseModel):
    video: Optional[List[OutputStorageDetailsVideo]] = None

    audio: Optional[List[OutputStorageDetailsAudio]] = None

    playlist: Optional[List[OutputStorageDetailsPlaylist]] = None

    thumbnail: Optional[List[OutputStorageDetailsThumbnail]] = None

    subtitle: Optional[List[OutputStorageDetailsSubtitle]] = None

    preview_thumbnail: Optional[List[OutputStorageDetailsPreviewThumbnail]] = FieldInfo(
        alias="previewThumbnail", default=None
    )


class Output(BaseModel):
    format: Optional[str] = None

    status_url: Optional[str] = None

    playback_url: Optional[str] = None

    dash_playback_url: Optional[str] = None

    thumbnail_url: Optional[List[str]] = None

    storage_details: Optional[OutputStorageDetails] = None

    transcription_word_level_timestamps: Optional[str] = None

    storage_bytes: Optional[int] = None

    preview_thumbnails_url: Optional[str] = None


class InputChapter(BaseModel):
    end_time: Optional[int] = FieldInfo(alias="endTime", default=None)

    label: Optional[str] = None


class InputTransformationsDrm(BaseModel):
    type: Literal["widevine", "fairplay", "clearkey", "widevine,fairplay", "fairplay,widevine"]


class InputTransformationsPreviewThumbnails(BaseModel):
    max_tiles: Optional[int] = None


class InputTransformationsGenerateSubtitles(BaseModel):
    audio_language: Optional[str] = None

    subtitle_languages: Optional[List[str]] = None


class InputTransformationsImageOverlay(BaseModel):
    url: Optional[str] = None

    vertical_align: Optional[str] = None

    horizontal_align: Optional[str] = None

    vertical_margin: Optional[str] = None

    horizontal_margin: Optional[str] = None

    width: Optional[str] = None

    height: Optional[str] = None

    image_downloaded: Optional[bool] = None


class InputTransformations(BaseModel):
    format: Optional[str] = None

    resolution: Optional[List[str]] = None

    audio_codec: Optional[List[str]] = None

    video_codec: Optional[List[str]] = None

    image_overlay: Optional[InputTransformationsImageOverlay] = None

    thumbnail: Optional[List[str]] = None

    thumbnail_format: Optional[str] = None

    mp4_access: Optional[bool] = None

    audio_only: Optional[bool] = None

    original_deleted: Optional[bool] = None

    per_title_encoding: Optional[bool] = None

    generate_subtitles: Optional[InputTransformationsGenerateSubtitles] = None

    preview_thumbnails: Optional[InputTransformationsPreviewThumbnails] = None

    pre_processing_successful: Optional[bool] = None
    """Flag indicating if the pre-processing was successful"""

    generate_chapters: Optional[bool] = None
    """Flag if AI chapter generation is enabled"""

    drm: Optional[InputTransformationsDrm] = None

    generate_description: Optional[bool] = None
    """Flag if AI description generation is enabled"""


class Input(BaseModel):
    transformations: Optional[InputTransformations] = None

    profile_id: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    chapters: Optional[List[InputChapter]] = None

    source_url: Optional[str] = None

    size: Optional[int] = None

    duration: Optional[float] = None

    aspect_ratio: Optional[str] = None

    fps: Optional[float] = None

    width: Optional[int] = None

    height: Optional[int] = None


class VideoAssetRetrieveDetailsResponse(BaseModel):
    asset_id: str

    progress: Optional[int] = None

    created_at: int
    """Asset created timestamp in milliseconds since epoch"""

    updated_at: Optional[int] = None
    """Asset updated timestamp in milliseconds since epoch"""

    status: str

    tag: Optional[List[str]] = None

    source_id: Optional[str] = None

    collection_id: Optional[str] = None

    input: Optional[Input] = None

    output: Optional[Output] = None

    processed_at: Optional[int] = None

    folder: Optional[str] = None

    playlists: Optional[List[str]] = None
    """Array of Playlist IDs"""

    thumbnail_updated_at: Optional[int] = None
    """Thumbnail updated timestamp in milliseconds since epoch"""

    collection_updated_at: int
    """Collection updated timestamp in milliseconds since epoch"""

    warning: Optional[List[Warning]] = None

    audio_only: Optional[bool] = FieldInfo(alias="audioOnly", default=None)
    """If `true` the asset is audio only"""

    video_protection: Optional[VideoProtection] = None

    access_control: Optional[Literal["private", "public", "password-protected", "dashboardOnly"]] = None
    """Access control"""

    access_controls: Optional[AccessControls] = None
