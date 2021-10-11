import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.skill.skill import Skill


@dataclass
class ItemStates(BaseDataclass):
    crystalizable: common.datatypes.Bool
    stackable: common.datatypes.Bool
    sellable: common.datatypes.Bool
    droppable: common.datatypes.Bool
    destroyable: common.datatypes.Bool
    tradable: common.datatypes.Bool


@dataclass
class Item(BaseDataclass):
    id: common.datatypes.Int32
    name: common.datatypes.UTFString
    inventory_type: common.datatypes.Int32
    special_type: common.datatypes.Int32
    type: common.datatypes.Int32
    weight: common.datatypes.Int32
    material_type: common.datatypes.Int32
    crystal_type: common.datatypes.Int32
    duration: common.datatypes.Int32
    body_part: common.datatypes.Int32
    reference_price: common.datatypes.Int32
    crystal_count: common.datatypes.Int32
    skills: typing.List[Skill]
