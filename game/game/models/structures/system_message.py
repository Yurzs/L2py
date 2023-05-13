from typing import ClassVar

from pydantic import Field

from common.ctype import ctype
from common.model import BaseModel


class MessageValue(BaseModel):
    type: ClassVar[ctype.int32]
    value: tuple


class Text(MessageValue):
    type: ClassVar[ctype.int32] = 0
    text: str

    @property
    def value(self) -> tuple:
        return (self.text,)


class Number(MessageValue):
    type: ClassVar[ctype.int32] = 1
    number: ctype.int32

    @property
    def value(self) -> tuple:
        return (self.number,)


class NpcName(MessageValue):
    type: ClassVar[ctype.int32] = 2
    npc_id: ctype.int32

    @property
    def value(self) -> tuple:
        return (self.npc_id + 1000000,)


class ItemName(MessageValue):
    type: ClassVar[ctype.int32] = 3
    item_id: ctype.int32

    @property
    def value(self) -> tuple:
        return (self.item_id,)


class SkillName(MessageValue):
    type: ClassVar[ctype.int32] = 4
    skill_id: ctype.int32
    skill_lvl: ctype.int32

    @property
    def value(self) -> tuple:
        return self.skill_id, self.skill_lvl


class ZoneName(MessageValue):
    type: ClassVar[ctype.int32] = 7
    x: ctype.int32
    y: ctype.int32
    z: ctype.int32

    @property
    def value(self) -> tuple:
        return self.x, self.y, self.z


class SystemMessage(BaseModel):
    type: ctype.int32
    data: tuple[MessageValue, ...] = Field(default_factory=tuple)
