from typing import ClassVar

from pydantic import Field

from common.ctype import ctype
from common.model import BaseModel
from game.models.structures.object.position import Position

from .base import GameServerPacket


class Hit(BaseModel):
    target_id: ctype.int32
    damage: ctype.int32
    flags: ctype.int8 = 0


class Attack(GameServerPacket):
    type: ctype.int8 = 5
    attacker_id: ctype.int32
    soulshot: ctype.bool
    grade: ctype.int32
    position: Position
    hit: Hit
    Hit = Hit

    hits: list[Hit] = Field(default_factory=list)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hits.append(self.hit)

    def add_hit(
        self,
        target_id: ctype.int32,
        damage: ctype.int32,
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
            ctype.int(len(self.hits) - 1),
        ]
        for hit in self.hits:
            ordered_data += [
                hit.target_id,
                hit.damage,
                ctype.int32(hit.flags),
            ]
        for item in ordered_data:
            encoded.append(item)
        return encoded
