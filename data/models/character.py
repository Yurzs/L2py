from dataclasses import dataclass, field
from common.document import Document
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


@dataclass
class Character(Document):
    __collection__: str = field(default="characters", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)

    _id: common.datatypes.Int32
    account_id: common.datatypes.String
    nickname: common.datatypes.String
    clan_id: common.datatypes.Int32
    sex: common.datatypes.Int32
    race: common.datatypes.Int32
    class_id: common.datatypes.Int32
    active: common.datatypes.Int32
    current_hp: common.datatypes.Int32
    max_hp: common.datatypes.Int64
    current_mp: common.datatypes.Int32
    max_mp: common.datatypes.Int64
    current_cp: common.datatypes.Int32
    max_cp: common.datatypes.Int64
    sp: common.datatypes.Int32 = field(default=0)
    exp: common.datatypes.Int64 = field(default=0)
    level: common.datatypes.Int32 = field(default=1)
    karma: common.datatypes.Int32 = field(default=0)
    equipped_items: EquippedItems = field(default=EquippedItems())
    equipped_items_objects: EquippedItems = field(default=EquippedItems())
    face_id: common.datatypes.Int32 = field(default=EquippedItems())
    is_deleted: common.datatypes.Int32 = field(default=False)
    base_class_id: common.datatypes.Int32 = field(default=1)
