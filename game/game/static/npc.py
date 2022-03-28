import typing
from dataclasses import dataclass, field

from game.models.structures.character.stats import BaseStats, Stats
from game.models.structures.object.point3d import Point3D
from game.static.static import StaticData


@dataclass
class NpcStatic(StaticData):
    id: cython.long
    name: UTFString
    title: UTFString
    cls: UTFString
    collision_radius: cython.long
    collision_height: cython.long
    level: cython.long
    sex: cython.long
    type: UTFString
    attackrange: cython.long
    hp: cython.long
    mp: cython.long
    hp_regeneration: cython.float
    mp_regeneration: cython.float
    str: cython.long
    con: cython.long
    dex: cython.long
    int: cython.long
    wit: cython.long
    men: cython.long
    exp: cython.long
    sp: cython.long
    patk: cython.long
    pdef: cython.long
    matk: cython.long
    mdef: cython.long
    atkspd: cython.long
    aggro: cython.bint
    matkspd: cython.long
    rhand: cython.long
    lhand: cython.long
    armor: cython.long
    walkspd: cython.long
    runspd: cython.long
    faction_id: typing.Optional[cython.long]
    faction_range: cython.long
    absorb_level: cython.long
    absorb_type: UTFString
    id_template: cython.long
    server_side_name: cython.long
    server_side_title: cython.long
    is_undead: cython.bint

    __filepath__ = "static/sql/npc.json"
