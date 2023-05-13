from .item import Item


class EtcItemType:
    ARROW = 0
    MATERIAL = 1
    PET_COLLAR = 2
    POTION = 3
    RECIPE = 4
    SCROLL = 5
    QUEST = 6
    MONEY = 7
    OTHER = 8
    SPELLBOOK = 9
    SEED = 10
    SHOT = 11
    HERB = 12


class EtcItem(Item):
    @property
    def is_consumable(self):
        return self.type in [EtcItemType.SHOT, EtcItemType.POTION]
