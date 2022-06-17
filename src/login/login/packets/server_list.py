import typing
from dataclasses import dataclass, field, fields

from src.common.common.ctype import ctype
from src.common.common.models import GameServer

from .base import LoginServerPacket


@dataclass(kw_only=True)
class ServerList(LoginServerPacket):
    type: ctype.char = field(default=4, init=False, repr=False)
    servers: typing.List[GameServer] = ()

    def encode(self, session):
        account = session.account
        arr = bytearray(self.type)
        arr.extend(ctype.char(len(self.servers)))
        arr.extend(ctype.char(0) if account.last_server is None else account.last_server)
        for server in self.servers:
            arr.extend(server.encode(strings_format="utf8"))
        print("Arr len", len(arr))
        arr.append(0)
        return arr
