import dataclasses

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class MacroEntry(BaseDataclass):
    entry_id: ctype.int8
    type: ctype.int8
    skill_id: ctype.int32
    shortcut_id: ctype.int8
    command: str


@dataclasses.dataclass(kw_only=True)
class Macro(BaseDataclass):
    id: ctype.int32
    name: str
    icon: ctype.int8
    acronym: str = ""
    description: str = ""
    entries: list[MacroEntry] = dataclasses.field(default_factory=list)
