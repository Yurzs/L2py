from common.datatypes import Int8
from .base import GameServerPacket


class UserInfo(GameServerPacket):
    type = Int8(4)
    arg_order = [
        "type",
        "position_x", "position_y", "position_z",
        "head_tilt_angle", "character_id", "character_name",
        "race", "sex", "class_id", "level", "exp",
        "STR", "DEX", "CON", "INT", "WIT", "MEN",
        "max_hp", "current_hp", "max_mp", "current_mp",
        "sp", "inventory_weight", "max_inventory_weight",
        "unknown1",
        "underwear_id", "rear_id", "left_rear_id", "necklace_id",
        "right_ring_id", "left_ring_id", "helmet_id", "left_hand_id", "right_hand_id",
        "gloves_id", "main_armor_id", "leggings_id", "boots_id", "back_id",
        "left_right_hand_id", "hair_id", "face_id",
        "underwear_item_id", "rear_item_id", "left_rear_item_id", "necklace_item_id",
        "right_ring_item_id", "left_ring_item_id", "helmet_item_id", "left_hand_item_id",
        "right_hand_item_id",
        "gloves_item_id", "main_armor_item_id", "leggings_item_id", "boots_item_id",
        "back_item_id",
        "left_right_hand_item_id", "hair_item_id", "face_item_id",
        "unknown2",
        "patk", "patk_speed", "pdef", "evasion", "accuracy", "critical", "matk", "cast_speed",
        "attack_speed", "mdef", "is_in_pvp", "karma", "run_speed", "walk_speed",
        "run_swim_speed", "walk_swim_speed", "fl_run_speed", "fl_walk_speed",
        "run_fly_speed", "walk_fly_speed", "move_x", "atk_speed_x",
        "character_radius", "character_height",
        "haircut_type", "haircut_color", "face_type", "access_level",
        "title", "clan_id", "clan_icon_id", "alliance_id", "alliance_icon_id", "siege_flag",
        "is_riding", "private_store_type", "can_craft", "pvp_count", "pk_count",
        "cubes_summoned", "cubes", "find_party_members",
        "abnormal_effect",
        "unknown3",
        "clan_privileges", "recommends_left", "recommended",
        "unknown4",
        "max_inventory_items_count", "character_class_id", "effect_around_player",
        "max_cp", "current_cp", "enchant_state", "event_command_id",
        "big_clan_icon_id",
        "is_nobles", "is_hero",
        "is_fishing", "fish_x", "fish_y", "fish_z",
        "name_rgb", "walk_is_on",
        "clan_class",
        "unknown5",
        "title_rgb", "cursed_weapon_level"
    ]
