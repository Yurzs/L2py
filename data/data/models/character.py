import time
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from common.document import Document
from common.helpers.bytearray import ByteArray
from data.models.structures.character.character import Character as CharacterStructure
from data.models.structures.item.inventory import Inventory


@dataclass
class Buff(BaseDataclass):
    pass


@dataclass
class Character(CharacterStructure, Document):
    __collection__: str = field(default="characters", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)

    account_username: common.datatypes.String = None

    sex: common.datatypes.Int32 = field(default=0)
    race: common.datatypes.Int32 = field(default=0)
    base_class: common.datatypes.Int32 = field(default=0)
    active_class: common.datatypes.Int32 = field(default=0)
    active: common.datatypes.Int32 = field(default=1)

    karma: common.datatypes.Int32 = field(default=0)
    pk_kills: common.datatypes.Int32 = field(default=0)
    pvp_kills: common.datatypes.Int32 = field(default=0)

    hair_style: common.datatypes.Int32 = field(default=0)
    hair_color: common.datatypes.Int32 = field(default=0)
    face: common.datatypes.Int32 = field(default=0)

    delete_at: common.datatypes.Int32 = field(default=0)

    inventory: Inventory = Inventory()

    @property
    def time_until_deletion(self):
        return common.datatypes.Int32(
            common.datatypes.Int32(time.time()) - self.delete_at
            if self.delete_at
            else 0
        )

    @classmethod
    async def all(cls, account_username=None, **kwargs):
        return await super().all(
            add_query={"account_username": account_username}, **kwargs
        )

    def encode(self, session):
        account = session.get_data()["account"]

        data = ByteArray(b"")

        encoded = [
            self.name,
            self.id,
            account.username,
            session.id,
            common.datatypes.Int32(0),  # TODO: clan_id,
            common.datatypes.Int32(0),
            self.sex,
            self.race,
            self.active_class,
            self.active,
            self.position.point3d.x,
            self.position.point3d.y,
            self.position.point3d.z,
            self.status.hp,
            self.status.mp,
            self.stats.sp,
            self.stats.exp,
            self.stats.level,
            self.karma,
            self.pk_kills,
            self.pvp_kills,
            *[common.datatypes.Int32(0) for _ in range(7)],
            *[common.datatypes.Int32(0) for _ in range(17)],
            *[common.datatypes.Int32(0) for _ in range(17)],
            self.hair_style,
            self.hair_color,
            self.face,
            self.stats.max_hp,
            self.stats.max_mp,
            self.time_until_deletion,
            self.active_class,
            common.datatypes.Int32(1),
            common.datatypes.Int8(0),
            common.datatypes.Int32(0),
        ]

        for field in encoded:
            data.append(field)
        return data
