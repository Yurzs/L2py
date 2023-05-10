from typing import ClassVar

from common.ctype import ctype
from common.model import BaseModel

from .base import GameServerPacket


class Requirement(BaseModel):
    item_id: ctype.int32
    count: ctype.int32
    type: ctype.int32
    unk: ctype.int32


class AcquireSkillInfo(GameServerPacket):
    type: ctype.int8 = 193
    requirements: list[Requirement]
    id: ctype.int32
    level: ctype.int32
    sp_cost: ctype.int32
    mode: ctype.int32

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.id,
            self.level,
            self.sp_cost,
            self.mode,
            ctype.int32(len(self.requirements)),
        ]

        for requirement in self.requirements:
            ordered_data += [
                requirement.type,
                requirement.item_id,
                requirement.count,
                requirement.unk,
            ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
