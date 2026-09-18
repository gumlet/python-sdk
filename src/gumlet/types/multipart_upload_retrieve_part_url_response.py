# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MultipartUploadRetrievePartURLResponse"]


class MultipartUploadRetrievePartURLResponse(BaseModel):
    asset_id: Optional[str] = None

    part_number: Optional[str] = None

    part_upload_url: Optional[str] = None
