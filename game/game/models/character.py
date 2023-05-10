import math
import time
from typing import ClassVar, Optional

from bson import ObjectId
from pydantic import Field

import game.packets
from common.ctype import ctype
from common.document import Document
from common.model import BaseModel
from common.models import IDFactory
from game.models.structures.character.appearance import CharacterAppearance
from game.models.structures.character.character import Character as CharStructure
from game.models.structures.character.status import Status
from game.models.structures.character.template import CharacterTemplate
from game.models.structures.item.inventory import Inventory
from game.models.structures.macro import Macro
from game.models.structures.object.position import Position
from game.models.structures.shortcut import Shortcut
from game.session import GameSession
from game.static.character_template import StaticCharacterTemplate


class Buff:
    pass


class AccountShort(BaseModel):
    username: str
    account_id: ctype.int32


class Character(Document, CharStructure):
    account: AccountShort

    template: Optional[CharacterTemplate] = Field(exclude=True)

    race: ctype.int32
    base_class: ctype.int32
    active_class: ctype.int32

    appearance: CharacterAppearance

    session: Optional[GameSession] = Field(None, exclude=True)

    # id of character who currently sends request (Party invite, Friend invite, Trade, etc.)
    active_requestor: ctype.int32 = Field(0, exclude=True)

    delete_at: ctype.int32 = 0
    friends: list[ctype.int32] = Field(default_factory=list)
    inventory: Inventory = Field(default_factory=Inventory)

    active: ctype.int32 = 0
    karma: ctype.int32 = 0

    pk_kills: ctype.int32 = 0
    pvp_kills: ctype.int32 = 0

    shortcuts: list[Shortcut] = Field(default_factory=list)
    macros: list[Macro] = Field(default_factory=list)
    macros_revision = 0

    __database__: ClassVar[str] = "l2py"
    __collection__: ClassVar[str] = "characters"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_template()

    @property
    def time_until_deletion(self) -> ctype.int32:
        return ctype.int32(self.delete_at - time.time() if self.delete_at else 0)

    def get_template(self) -> CharacterTemplate:
        if self.template is None:
            static_template = {
                template.class_id: template for template in StaticCharacterTemplate.read_file()
            }
            self.template = CharacterTemplate.from_static_template(
                static_template[self.base_class], self.appearance.sex
            )
        return self.template

    @classmethod
    async def one_by_name(cls, character_name: str, required=True):
        return await super().one(add_query={"name": character_name}, required=required)

    @classmethod
    async def all(cls, account_username=None, **kwargs):
        return await super().all(add_query={"account.username": account_username}, **kwargs)

    @classmethod
    async def all_by_game_id(cls, character_game_ids: list[ctype.int32]):
        return await super().all(add_query={"id": {"$in": character_game_ids}})

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
            object_id=str(ObjectId()),
            id=await IDFactory.get_new_id(IDFactory.NAME_CHARACTERS),
            account=AccountShort(
                username=account.username,
                account_id=account.account_id,
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
        """Update shortcut immediately."""
        session.send_packet(game.packets.ShortcutRegister(shortcut=shortcut))

    def notify_shortcuts(self, session):
        """Load shortcuts on enter the world."""
        if self.shortcuts:
            for shortcut in self.shortcuts:
                session.send_packet(game.packets.ShortcutRegister(shortcut=shortcut))

    def notify_macros(self, session):
        """Load macros states on enter the world."""
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

    async def notify_friends(self, session):
        from game.models.world import WORLD

        friends_list = await Character.all_by_game_id(self.friends)
        if not friends_list:
            session.send_packet(game.packets.FriendList())
            return

        friends = list()
        for char in friends_list:
            char.session = WORLD.get_session_by_character_name(char.name)
            friends.append(char)

        session.send_packet(game.packets.FriendList(friends=friends))

        online_friends = [char for char in friends if char.session]

        return online_friends
