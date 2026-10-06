# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, TYPE_CHECKING
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductEventWebhookEvent"]


class ProductEventWebhookEvent(BaseModel):
    type: Literal[
        "event.embed.viewed",
        "event.embed.cta_clicked",
        "event.video.updated",
        "event.video.uploaded",
        "event.playlist.created",
        "event.playlist.asset",
        "event.playlist.deleted",
        "event.video.analytics",
        "event.image.analytics",
        "event.embed.form_submitted",
        "event.comment.all",
        "event.channel.member_joined",
    ]
    """Product event that triggered this delivery."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]
