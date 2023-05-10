from typing import ClassVar

from common.document import Document
from game.models.structures.item.item import Item, ItemLocation


class DroppedItem(Document, Item):
    __collection__: ClassVar[str] = "dropped_items"
    __database__: ClassVar[str] = "l2py"

    def validate_position(self):
        pass
