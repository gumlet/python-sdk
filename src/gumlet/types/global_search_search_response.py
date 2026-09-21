# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "GlobalSearchSearchResponse",
    "AllFolder",
    "AllFolderHighlight",
    "AllFolderHighlightText",
    "AllAsset",
    "AllAssetHighlight",
    "AllAssetHighlightText",
    "AllPlaylist",
    "AllPlaylistHighlight",
    "AllPlaylistHighlightText",
    "AllChannel",
    "AllChannelHighlight",
    "AllChannelHighlightText",
]


class AllChannelHighlightText(BaseModel):
    value: str
    """The word to highlight or not"""

    type: Literal["hit", "text"]
    """Whether this word needs highlight"""


class AllChannelHighlight(BaseModel):
    score: float
    """Search ranking score"""

    path: str
    """Which field to highlight"""

    texts: List[AllChannelHighlightText]


class AllChannel(BaseModel):
    title: str
    """Channel title"""

    description: str
    """Channel description"""

    created_at: int
    """Created at timestamp in milliseconds since epoch"""

    updated_at: int
    """Updated at timestamp in milliseconds since epoch"""

    workspace_id: str
    """Workspace ID on in which this channel resides"""

    highlight: List[AllChannelHighlight]


class AllPlaylistHighlightText(BaseModel):
    value: str
    """The word to highlight or not"""

    type: Literal["hit", "text"]
    """Whether this word needs highlight"""


class AllPlaylistHighlight(BaseModel):
    score: float
    """Search ranking score"""

    path: str
    """Which field to highlight"""

    texts: List[AllPlaylistHighlightText]


class AllPlaylist(BaseModel):
    id: str
    """Playlist ID"""

    title: str
    """Playlist title"""

    description: str
    """Playlist description"""

    created_at: int
    """Created at timestamp in milliseconds since epoch"""

    updated_at: int
    """Updated at timestamp in milliseconds since epoch"""

    workspace_id: str
    """Workspace ID on in which this playlist resides"""

    highlight: List[AllPlaylistHighlight]


class AllAssetHighlightText(BaseModel):
    value: str
    """The word to highlight or not"""

    type: Literal["hit", "text"]
    """Whether this word needs highlight"""


class AllAssetHighlight(BaseModel):
    score: float
    """Search ranking score"""

    path: str
    """Which field to highlight"""

    texts: List[AllAssetHighlightText]


class AllAsset(BaseModel):
    id: str
    """Asset ID"""

    title: str
    """Asset Title"""

    tags: List[str]
    """List of tags applied to this asset"""

    workspace_id: str
    """Workspace ID on in which this asset resides"""

    created_at: int
    """Created at timestamp in milliseconds since epoch"""

    updated_at: int
    """Updated at timestamp in milliseconds since epoch"""

    highlight: List[AllAssetHighlight]


class AllFolderHighlightText(BaseModel):
    value: str
    """The word to highlight or not"""

    type: Literal["hit", "text"]
    """Whether this word needs highlight"""


class AllFolderHighlight(BaseModel):
    score: float
    """Search ranking score"""

    path: str
    """Which field to highlight"""

    texts: List[AllFolderHighlightText]


class AllFolder(BaseModel):
    id: str
    """Folder ID"""

    created_at: int
    """Created at timestamp in milliseconds since epoch"""

    updated_at: int
    """Updated at timestamp in milliseconds since epoch"""

    workspace_id: str
    """Workspace ID in which the folder resides"""

    highlight: List[AllFolderHighlight]


class GlobalSearchSearchResponse(BaseModel):
    all_folders: List[AllFolder]
    """Result array of all folders"""

    all_assets: List[AllAsset]
    """Result array of all assets"""

    all_playlists: List[AllPlaylist]
    """Result array of all playlists"""

    all_channels: List[AllChannel]
    """Result array of all channels"""
