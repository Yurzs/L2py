import dataclasses
import typing
from dataclasses import field

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.item.armor import Armor
from src.game.game.models.structures.item.item import Item
from src.game.game.models.structures.item.weapon import Weapon


@dataclasses.dataclass(kw_only=True)
class PaperDoll(BaseDataclass):
    class IDs:
        under_id = ctype.int32(0)
        left_ear_id = ctype.int32(1)
        right_ear_id = ctype.int32(2)
        neck_id = ctype.int32(3)
        left_finger_id = ctype.int32(4)
        right_finger_id = ctype.int32(5)
        head_id = ctype.int32(6)
        right_hand_id = ctype.int32(7)
        left_hand_id = ctype.int32(8)
        gloves_id = ctype.int32(9)
        chest_id = ctype.int32(10)
        legs_id = ctype.int32(11)
        feet_id = ctype.int32(12)
        back_id = ctype.int32(13)
        double_handed_id = ctype.int32(14)
        face_id = ctype.int32(15)
        hair_id = ctype.int32(16)
        double_hair_id = ctype.int32(17)
        total_slots_count = ctype.int32(17)

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

    under: typing.Optional[Armor] = None
    left_ear: typing.Optional[Armor] = None
    right_ear: typing.Optional[Armor] = None
    neck: typing.Optional[Armor] = None
    left_finger: typing.Optional[Armor] = None
    right_finger: typing.Optional[Armor] = None
    head: typing.Optional[Armor] = None
    right_hand: typing.Optional[Weapon] = None
    left_hand: typing.Optional[Weapon] = None
    gloves: typing.Optional[Armor] = None
    chest: typing.Optional[Armor] = None
    legs: typing.Optional[Armor] = None
    feet: typing.Optional[Armor] = None
    back: typing.Optional[Armor] = None
    face: typing.Optional[Armor] = None
    hair: typing.Optional[Armor] = None
    hair_all: typing.Optional[Armor] = None
    double_handed: typing.Optional[Weapon] = None

    def by_id(self, item_slot_id: ctype.int32):
        """Finds item by its slot ID."""

        return {
            self.IDs.under_id: self.under,
            self.IDs.left_ear_id: self.left_ear,
            self.IDs.right_ear_id: self.right_ear,
            self.IDs.neck_id: self.neck,
            self.IDs.left_finger_id: self.left_finger,
            self.IDs.right_finger_id: self.right_finger,
            self.IDs.head_id: self.head,
            self.IDs.right_hand_id: self.right_hand,
            self.IDs.left_hand_id: self.left_hand,
            self.IDs.gloves_id: self.gloves,
            self.IDs.chest_id: self.chest,
            self.IDs.legs_id: self.legs,
            self.IDs.feet_id: self.feet,
            self.IDs.back_id: self.back,
            self.IDs.face_id: self.face,
            self.IDs.hair_id: self.hair,
            self.IDs.double_hair_id: self.hair_all,
            self.IDs.double_handed_id: self.double_handed,
        }[item_slot_id]

    def set_item(self, slot_id, item):
        if hasattr(self, slot_id):
            setattr(self, slot_id, item)

    def by_body_part_name(self, body_part_name):
        return {
            self.IDs.under_id: self.under,
            self.IDs.left_ear_id: self.left_ear,
            self.IDs.right_ear_id: self.right_ear,
            self.IDs.neck_id: self.neck,
            self.IDs.left_finger_id: self.left_finger,
            self.IDs.right_finger_id: self.right_finger,
            self.IDs.head_id: self.head,
            self.IDs.right_hand_id: self.right_hand,
            self.IDs.left_hand_id: self.left_hand,
            self.IDs.gloves_id: self.gloves,
            self.IDs.chest_id: self.chest,
            self.IDs.legs_id: self.legs,
            self.IDs.feet_id: self.feet,
            self.IDs.back_id: self.back,
            self.IDs.face_id: self.face,
            self.IDs.hair_id: self.hair,
            self.IDs.double_hair_id: self.hair_all,
            self.IDs.double_handed_id: self.double_handed,
        }[body_part_name]


@dataclasses.dataclass(kw_only=True)
class Inventory(BaseDataclass):
    equipped_items: PaperDoll = field(default_factory=PaperDoll)
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
        for item_id in self.equipped_items.IDs.all_items_ids:
            if item_id == PaperDoll.IDs.double_handed_id:
                continue
            item = self.equipped_items.by_id(item_id)
            if item is not None:
                object_ids.append(item.id)
                type_ids.append(item.special_type)
            else:
                object_ids.append(ctype.int32(0))
                type_ids.append(ctype.int32(0))
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
                result.append(ctype.int32(0))
        return result
