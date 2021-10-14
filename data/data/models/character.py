import datetime
import time
import typing
from dataclasses import dataclass, field

import common.datatypes
from common.dataclass import BaseDataclass
from common.document import Document, DocumentDefaults
from common.helpers.bytearray import ByteArray
from data.models.structures.character.character import Character as CharacterStructure
from data.models.structures.character.character import CharacterBase as CharacterBaseStructure
from data.models.structures.character.character import (
    CharacterDefaults as CharacterDefaultsStructure,
)
from data.models.structures.character.status import Status
from data.models.structures.character.template import CharacterTemplate
from data.models.structures.item.inventory import Inventory
from data.models.structures.object.position import Position


@dataclass
class Buff(BaseDataclass):
    pass


@dataclass
class CharacterBase(CharacterBaseStructure):
    account_username: common.datatypes.String

    sex: common.datatypes.Int32
    race: common.datatypes.Int32
    base_class: common.datatypes.Int32
    active_class: common.datatypes.Int32

    hair_style: common.datatypes.Int32
    hair_color: common.datatypes.Int32
    face: common.datatypes.Int32


@dataclass
class CharacterDefaults(DocumentDefaults, CharacterDefaultsStructure):
    __collection__: str = field(default="characters", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)

    delete_at: common.datatypes.Int32 = field(default=0)
    friends: typing.List[common.datatypes.Int32] = field(default_factory=list)
    inventory: Inventory = Inventory()

    active: common.datatypes.Int32 = True
    karma: common.datatypes.Int32 = 0

    pk_kills: common.datatypes.Int32 = 0
    pvp_kills: common.datatypes.Int32 = 0


@dataclass
class Character(
    CharacterStructure,
    Document,
    CharacterDefaults,
    CharacterBase,
):
    @property
    def time_until_deletion(self):
        return common.datatypes.Int32(
            common.datatypes.Int32(self.delete_at - time.time()) if self.delete_at else 0
        )

    @classmethod
    async def all(cls, account_username=None, **kwargs):
        return await super().all(add_query={"account_username": account_username}, **kwargs)

    @classmethod
    def from_template(
        cls, template: CharacterTemplate, name, account, sex, race, face, hair_style, hair_color
    ):

        status = Status(
            hp=template.stats.max_hp,
            cp=template.stats.max_cp,
            mp=template.stats.max_cp,
        )

        position = Position(point3d=template.spawn)

        return cls(
            id=common.datatypes.Int32.random(),
            account_username=account.username,
            is_visible=True,
            name=name,
            status=status,
            template=template,
            position=position,
            stats=template.stats,
            sex=sex,
            race=race,
            base_class=template.class_info.id,
            active_class=template.class_info.id,
            hair_style=hair_style,
            hair_color=hair_color,
            face=face,
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

    async def mark_deleted(self):
        self.delete_at = time.time() + 7 * 24 * 60 * 60
        await self.commit_changes(fields=["delete_at"])

    async def remove_deleted_mark(self):
        self.delete_at = 0
        await self.commit_changes(fields=["delete_at"])
