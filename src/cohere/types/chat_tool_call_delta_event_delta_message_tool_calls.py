# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .chat_tool_call_delta_event_delta_message_tool_calls_function import (
    ChatToolCallDeltaEventDeltaMessageToolCallsFunction,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ChatToolCallDeltaEventDeltaMessageToolCalls(UncheckedBaseModel):
    function: typing.Optional[ChatToolCallDeltaEventDeltaMessageToolCallsFunction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
