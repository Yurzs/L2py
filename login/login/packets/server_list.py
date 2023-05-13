from typing import ClassVar

from pydantic import Field

from common.ctype import ctype
from common.models import GameServer

from .base import LoginServerPacket


class ServerList(LoginServerPacket):
    type: ctype.char = 4
    servers: list[GameServer] = Field(default_factory=list)

    def encode(self, session, strings_format="utf8"):
        account = session.account
        arr = bytearray(self.type)
        arr.extend(ctype.char(len(self.servers)))
        arr.extend(ctype.char(0) if account.last_server is None else account.last_server)
        for server in self.servers:
            arr.extend(
                server.encode(
                    include=[
                        "server_id",
                        "host_as_bytearray",
                        "port",
                        "age_limit",
                        "is_pvp",
                        "online_count",
                        "max_online",
                        "server_is_alive",
                        "type",
                        "brackets",
                    ],
                    strings_format=strings_format,
                )
            )
        print("Arr len", len(arr))
        arr.append(0)
        print(arr)
        return arr
