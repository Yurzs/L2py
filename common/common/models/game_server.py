from dataclasses import dataclass, field

from common.document import Document, DocumentDefaults
from common.helpers.cython import cython


@dataclass
class GameServerBase:
    id: cython.char
    host: str
    port: cython.long


@dataclass
class GameServerDefaults(DocumentDefaults):
    age_limit: cython.char = 13
    is_pvp: cython.bint = False
    online_count: cython.int = 0
    max_online: cython.int = 500
    is_online: cython.bint = False
    type: cython.long = 1
    brackets: cython.char = 0
    last_alive: cython.long = 0


@dataclass
class GameServer(Document, GameServerDefaults, GameServerBase):
    __collection__: str = field(default="game_servers", repr=False, init=False)
    __database__: str = field(default="l2py", repr=False, init=False)

    @property
    def is_full(self):
        return self.online_count >= self.max_online

    @classmethod
    async def one(cls, server_id, **kwargs) -> "GameServer":
        return await super().one(add_query={"id": int(server_id)}, **kwargs)
