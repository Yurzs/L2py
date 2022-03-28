import typing
from dataclasses import dataclass

from common.dataclass import BaseDataclass
from common.helpers.bytearray import ByteArray
from common.session import Session


@dataclass
class Request(BaseDataclass):
    raw_data: ByteArray  # Data received from socket
    session: Session  # Client connection session
    data: bytearray = None  # Data modified during processing
    validated_data: typing.Dict[str, typing.Any] = None

    def __post_init__(self):
        self.data = self.data if self.data is not None else self.raw_data
        self.validated_data = self.validated_data or {}
