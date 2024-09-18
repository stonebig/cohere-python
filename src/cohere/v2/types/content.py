# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
import typing_extensions
from ...core.unchecked_base_model import UnionMetadata


class TextContent(UncheckedBaseModel):
    """
    A Content block which contains information about the content type and the content itself.
    """

    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Content = typing_extensions.Annotated[TextContent, UnionMetadata(discriminant="type")]
