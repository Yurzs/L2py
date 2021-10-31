import time
import typing
from dataclasses import dataclass, field

from common.helpers.bytearray import ByteArray
from common.models.game_server import GameServer

from .base import LoginServerPacket


@dataclass
class ServerList(LoginServerPacket):
    type: Int8 = field(default=4, init=False, repr=False)
    servers: typing.List[GameServer] = ()

    def encode(self, session):
        account = session.account
        arr = ByteArray(self.type.encode())
        arr.append(Int8(len(self.servers)))
        arr.append(Int8(0 if account.last_server is None else account.last_server))
        for server in self.servers:
            arr.extend(server.id)
            ip = server.host.split(".")
            arr.append(Int8(ip[0]))
            arr.append(Int8(ip[1]))
            arr.append(Int8(ip[2]))
            arr.append(Int8(ip[3]))
            arr.append(server.port)
            arr.append(server.age_limit)
            arr.append(server.is_pvp)
            arr.append(server.online_count)
            arr.append(server.max_online)
            is_online = Bool(server.last_alive > time.time() - 15)
            arr.append(Bool(is_online))
            arr.append(server.type)
            arr.append(server.brackets)
        arr.append(Int8(0))
        return arr
