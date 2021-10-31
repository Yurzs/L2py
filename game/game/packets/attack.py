import typing
from dataclasses import dataclass, field

import game.models.structures.object.position
from common.dataclass import BaseDataclass

from .base import GameServerPacket


@dataclass
class Hit(BaseDataclass):
    target_id: Int32
    damage: Int32
    flags: Int8 = 0


@dataclass
class Attack(GameServerPacket):
    type: Int8 = field(default=5, init=False, repr=False)
    attacker_id: Int32
    soulshot: Bool
    grade: Int32
    position: game.models.structures.object.position.Position
    hit: Hit
    hits: typing.List[Hit] = field(default_factory=list, init=False)
    Hit = Hit

    def __post_init__(self):
        super().__post_init__()
        self.hits.append(self.hit)

    def add_hit(
        self,
        target_id: Int32,
        damage: Int32,
        have_missed: bool,
        is_critical: bool,
        is_shielded: bool,
    ):

        hit = Hit(target_id, damage)

        if self.soulshot:
            hit.flags |= 0x10 | self.grade
        if is_critical:
            hit.flags |= 0x20
        if is_shielded:
            hit.flags |= 0x40
        if have_missed:
            hit.flags |= 0x80

        self.hits.append(hit)

    def encode(self, session):
        encoded = self.type.encode()

        ordered_data = [
            self.attacker_id,
            self.hits[0].target_id,
            self.hits[0].damage,
            self.hits[0].flags,
            self.position.point3d.x,
            self.position.point3d.y,
            self.position.point3d.z,
            Int16(len(self.hits) - 1),
        ]
        for hit in self.hits:
            ordered_data += [
                hit.target_id,
                hit.damage,
                Int32(hit.flags),
            ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
