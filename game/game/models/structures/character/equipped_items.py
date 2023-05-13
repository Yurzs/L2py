from common.ctype import ctype
from common.model import BaseModel


class EquippedItems(BaseModel):
    under: ctype.int32 = 0
    left_ear: ctype.int32 = 0
    right_ear: ctype.int32 = 0
    necklace: ctype.int32 = 0
    right_finger: ctype.int32 = 0
    left_finger: ctype.int32 = 0
    head: ctype.int32 = 0
    right_hand: ctype.int32 = 0
    left_hand: ctype.int32 = 0
    gloves: ctype.int32 = 0
    chest: ctype.int32 = 0
    legs: ctype.int32 = 0
    feet: ctype.int32 = 0
    back: ctype.int32 = 0
    double_handed: ctype.int32 = 0
    hair: ctype.int32 = 0
