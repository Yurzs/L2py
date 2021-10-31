import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.item.item import Item


@dataclass
class PaperDoll(BaseDataclass):
    under_id = Int32(0)
    left_ear_id = Int32(1)
    right_ear_id = Int32(2)
    neck_id = Int32(3)
    left_finger_id = Int32(4)
    right_finger_id = Int32(5)
    head_id = Int32(6)
    right_hand_id = Int32(7)
    left_hand_id = Int32(8)
    gloves_id = Int32(9)
    chest_id = Int32(10)
    legs_id = Int32(11)
    feet_id = Int32(12)
    back_id = Int32(13)
    double_handed_id = Int32(14)
    face_id = Int32(15)
    hair_id = Int32(16)
    double_hair_id = Int32(17)
    total_slots_count = Int32(17)

    all_items_ids = [
        under_id,
        left_ear_id,
        right_ear_id,
        neck_id,
        left_finger_id,
        right_finger_id,
        head_id,
        right_hand_id,
        left_hand_id,
        gloves_id,
        chest_id,
        legs_id,
        feet_id,
        back_id,
        double_handed_id,
        face_id,
        hair_id,
        double_hair_id,
    ]

    under: Item = None
    left_ear: Item = None
    right_ear: Item = None
    neck: Item = None
    left_finger: Item = None
    right_finger: Item = None
    head: Item = None
    right_hand: Item = None
    left_hand: Item = None
    gloves: Item = None
    chest: Item = None
    legs: Item = None
    feet: Item = None
    back: Item = None
    face: Item = None
    hair: Item = None
    hair_all: Item = None
    double_handed: Item = None

    def by_id(self, item_slot_id: Int32):
        """Finds item by its slot ID."""

        return {
            self.under_id: self.under,
            self.left_ear_id: self.left_ear,
            self.right_ear_id: self.right_ear,
            self.neck_id: self.neck,
            self.left_finger_id: self.left_finger,
            self.right_finger_id: self.right_finger,
            self.head_id: self.head,
            self.right_hand_id: self.right_hand,
            self.left_hand_id: self.left_hand,
            self.gloves_id: self.gloves,
            self.chest_id: self.chest,
            self.legs_id: self.legs,
            self.feet_id: self.feet,
            self.back_id: self.back,
            self.face_id: self.face,
            self.hair_id: self.hair,
            self.double_hair_id: self.hair_all,
            self.double_handed_id: self.double_handed,
        }[item_slot_id]

    def set_item(self, slot_id, item):
        if hasattr(self, slot_id):
            setattr(self, slot_id, item)

    def by_body_part_name(self, body_part_name):
        return {
            self.under_id: self.under,
            self.left_ear_id: self.left_ear,
            self.right_ear_id: self.right_ear,
            self.neck_id: self.neck,
            self.left_finger_id: self.left_finger,
            self.right_finger_id: self.right_finger,
            self.head_id: self.head,
            self.right_hand_id: self.right_hand,
            self.left_hand_id: self.left_hand,
            self.gloves_id: self.gloves,
            self.chest_id: self.chest,
            self.legs_id: self.legs,
            self.feet_id: self.feet,
            self.back_id: self.back,
            self.face_id: self.face,
            self.hair_id: self.hair,
            self.double_hair_id: self.hair_all,
            self.double_handed_id: self.double_handed,
        }[body_part_name]


@dataclass
class Inventory(BaseDataclass):
    equipped_items: PaperDoll = PaperDoll()
    items: typing.List[Item] = field(default_factory=list)

    @property
    def total_weight(self):
        weight = 0
        for item in [*self.equipped_items, *self.items]:
            weight += item.weight
        return weight

    def encode(self):
        object_ids = []
        type_ids = []
        for item_id in self.equipped_items.all_items_ids:
            if item_id == PaperDoll.double_handed_id:
                continue
            item = self.equipped_items.by_id(item_id)
            if item is not None:
                object_ids.append(item.id)
                type_ids.append(item.special_type)
            else:
                object_ids.append(Int32(0))
                type_ids.append(Int32(0))
        return [*object_ids, *type_ids]

    def equip(self, item, slot_id=None):
        """Equips item."""

        if slot_id is not None:
            current_item = self.equipped_items.by_id(slot_id)
            self.items.append(current_item)
            self.equipped_items.set_item(slot_id, item)
            self.items.pop(item)
            item.is_equipped = True

    def encode_other(self):
        """Encodes inventory as other character."""

        result = []
        required_items = [
            self.equipped_items.hair_all,
            self.equipped_items.head,
            self.equipped_items.right_hand,
            self.equipped_items.left_hand,
            self.equipped_items.gloves,
            self.equipped_items.chest,
            self.equipped_items.legs,
            self.equipped_items.feet,
            self.equipped_items.back,
            self.equipped_items.double_handed,
            self.equipped_items.hair,
            self.equipped_items.face,
        ]
        for item in required_items:
            if item is not None:
                result.append(item.id)
            else:
                result.append(Int32(0))
        return result
