from dataclasses import dataclass, field

import game.constants
from common.ctype import ctype
from game.static.item import Item, ItemProperties
from game.static.static import StaticData


@dataclass(kw_only=True)
class EtcItem(Item, StaticData):

    __filepath__ = "data/etcitem.json"

    @property
    def is_arrow(self):
        return
