import time
import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.document import Document, DocumentDefaults
from common.models import IDFactory
from game.models.structures.character.character import Character as CharacterStructure
from game.models.structures.character.character import CharacterBase as CharacterBaseStructure
from game.models.structures.character.character import (
    CharacterDefaults as CharacterDefaultsStructure,
)
from game.models.structures.character.status import Status
from game.models.structures.character.template import CharacterTemplate
from game.models.structures.item.inventory import Inventory
from game.models.structures.object.position import Position


@dataclass
class Buff(BaseDataclass):
    pass


@dataclass
class CharacterBase(CharacterBaseStructure):
    account_username: String

    sex: cython.long
    race: cython.long
    base_class: cython.long
    active_class: cython.long

    hair_style: cython.long
    hair_color: cython.long
    face: cython.long


@dataclass
class CharacterDefaults(DocumentDefaults, CharacterDefaultsStructure):
    __collection__: str = field(default="characters", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)

    delete_at: cython.long = field(default=0)
    friends: typing.List[cython.long] = field(default_factory=list)
    inventory: Inventory = Inventory()

    active: cython.long = True
    karma: cython.long = 0

    pk_kills: cython.long = 0
    pvp_kills: cython.long = 0


@dataclass
class Character(
    CharacterStructure,
    Document,
    CharacterDefaults,
    CharacterBase,
):
    @property
    def time_until_deletion(self):
        return cython.long(cython.long(self.delete_at - time.time()) if self.delete_at else 0)

    @classmethod
    async def all(cls, account_username=None, **kwargs):
        return await super().all(add_query={"account_username": account_username}, **kwargs)

    @classmethod
    async def from_template(
        cls, template: CharacterTemplate, name, account, sex, race, face, hair_style, hair_color
    ):

        status = Status(
            hp=template.stats.max_hp,
            cp=template.stats.max_cp,
            mp=template.stats.max_cp,
        )

        position = Position(point3d=template.spawn)

        return cls(
            id=await IDFactory.get_new_id(IDFactory.NAME_CHARACTERS),
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
