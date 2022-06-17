from dataclasses import dataclass, field

from src.common.common.document import Document


@dataclass(kw_only=True)
class SystemMessage(Document):
    __collection__: str = field(default="game_servers", repr=False, init=False)
    __database__: str = field(default="l2py", repr=False, init=False)
