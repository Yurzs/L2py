import typing
from dataclasses import dataclass, field

from .base import GameServerPacket


@dataclass
class Requirement:
    item_id: cython.long
    count: cython.long
    type: cython.long
    unk: cython.long


@dataclass
class AcquireSkillInfo(GameServerPacket):
    type: cython.char = field(default=193, init=False, repr=False)
    requirements: typing.List[Requirement]
    id: cython.long
    level: cython.long
    sp_cost: cython.long
    mode: cython.long

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.id,
            self.level,
            self.sp_cost,
            self.mode,
            cython.long(len(self.requirements)),
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
