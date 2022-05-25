import dataclasses
from dataclasses import field

from common.ctype import ctype
from common.dataclass import BaseDataclass


@dataclasses.dataclass(kw_only=True)
class EquippedItems(BaseDataclass):
    under: ctype.int32 = field(default=0)
    left_ear: ctype.int32 = field(default=0)
    right_ear: ctype.int32 = field(default=0)
    necklace: ctype.int32 = field(default=0)
    right_finger: ctype.int32 = field(default=0)
    left_finger: ctype.int32 = field(default=0)
    head: ctype.int32 = field(default=0)
    right_hand: ctype.int32 = field(default=0)
    left_hand: ctype.int32 = field(default=0)
    gloves: ctype.int32 = field(default=0)
    chest: ctype.int32 = field(default=0)
    legs: ctype.int32 = field(default=0)
    feet: ctype.int32 = field(default=0)
    back: ctype.int32 = field(default=0)
    double_handed: ctype.int32 = field(default=0)
    hair: ctype.int32 = field(default=0)
