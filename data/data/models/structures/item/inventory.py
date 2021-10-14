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

    under: common.datatypes.Int32 = 0
    left_ear: common.datatypes.Int32 = 0
    right_ear: common.datatypes.Int32 = 0
    neck: common.datatypes.Int32 = 0
    left_finger: common.datatypes.Int32 = 0
    right_finger: common.datatypes.Int32 = 0
    head: common.datatypes.Int32 = 0
    right_hand: common.datatypes.Int32 = 0
    left_hand: common.datatypes.Int32 = 0
    gloves: common.datatypes.Int32 = 0
    chest: common.datatypes.Int32 = 0
    legs: common.datatypes.Int32 = 0
    feet: common.datatypes.Int32 = 0
    back: common.datatypes.Int32 = 0
    face: common.datatypes.Int32 = 0
    hair: common.datatypes.Int32 = 0
    hair_all: common.datatypes.Int32 = 0


@dataclass
class Inventory(BaseDataclass):
    equipped_items: PaperDoll = PaperDoll()
    items: typing.List[Item] = field(default_factory=list)
