from dataclasses import dataclass, field

from common.document import Document
from game.models.structures.item.item import Item, ItemLocation


@dataclass
class DroppedItem(Document, Item):
    __collection__: String = field(default="dropped_items", repr=False, init=False)
    __database__: String = field(default="l2py", repr=False, init=False)

    def validate_position(self):
        print(self.location in ItemLocation.__dict__)
