from typing import TYPE_CHECKING, ClassVar

from common.ctype import ctype
from common.misc import extend_bytearray

from .base import GameServerPacket

if TYPE_CHECKING:
    from game.models.character import Character
    from game.session import GameSession


class UserInfo(GameServerPacket):
    type: ctype.int8 = 4
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
                self.character.stats.level,
                self.character.stats.exp,
                self.character.stats.base.STR,
                self.character.stats.base.DEX,
                self.character.stats.base.CON,
                self.character.stats.base.INT,
                self.character.stats.base.WIT,
                self.character.stats.base.MEN,
                self.character.stats.max_hp,
                self.character.status.hp,
                self.character.stats.max_mp,
                self.character.status.mp,
                self.character.stats.sp,
                self.character.status.weight_load,
                self.character.template.load,
                *self.character.inventory.encode(),
                *[ctype.int32(0) for _ in range(18)],
                # # right hand augment
                # self.character.inventory.equipped_items.right_hand.augmentation
                # if self.character.inventory.equipped_items.right_hand is not None
                # else ctype.int32(0),
                # *[ctype.int32(0) for _ in range(12)],
                # # left hand augment
                # self.character.inventory.equipped_items.left_hand.augmentation
                # if self.character.inventory.equipped_items.left_hand is not None
                # else ctype.int32(0),
                # *[ctype.int32(0) for _ in range(6)],
                self.character.stats.physical_attack,
                self.character.stats.physical_attack_speed,
                self.character.stats.physical_defense,
                self.character.stats.evasion,
                self.character.stats.accuracy,
                self.character.stats.critical_damage,
                self.character.stats.magic_attack,
                self.character.stats.magic_attack_speed,
                self.character.stats.physical_attack_speed,
                self.character.stats.magic_defense,
                ctype.int32(self.character.status.is_pvp),
                self.character.karma,
                self.character.stats.run_speed,
                self.character.stats.walk_speed,
                self.character.stats.swim_run_speed,
                self.character.stats.swim_walk_speed,
                self.character.stats.ride_run_speed,
                self.character.stats.ride_walk_speed,
                self.character.stats.fly_run_speed,
                self.character.stats.fly_walk_speed,
                self.character.stats.move_multiplier,
                self.character.stats.attack_speed_multiplier,
                self.character.template.collision_radius,
                self.character.template.collision_height,
                self.character.appearance.hair_style,
                self.character.appearance.hair_color,
                self.character.appearance.face_id,
                ctype.int32(0),  # TODO Access level
                self.character.title if self.character.is_visible else str("Invisible"),
                ctype.int32(0),  # TODO clan id
                ctype.int32(0),  # TODO clan crest id
                ctype.int32(0),  # TODO ally id
                ctype.int32(0),  # TODO ally crest id
                ctype.int32(0),  # TODO clan leader
                self.character.status.is_mounted,
                self.character.status.is_private_store,
                self.character.status.is_dwarf_craft_store,
                self.character.pk_kills,
                self.character.pvp_kills,
                ctype.int16(0),  # TODO cubics
                ctype.bool(0),  # 1 - to find party members
                ctype.int32(0),  # TODO abnormal effect
                ctype.int8(0),
                ctype.int32(0),  # TODO clan privileges
                self.character.stats.recommends_left,
                self.character.stats.recommends_received,
                ctype.int32(0),
                self.character.inventory_max,
                self.character.base_class,
                ctype.int32(0),
                self.character.stats.max_cp,
                self.character.status.cp,
                self.character.status.is_mounted,
                # TODO circles
                ctype.int8(0),
                ctype.int32(0),  # TODO clan large crest id
                self.character.status.is_noble,
                self.character.status.is_hero,
                self.character.status.is_fishing,
                ctype.int32(0),  # TODO fish x
                ctype.int32(0),  # TODO fish y
                ctype.int32(0),  # TODO fish z
                self.character.name_color,  # TODO name color
                self.character.status.is_running,  # TODO is running
                ctype.int32(0),  # TODO pledge class
                ctype.int32(0),
                self.character.title_color,
                # TODO cursed weapons
                ctype.int32(0),
                ctype.int32(0),
            ],
        )
        return encoded
