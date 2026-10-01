# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["MultipartUploadRetrievePartURLResponse"]


class MultipartUploadRetrievePartURLResponse(BaseModel):
    asset_id: str
    """Asset ID"""

    part_number: str
    """Part number of the part that is to be uploaded"""

    part_upload_url: str
    """Upload URL for the part on which you need to send PUT request for blob of that part"""
