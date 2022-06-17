import typing
from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.game.game.models.structures.character.stats import BaseStats, Stats
from src.game.game.models.structures.object.point3d import Point3D
from src.game.game.static.static import StaticData


@dataclass(kw_only=True)
class NpcStatic(StaticData):
    id: ctype.int32
    name: str
    title: str
    cls: str
    collision_radius: ctype.int32
    collision_height: ctype.int32
    level: ctype.int32
    sex: ctype.int32
    type: str
    attackrange: ctype.int32
    hp: ctype.int32
    mp: ctype.int32
    hp_regeneration: ctype.float
    mp_regeneration: ctype.float
    STR: ctype.int32
    CON: ctype.int32
    DEX: ctype.int32
    INT: ctype.int32
    WIT: ctype.int32
    MEN: ctype.int32
    exp: ctype.int32
    sp: ctype.int32
    patk: ctype.int32
    pdef: ctype.int32
    matk: ctype.int32
    mdef: ctype.int32
    atkspd: ctype.int32
    aggro: ctype.bool
    matkspd: ctype.int32
    rhand: ctype.int32
    lhand: ctype.int32
    armor: ctype.int32
    walkspd: ctype.int32
    runspd: ctype.int32
    faction_id: typing.Optional[ctype.int32]
    faction_range: ctype.int32
    absorb_level: ctype.int32
    absorb_type: str
    id_template: ctype.int32
    server_side_name: ctype.int32
    server_side_title: ctype.int32
    is_undead: ctype.bool

    __filepath__ = "static/sql/npc.json"
