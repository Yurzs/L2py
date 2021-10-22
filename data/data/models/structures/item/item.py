import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from data.models.structures.skill.skill import Skill


@dataclass
class ItemPropertiesBases:
    crystalizable: Bool
    stackable: Bool
    sellable: Bool
    droppable: Bool
    destroyable: Bool
    tradable: Bool


@dataclass
class ItemProperties(BaseDataclass, ItemPropertiesBases):
    pass


@dataclass
class Item(BaseDataclass):
    id: Int32
    name: UTFString
    inventory_type: Int32
    special_type: Int32
    type: Int32
    weight: Int32
    material: Int32
    crystal_type: Int32
    duration: Int32
    body_part: UTFString
    price: Int32
    crystal_count: Int32
    skills: typing.List[Skill]
    properties: ItemProperties
    avoid_modify: Bool
    object_id: Int32 = field(default_factory=Int32.random)
    augmentation: Int32 = field(default=0)


Item.update_forward_refs()
