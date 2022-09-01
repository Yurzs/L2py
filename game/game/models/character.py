import dataclasses
import math
import time

import game.packets
from common.ctype import ctype
from common.dataclass import BaseDataclass
from common.document import DocumentBase, MetaDocumentMixin
from common.models import IDFactory
from game.models.structures.character.appearance import CharacterAppearance
from game.models.structures.character.character import Character as CharStructure
from game.models.structures.character.status import Status
from game.models.structures.character.template import CharacterTemplate
from game.models.structures.item.inventory import Inventory
from game.models.structures.macro import Macro
from game.models.structures.object.position import Position
from game.models.structures.shortcut import Shortcut


class Buff:
    pass


@dataclasses.dataclass(kw_only=True)
class AccountShort(BaseDataclass):
    _id: str
    username: str
    id: ctype.int32


@dataclasses.dataclass(kw_only=True)
class CharacterBase(CharStructure):
    account: AccountShort

    race: ctype.int32
    base_class: ctype.int32
    active_class: ctype.int32

    appearance: CharacterAppearance

    delete_at: ctype.int32 = 0
    friends: list[ctype.int32] = dataclasses.field(default_factory=list)
    inventory: Inventory = dataclasses.field(default_factory=Inventory)

    active: ctype.int32 = 0
    karma: ctype.int32 = 0

    pk_kills: ctype.int32 = 0
    pvp_kills: ctype.int32 = 0

    shortcuts: list[Shortcut] = dataclasses.field(default_factory=list)
    macros: list[Macro] = dataclasses.field(default_factory=list)
    macros_revision = 0

    __database__ = "l2py"
    __collection__ = "characters"

    @property
    def time_until_deletion(self) -> ctype.int32:
        return ctype.int32(self.delete_at - time.time() if self.delete_at else 0)

    @classmethod
    async def all(cls, account_username=None, **kwargs):
        return await super().all(
            add_query={"account.username": account_username}, **kwargs
        )

    @classmethod
    async def from_template(
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

        position = Position(point3d=template.spawn, heading_angle=0)

        appearance = CharacterAppearance(
            face_id=face,
            hair_style=hair_style,
            hair_color=hair_color,
            sex=sex,
        )

        return cls(
            id=await IDFactory.get_new_id(IDFactory.NAME_CHARACTERS),
            account=AccountShort(
                username=account.username,
                id=account.id,
                _id=account._id,
            ),
            is_visible=True,
            name=name,
            status=status,
            template=template,
            position=position,
            stats=template.stats,
            race=race,
            base_class=template.class_info.id,
            active_class=template.class_info.id,
            appearance=appearance,
        )

    async def mark_deleted(self):
        self.delete_at = ctype.int32(math.floor(time.time() + 7 * 24 * 60 * 60))
        await self.commit_changes(fields=["delete_at"])

    async def remove_deleted_mark(self):
        self.delete_at = ctype.int32(0)
        await self.commit_changes(fields=["delete_at"])

    def __hash__(self):
        return hash(f"{self.id}_{self.name}")

    def update_shortcut(self, session, shortcut):
        """
        Update shortcut immediately
        """
        session.send_packet(
            game.packets.ShortcutRegister(shortcut=shortcut)
        )

    def notify_shortcuts(self, session):
        """
        Load shortcuts on enter the world.
        """
        if self.shortcuts:
            for shortcut in self.shortcuts:
                session.send_packet(
                    game.packets.ShortcutRegister(shortcut=shortcut)
                )

    def notify_macros(self, session):
        """
        Load macros states on enter the world.
        """
        if self.macros:
            for macro in self.macros:
                session.send_packet(
                    game.packets.MacrosList(
                        macro=macro,
                        revision=self.macros_revision,
                        total_macros=len(self.macros),
                    )
                )
        else:
            session.send_packet(
                game.packets.MacrosList(
                    macro=None,
                    revision=self.macros_revision,
                    total_macros=len(self.macros),
                )
            )


@dataclasses.dataclass(kw_only=True)
class Character(CharacterBase, DocumentBase, metaclass=MetaDocumentMixin):
    pass

    def __hash__(self):
        return hash(self.id)
