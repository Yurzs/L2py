import typing
from dataclasses import dataclass, field

from common.helpers.bytearray import ByteArray
from game.models.character import Character

from .base import GameServerPacket


@dataclass
class CharList(GameServerPacket):
    type: cython.char = field(default=19, init=False, repr=False)
    characters: typing.List[Character] = ()

    def encode(self, session):
        account = session.account

        encoded = self.type.encode()

        encoded.append(cython.long(len(self.characters)))

        for character in self.characters:
            encoded.extend(
                [
                    character.name,
                    character.id,
                    account.username,
                    session.id,
                    cython.long(0),  # TODO: clan_id,
                    cython.long(0),
                    character.sex,
                    character.race,
                    character.active_class,
                    character.active,
                    character.position.point3d.x,
                    character.position.point3d.y,
                    character.position.point3d.z,
                    cython.double(character.status.hp.value),
                    cython.double(character.status.mp.value),
                    character.stats.sp,
                    character.stats.exp,
                    character.stats.level,
                    character.karma,
                    character.pk_kills,
                    character.pvp_kills,
                    *[cython.long(0) for _ in range(7)],
                    *character.inventory.encode(),
                    character.hair_style,
                    character.hair_color,
                    character.face,
                    cython.double(character.stats.max_hp.value),
                    cython.double(character.stats.max_mp.value),
                    character.time_until_deletion,
                    character.active_class,
                    cython.long(account.last_character == character.name),
                    cython.char(0),
                    character.face,
                ]
            )
        return encoded
