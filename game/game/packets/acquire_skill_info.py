import typing
from dataclasses import dataclass, field

from .base import GameServerPacket


@dataclass
class Requirement:
    item_id: Int32
    count: Int32
    type: Int32
    unk: Int32


@dataclass
class AcquireSkillInfo(GameServerPacket):
    type: Int8 = field(default=193, init=False, repr=False)
    requirements: typing.List[Requirement]
    id: Int32
    level: Int32
    sp_cost: Int32
    mode: Int32

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.id,
            self.level,
            self.sp_cost,
            self.mode,
            Int32(len(self.requirements)),
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
