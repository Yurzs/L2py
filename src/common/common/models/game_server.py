# from __future__ import annotations

import dataclasses
import time

from src.common.common.ctype import ctype
from src.common.common.document import Document


@dataclasses.dataclass(kw_only=True)
class GameServer(Document):
    __collection__ = "game_servers"
    __database__ = "l2py"

    id: ctype.char
    host: str
    port: ctype.int

    age_limit: ctype.char = 13
    is_pvp: ctype.bool = False
    online_count: ctype.short = 0
    max_online: ctype.short = 1000
    is_online: ctype.bool = False
    type: ctype.int = 1
    brackets: ctype.char = False
    last_alive: ctype.long = 0

    __encode__ = (
        "id",
        "host_as_bytearray",
        "port",
        "age_limit",
        "is_pvp",
        "online_count",
        "max_online",
        "server_is_alive",
        "type",
        "brackets",
    )

    @property
    def is_full(self) -> ctype.bool:
        return self.online_count >= self.max_online

    @property
    def host_as_bytearray(self) -> bytearray:
        return bytearray([int(i) for i in self.host.split(".")])

    @property
    def server_is_alive(self) -> ctype.bool:
        return ctype.bool(self.last_alive >= time.time() - 15)

    @classmethod
    async def one(cls, server_id, **kwargs) -> "GameServer":
        return await super().one(add_query={"id": int(server_id)}, **kwargs)
