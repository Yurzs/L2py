import time
import typing
from dataclasses import dataclass, field

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
    account_username: String

    sex: Int32
    race: Int32
    base_class: Int32
    active_class: Int32

    hair_style: Int32
    hair_color: Int32
    face: Int32


@dataclass
class CharacterDefaults(DocumentDefaults, CharacterDefaultsStructure):
    __collection__: str = field(default="characters", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)

    delete_at: Int32 = field(default=0)
    friends: typing.List[Int32] = field(default_factory=list)
    inventory: Inventory = Inventory()

    active: Int32 = True
    karma: Int32 = 0

    pk_kills: Int32 = 0
    pvp_kills: Int32 = 0


@dataclass
class Character(
    CharacterStructure,
    Document,
    CharacterDefaults,
    CharacterBase,
):
    @property
    def time_until_deletion(self):
        return Int32(Int32(self.delete_at - time.time()) if self.delete_at else 0)

    @classmethod
    async def all(cls, account_username=None, **kwargs):
        return await super().all(add_query={"account_username": account_username}, **kwargs)

    @classmethod
    def from_template(
        cls,
        template: CharacterTemplate,
        name,
        account,
        sex,
        race,
        face,
        hair_style,
        hair_color,
    ):

        status = Status(
            hp=template.stats.max_hp,
            cp=template.stats.max_cp,
            mp=template.stats.max_cp,
        )

        position = Position(point3d=template.spawn)

        return cls(
            id=Int32.random(),
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

    async def mark_deleted(self):
        self.delete_at = time.time() + 7 * 24 * 60 * 60
        await self.commit_changes(fields=["delete_at"])

    async def remove_deleted_mark(self):
        self.delete_at = 0
        await self.commit_changes(fields=["delete_at"])

    def __hash__(self):
        return hash(f"{self.id}_{self.name}")
