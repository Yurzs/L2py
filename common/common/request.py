import typing

from pydantic import Field

from common.model import BaseModel
from common.session import Session


class Request(BaseModel):
    raw_data: bytearray  # Data received from socket
    session: Session  # Client connection session
    data: bytearray = Field(default_factory=bytearray)  # Data modified during processing
    validated_data: typing.Dict[str, typing.Any] = Field(default_factory=dict)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = self.raw_data
