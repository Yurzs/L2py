from dataclasses import dataclass, field

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclass(kw_only=True)
class MessageValue(BaseDataclass):
    type: ctype.int32
    value: tuple = field(init=False)


@dataclass(kw_only=True)
class Text(MessageValue):
    type: ctype.int32 = field(default=0, init=False)
    text: str

    @property
    def value(self) -> tuple:
        return (self.text,)


@dataclass(kw_only=True)
class Number(MessageValue):
    type: ctype.int32 = field(default=1, init=False)
    number: ctype.int32

    @property
    def value(self) -> tuple:
        return (self.number,)


@dataclass(kw_only=True)
class NpcName(MessageValue):
    type: ctype.int32 = field(default=2, init=False)
    npc_id: ctype.int32

    @property
    def value(self) -> tuple:
        return (self.npc_id + 1000000,)


@dataclass(kw_only=True)
class ItemName(MessageValue):
    type: ctype.int32 = field(default=3, init=False)
    item_id: ctype.int32

    @property
    def value(self) -> tuple:
        return (self.item_id,)


@dataclass(kw_only=True)
class SkillName(MessageValue):
    type: ctype.int32 = field(default=4, init=False)
    skill_id: ctype.int32
    skill_lvl: ctype.int32

    @property
    def value(self) -> tuple:
        return self.skill_id, self.skill_lvl


@dataclass(kw_only=True)
class ZoneName(MessageValue):
    type: ctype.int32 = field(default=7, init=False)
    x: ctype.int32
    y: ctype.int32
    z: ctype.int32

    @property
    def value(self) -> tuple:
        return self.x, self.y, self.z


@dataclass(kw_only=True)
class SystemMessage(BaseDataclass):
    type: ctype.int32
    data: tuple[MessageValue, ...] = field(default_factory=tuple)
