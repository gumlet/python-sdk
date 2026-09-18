# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["VideoAssetDeleteManyResponse"]


class VideoAssetDeleteManyResponse(BaseModel):
    success: bool
    """Boolean parameter indicating if the delete was successful."""
