from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class EquippedItems(BaseDataclass):
    under: Int32 = field(default=0)
    left_ear: Int32 = field(default=0)
    right_ear: Int32 = field(default=0)
    necklace: Int32 = field(default=0)
    right_finger: Int32 = field(default=0)
    left_finger: Int32 = field(default=0)
    head: Int32 = field(default=0)
    right_hand: Int32 = field(default=0)
    left_hand: Int32 = field(default=0)
    gloves: Int32 = field(default=0)
    chest: Int32 = field(default=0)
    legs: Int32 = field(default=0)
    feet: Int32 = field(default=0)
    back: Int32 = field(default=0)
    double_handed: Int32 = field(default=0)
    hair: Int32 = field(default=0)
