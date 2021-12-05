import typing
from dataclasses import dataclass, field

from game.models.character import Character

if typing.TYPE_CHECKING:
    from game.session import GameSession

from .base import GameServerPacket


@dataclass
class UserInfo(GameServerPacket):
    type: Int8 = field(default=4, init=False, repr=False)
    character: Character

    def encode(self, session: "GameSession"):
        encoded = self.type.encode()

        encoded.extend(
            [
                self.character.position.point3d.x,
                self.character.position.point3d.y,
                self.character.position.point3d.z,
                self.character.position.heading_angle,
                self.character.id,
                self.character.name,
                self.character.race,
                self.character.sex,
                self.character.active_class,
                self.character.stats.level,
                self.character.stats.exp,
                self.character.stats.base.str,
                self.character.stats.base.dex,
                self.character.stats.base.con,
                self.character.stats.base.int,
                self.character.stats.base.wit,
                self.character.stats.base.men,
                self.character.stats.max_hp,
                self.character.status.hp,
                self.character.stats.max_mp,
                self.character.status.mp,
                self.character.stats.sp,
                self.character.status.weight_load,
                self.character.template.load,
                *self.character.inventory.encode(),
                *[Int16(0) for _ in range(14)],
                # right hand augment
                self.character.inventory.equipped_items.right_hand.augmentation
                if self.character.inventory.equipped_items.right_hand is not None
                else Int32(0),
                *[Int16(0) for _ in range(12)],
                # left hand augment
                self.character.inventory.equipped_items.left_hand.augmentation
                if self.character.inventory.equipped_items.left_hand is not None
                else Int32(0),
                *[Int16(0) for _ in range(6)],
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
                Int32(self.character.status.is_pvp),
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
                self.character.hair_style,
                self.character.hair_color,
                self.character.face,
                Int32(0),  # TODO Access level
                self.character.title if self.character.is_visible else UTFString("Invisible"),
                Int32(0),  # TODO clan id
                Int32(0),  # TODO clan crest id
                Int32(0),  # TODO ally id
                Int32(0),  # TODO ally crest id
                Int32(0),  # TODO clan leader
                self.character.status.is_mounted,
                self.character.status.is_private_store,
                self.character.status.is_dwarf_craft_store,
                self.character.pk_kills,
                self.character.pvp_kills,
                Int16(0),  # TODO cubics
                Bool(0),  # 1 - to find party members
                Int32(0),  # TODO abnormal effect
                Int8(0),
                Int32(0),  # TODO clan privileges
                Int16(self.character.stats.recommends_left),
                Int16(self.character.stats.recommends_received),
                Int32(0),
                Int16(self.character.inventory_max),
                self.character.base_class,
                Int32(0),
                self.character.stats.max_cp,
                self.character.status.cp,
                self.character.status.is_mounted,
                # TODO circles
                Int8(0),
                Int32(0),  # TODO clan large crest id
                self.character.status.is_noble,
                self.character.status.is_hero,
                self.character.status.is_fishing,
                Int32(0),  # TODO fish x
                Int32(0),  # TODO fish y
                Int32(0),  # TODO fish z
                self.character.name_color,  # TODO name color
                self.character.status.is_running,  # TODO is running
                Int32(0),  # TODO pledge class
                Int32(0),
                self.character.title_color,
                # TODO cursed weapons
                Int32(0),
                Int32(0),
            ]
        )
        return encoded
