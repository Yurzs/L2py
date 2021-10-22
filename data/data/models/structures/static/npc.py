import typing
from dataclasses import dataclass, field

from common.helpers.bytearray import ByteArray
from data.models.structures.character.stats import BaseStats, Stats
from data.models.structures.character.template import CharacterTemplate, LevelUpGain
from data.models.structures.object.point3d import Point3D
from data.models.structures.static.static import StaticData


@dataclass
class NpcStatic(StaticData):
    id: Int32
    name: UTFString
    title: UTFString
    cls: UTFString
    collision_radius: Int32
    collision_height: Int32
    level: Int32
    sex: Int32
    type: UTFString
    attackrange: Int32
    hp: Int32
    mp: Int32
    hp_regeneration: Float
    mp_regeneration: Float
    str: Int32
    con: Int32
    dex: Int32
    int: Int32
    wit: Int32
    men: Int32
    exp: Int32
    sp: Int32
    patk: Int32
    pdef: Int32
    matk: Int32
    mdef: Int32
    atkspd: Int32
    aggro: Bool
    matkspd: Int32
    rhand: Int32
    lhand: Int32
    armor: Int32
    walkspd: Int32
    runspd: Int32
    faction_id: typing.Optional[Int32]
    faction_range: Int32
    absorb_level: Int32
    absorb_type: UTFString
    id_template: Int32
    server_side_name: Int32
    server_side_title: Int32
    is_undead: Bool

    __filepath__ = "static/sql/npc.json"
