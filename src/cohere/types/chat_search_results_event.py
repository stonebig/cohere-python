# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .chat_document import ChatDocument
from .chat_search_result import ChatSearchResult
from .chat_stream_event import ChatStreamEvent

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ChatSearchResultsEvent(ChatStreamEvent):
    search_results: typing.Optional[typing.List[ChatSearchResult]] = pydantic.Field(
        description="Conducted searches and the ids of documents retrieved from each of them."
    )
    documents: typing.List[ChatDocument] = pydantic.Field(
        description="Documents fetched from searches or provided by the user."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
