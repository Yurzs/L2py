import typing
from dataclasses import dataclass, field

from src.common.common.packet import Packet
from src.common.common.session import Session


@dataclass(kw_only=True)
class Response:
    packet: Packet  # Packet response.
    session: Session  # Client connection session
    data: typing.Optional[bytearray] = None  # packet in bytearray format.
    encode: bool = field(default=True)

    def __post_init__(self):
        self.data = self.packet.encode(self.session) if self.data is None else self.data
