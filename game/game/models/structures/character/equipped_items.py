from dataclasses import dataclass, field

from common.dataclass import BaseDataclass


@dataclass
class EquippedItems(BaseDataclass):
    under: cython.long = field(default=0)
    left_ear: cython.long = field(default=0)
    right_ear: cython.long = field(default=0)
    necklace: cython.long = field(default=0)
    right_finger: cython.long = field(default=0)
    left_finger: cython.long = field(default=0)
    head: cython.long = field(default=0)
    right_hand: cython.long = field(default=0)
    left_hand: cython.long = field(default=0)
    gloves: cython.long = field(default=0)
    chest: cython.long = field(default=0)
    legs: cython.long = field(default=0)
    feet: cython.long = field(default=0)
    back: cython.long = field(default=0)
    double_handed: cython.long = field(default=0)
    hair: cython.long = field(default=0)
