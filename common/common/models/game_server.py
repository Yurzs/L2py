import time
from typing import ClassVar

from common.ctype import ctype
from common.document import Document


class GameServer(Document):
    __collection__: ClassVar[str] = "game_servers"
    __database__: ClassVar[str] = "l2py"

    server_id: ctype.char
    host: str
    port: ctype.uint32

    age_limit: ctype.char = 13
    is_pvp: ctype.bool = False
    online_count: ctype.short = 0
    max_online: ctype.short = 1000
    is_online: ctype.bool = False
    type: ctype.int32 = 1
    brackets: ctype.char = False
    last_alive: ctype.long = 0

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
        return await super().one(add_query={"server_id": int(server_id)}, **kwargs)
