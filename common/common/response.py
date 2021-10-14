import typing
from dataclasses import dataclass

from common.helpers.bytearray import ByteArray
from common.packet import Packet
from common.session import Session


@dataclass()
class Response:
    packet: Packet  # Packet response.
    session: Session  # Client connection session
    data: ByteArray = None  # packet in bytearray format.
    actions_after: typing.List[typing.Coroutine] = None

    def __post_init__(self):
        self.data = self.packet.encode(self.session) if self.data is None else self.data
        self.actions_after = self.actions_after if self.actions_after is not None else []
