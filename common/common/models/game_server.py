from dataclasses import dataclass, field

from common.document import Document, DocumentDefaults


@dataclass
class GameServerBase:
    id: Int8
    host: String
    port: Int32


@dataclass
class GameServerDefaults(DocumentDefaults):
    age_limit: Int8 = 13
    is_pvp: Int8 = False
    online_count: Int16 = 0
    max_online: Int16 = 500
    is_online: Int8 = False
    type: Int32 = 1
    brackets: Int8 = 0
    last_alive: Int32 = 0


@dataclass
class GameServer(Document, GameServerDefaults, GameServerBase):
    __collection__: String = field(default="game_servers", repr=False, init=False)
    __database__: String = field(default="l2py", repr=False, init=False)

    @property
    def is_full(self):
        return self.online_count >= self.max_online

    @classmethod
    async def one(cls, server_id, **kwargs) -> "GameServer":
        return await super().one(add_query={"id": int(server_id)}, **kwargs)
