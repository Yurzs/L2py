from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass


@dataclass
class EquippedItems(BaseDataclass):
    under: common.datatypes.Int32 = field(default=0)
    left_ear: common.datatypes.Int32 = field(default=0)
    right_ear: common.datatypes.Int32 = field(default=0)
    necklace: common.datatypes.Int32 = field(default=0)
    right_finger: common.datatypes.Int32 = field(default=0)
    left_finger: common.datatypes.Int32 = field(default=0)
    head: common.datatypes.Int32 = field(default=0)
    right_hand: common.datatypes.Int32 = field(default=0)
    left_hand: common.datatypes.Int32 = field(default=0)
    gloves: common.datatypes.Int32 = field(default=0)
    chest: common.datatypes.Int32 = field(default=0)
    legs: common.datatypes.Int32 = field(default=0)
    feet: common.datatypes.Int32 = field(default=0)
    back: common.datatypes.Int32 = field(default=0)
    double_handed: common.datatypes.Int32 = field(default=0)
    hair: common.datatypes.Int32 = field(default=0)
