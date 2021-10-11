import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from data.models.structures.item.item import Item


@dataclass
class PaperDoll(BaseDataclass):
    under_id = common.datatypes.Int32(0)
    left_ear_id = common.datatypes.Int32(1)
    right_ear_id = common.datatypes.Int32(2)
    neck_id = common.datatypes.Int32(3)
    left_finger_id = common.datatypes.Int32(4)
    right_finger_id = common.datatypes.Int32(5)
    head_id = common.datatypes.Int32(6)
    right_hand_id = common.datatypes.Int32(7)
    left_hand_id = common.datatypes.Int32(8)
    gloves_id = common.datatypes.Int32(9)
    chest_id = common.datatypes.Int32(10)
    legs_id = common.datatypes.Int32(11)
    feet_id = common.datatypes.Int32(12)
    back_id = common.datatypes.Int32(13)
    face_id = common.datatypes.Int32(14)
    hair_id = common.datatypes.Int32(15)
    hair_all_id = common.datatypes.Int32(16)
    total_slots_count = common.datatypes.Int32(17)

    under: Item
    left_ear: Item
    right_ear: Item
    neck: Item
    left_finger: Item
    right_finger: Item
    head: Item
    right_hand: Item
    left_hand: Item
    gloves: Item
    chest: Item
    legs: Item
    feet: Item
    back: Item
    face: Item
    hair: Item
    hair_all: Item


@dataclass
class Inventory(BaseDataclass):
    equipped_items: PaperDoll
    items: typing.List[None]
