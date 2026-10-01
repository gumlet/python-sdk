# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["VideoPlaylistListAllResponse", "VideoPlaylistListAllResponseItem"]


class VideoPlaylistListAllResponseItem(BaseModel):
    id: str
    """Playlist ID"""

    collection_id: Optional[str] = None
    """Workspace ID"""

    title: Optional[str] = None
    """Title of the playlist"""

    description: Optional[str] = None
    """Description of the playlist"""

    player_config: Optional[object] = None
    """Player configuration for the playlist"""


VideoPlaylistListAllResponse: TypeAlias = List[VideoPlaylistListAllResponseItem]
