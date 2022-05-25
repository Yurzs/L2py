import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.session import Session


@dataclass(kw_only=True)
class Request(BaseDataclass):
    raw_data: bytearray  # Data received from socket
    session: Session  # Client connection session
    data: bytearray = field(
        default_factory=bytearray
    )  # Data modified during processing
    validated_data: typing.Dict[str, typing.Any] = field(default_factory=dict)

    def __post_init__(self):
        self.data = self.raw_data
        self.validated_data = self.validated_data or {}
