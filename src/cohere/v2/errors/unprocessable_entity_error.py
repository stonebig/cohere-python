# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError
from ..types.unprocessable_entity_error_body import UnprocessableEntityErrorBody


class UnprocessableEntityError(ApiError):
    def __init__(self, body: UnprocessableEntityErrorBody):
        super().__init__(status_code=422, body=body)
