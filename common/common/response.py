import typing

from common.model import BaseModel
from common.packet import Packet
from common.session import Session


class Response(BaseModel):
    packet: Packet  # Packet response.
    session: Session  # Client connection session
    data: typing.Optional[bytearray] = None  # packet in bytearray format.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = self.packet.encode(self.session) if self.data is None else self.data
