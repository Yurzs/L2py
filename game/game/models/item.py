from dataclasses import dataclass, field

from common.document import Document
from game.models.structures.item.item import Item, ItemLocation


@dataclass(kw_only=True)
class DroppedItem(Document, Item):
    __collection__: str = field(default="dropped_items", repr=False, init=False)
    __database__: str = field(default="l2py", repr=False, init=False)

    def validate_position(self):
        pass
