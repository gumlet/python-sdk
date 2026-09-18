# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationDataFetchOrgResponse", "PlanData", "PlanDataImage", "PlanDataVideo", "Metadata"]


class Metadata(BaseModel):
    first_image_source_created: bool = FieldInfo(alias="firstImageSourceCreated")

    first_video_uploaded: bool = FieldInfo(alias="firstVideoUploaded")

    nsfw_blocked: bool
    """Flag is org is blocked for NSFW uploads."""


class PlanDataVideo(BaseModel):
    plan: str
    """Video plan name"""

    cycle: Literal["monthly", "yearly"]
    """Billing cycle. `monthly` or `yearly`."""

    trialing: bool
    """If the plan is under trial or not."""

    display_name: str


class PlanDataImage(BaseModel):
    plan: str
    """Image plan name"""

    cycle: Literal["monthly", "yearly"]
    """Billing cycle. `monthly` or `yearly`."""

    trialing: bool
    """If the plan is under trial or not."""

    display_name: str


class PlanData(BaseModel):
    image: PlanDataImage

    video: PlanDataVideo


class OrganizationDataFetchOrgResponse(BaseModel):
    id: str
    """Organization ID"""

    org_email: str
    """Primary email of the organization"""

    unpaid: bool
    """Flag if account is blocked due to unpaid dues. False means account is not blocked."""

    created_at: float
    """Org creation time. Epoch timestamp in milliseconds."""

    plan: str
    """Subscription plan name"""

    plan_cycle: Literal["monthly", "yearly"]
    """Billing cycle. `monthly` or `yearly`."""

    plan_data: PlanData

    stripe_account_loc: Literal["ind", "sgp"]

    sso_enabled: Optional[bool] = None
    """Flag if SSO is enabled for org."""

    got_free_trial: Optional[bool] = None

    metadata: Optional[Metadata] = None
