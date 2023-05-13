from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray
from game.packets.base import GameServerPacket

if TYPE_CHECKING:
    from game.models.character import Character
    from game.session import GameSession


class CharInfo(GameServerPacket):
    type: ctype.int8 = 3
    character: "Character"

    def encode(self, session: "GameSession"):
        encoded = bytearray()

        extend_bytearray(
            encoded,
            [
                self.type,
                self.character.position.point3d.x,
                self.character.position.point3d.y,
                self.character.position.point3d.z,
                self.character.position.heading_angle,
                self.character.id,
                self.character.name,
                self.character.race,
                ctype.int32(self.character.appearance.sex),
                self.character.active_class,
                *self.character.inventory.encode_other(),
                *[ctype.int32(0) for _ in range(12)],
                # *[ctype.int32(0) for _ in range(4)],
                # # right hand augment
                # self.character.inventory.equipped_items.right_hand.augmentation
                # if self.character.inventory.equipped_items.right_hand is not None
                # else ctype.int32(0),
                # *[ctype.int(0) for _ in range(12)],
                # # left hand augment
                # self.character.inventory.equipped_items.left_hand.augmentation
                # if self.character.inventory.equipped_items.left_hand is not None
                # else ctype.int32(0),
                # *[ctype.int32(0) for _ in range(4)],
                ctype.int32(self.character.status.is_pvp),
                self.character.stats.karma,
                self.character.stats.magic_attack_speed,
                self.character.stats.physical_attack_speed,
                ctype.int32(self.character.status.is_pvp),
                self.character.stats.karma,
                self.character.stats.run_speed,
                self.character.stats.walk_speed,
                self.character.stats.run_speed,  # TODO SWIM SPEED
                self.character.stats.walk_speed,  # TODO SWIM SPEED
                self.character.stats.run_speed,  # TODO FL SPEED
                self.character.stats.walk_speed,  # TODO FL SPEED
                self.character.stats.run_speed,  # TODO FLY SPEED
                self.character.stats.walk_speed,  # TODO FLY SPEED
                self.character.stats.move_multiplier,
                self.character.stats.attack_speed_multiplier,
                self.character.template.collision_radius,
                self.character.template.collision_height,
                self.character.appearance.hair_style,
                self.character.appearance.hair_color,
                self.character.appearance.face_id,
                self.character.title if self.character.is_visible else "Invisible",
                ctype.int32(0),  # TODO clan id
                ctype.int32(0),  # TODO clan crest id
                ctype.int32(0),  # TODO ally id
                ctype.int32(0),  # TODO ally crest id
                ctype.int32(0),
                ctype.bool(not self.character.status.is_sitting),
                self.character.status.is_running,
                self.character.status.is_in_combat,
                self.character.status.is_faking_death,
                ctype.bool(not self.character.is_visible),
                self.character.status.is_mounted,
                self.character.status.is_private_store,
                ctype.int16(0),  # TODO cubics
                ctype.bool(0),  # 1 - to find party members
                ctype.int32(0),  # TODO abnormal effect
                ctype.int8(self.character.stats.recommends_left),
                self.character.stats.recommends_received,
                self.character.base_class,
                self.character.stats.max_cp,
                self.character.status.cp,
                self.character.status.is_mounted,
                # TODO circles
                ctype.int8(0),  # TODO Team id
                ctype.int32(0),  # TODO clan large crest id
                self.character.status.is_noble,
                self.character.status.is_hero,
                self.character.status.is_fishing,
                ctype.int32(0),  # TODO fish x
                ctype.int32(0),  # TODO fish y
                ctype.int32(0),  # TODO fish z
                self.character.name_color,
                ctype.int32(self.character.status.is_running),
                ctype.int32(0),  # TODO pledge class
                ctype.int32(0),  # TODO pledge colour
                self.character.title_color,
                # TODO cursed weapons
                ctype.int32(0),
            ],
        )

        return encoded
