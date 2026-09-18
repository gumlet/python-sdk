# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["VideoPlaylistListAllResponse", "VideoPlaylistListAllResponseItem"]


class VideoPlaylistListAllResponseItem(BaseModel):
    id: Optional[str] = None

    collection_id: Optional[str] = None

    title: Optional[str] = None

    description: Optional[str] = None

    player_config: Optional[object] = None


VideoPlaylistListAllResponse: TypeAlias = List[VideoPlaylistListAllResponseItem]
