from pydantic import Field

from common.ctype import ctype
from common.model import BaseModel


class MacroEntry(BaseModel):
    entry_id: ctype.int8
    type: ctype.int8
    skill_id: ctype.int32
    shortcut_id: ctype.int8
    command: str


class Macro(BaseModel):
    id: ctype.int32
    name: str
    icon: ctype.int8
    acronym: str = ""
    description: str = ""
    entries: list[MacroEntry] = Field(default_factory=list)
