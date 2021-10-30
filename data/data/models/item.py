from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.document import Document, DocumentDefaults
from data.models.structures.item.item import Item as ItemStructure
from data.models.structures.item.item import ItemLocation
from data.models.structures.object.object import L2Object, L2ObjectBases, L2ObjectDefaults


@dataclass
class ItemDefaults(L2ObjectDefaults, DocumentDefaults):
    decrease: Bool = False
    augmentation: Int32 = None
    mana: Int32 = -1
    consuming_mana: Bool = False
    mana_consumption_rate = 60000

    charged_soulshot: Int32 = 0
    charged_spiritshot: Int32 = 0
    charged_fishshot: Bool = False

    last_change: Int32 = 2


@dataclass
class ItemBases(L2ObjectBases):
    owner_id: Int32
    count: Int32
    initial_count: Int32
    usage_time: Int32
    item: ItemStructure
    location: Int32
    slot: Int32
    enchant: Int32
    price_sell: Int32
    price_buy: Int32
    wear: Bool
    drop_time: Int32
    protected: Bool


@dataclass
class Item(BaseDataclass, ItemDefaults, ItemBases):
    pass


@dataclass
class DroppedItem(Document, Item):
    __collection__: String = field(default="dropped_items", repr=False, init=False)
    __database__: String = field(default="l2py", repr=False, init=False)

    @Item.post_init_hook
    def check_position(self):
        print(self.location in ItemLocation.__dict__)
