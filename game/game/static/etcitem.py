from typing import ClassVar

from game.static.item import Item
from game.static.static import StaticData


class EtcItem(Item, StaticData):
    filepath: ClassVar[str] = "game/data/etcitem.json"

    @property
    def is_arrow(self):
        return
