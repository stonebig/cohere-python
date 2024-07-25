# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .status import Status


class Event(UncheckedBaseModel):
    """
    A change in status of a fine-tuned model.
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the user who initiated the event. Empty if initiated by the system.
    """

    status: typing.Optional[Status] = pydantic.Field(default=None)
    """
    Status of the fine-tuned model.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the event happened.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
