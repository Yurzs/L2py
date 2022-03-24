from dataclasses import dataclass, field

from common import datatypes
from common.document import Document


@dataclass
class GameServer(Document):
    __collection__: datatypes.String = field(default="game_servers", repr=False, init=False)
    __database__: datatypes.String = field(default="l2py", repr=False, init=False)

    _id: datatypes.Int8
    host: datatypes.String
    port: datatypes.Int32
    age_limit: datatypes.Int8 = 13
    is_pvp: datatypes.Int8 = False
    online_count: datatypes.Int16 = 0
    max_online: datatypes.Int16 = 500
    is_online: datatypes.Int8 = False
    type: datatypes.Int32 = 1
    brackets: datatypes.Int8 = 0

    @property
    def is_full(self):
        return self.online_count >= self.max_online
