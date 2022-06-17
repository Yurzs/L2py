import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.object.position import Position

from .base import GameServerPacket


@dataclass(kw_only=True)
class Hit(BaseDataclass):
    target_id: ctype.int32
    damage: ctype.int32
    flags: ctype.int8 = 0


@dataclass(kw_only=True)
class Attack(GameServerPacket):
    type: ctype.int8 = field(default=5, init=False, repr=False)
    attacker_id: ctype.int32
    soulshot: ctype.bool
    grade: ctype.int32
    position: Position
    hit: Hit
    hits: typing.List[Hit] = field(default_factory=list, init=False)
    Hit = Hit

    def __post_init__(self):
        super().__post_init__()
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
