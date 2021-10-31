from dataclasses import dataclass, field

from common.document import Document


@dataclass
class SystemMessage(Document):
    __collection__: String = field(default="game_servers", repr=False, init=False)
    __database__: String = field(default="l2py", repr=False, init=False)
