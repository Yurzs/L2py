import dataclasses
from dataclasses import field

import game.packets
from common.ctype import ctype
from game.broadcaster import Broadcaster
from game.models.structures.character.stats import Stats
from game.models.structures.character.status import Status
from game.models.structures.character.template import CharacterTemplate
from game.models.structures.character.updates import UpdateChecks
from game.models.structures.object.playable import Playable
from game.models.structures.skill.skill import Skill
from game.models.structures.world_region import WorldRegion


@dataclasses.dataclass(kw_only=True)
class Character(Playable):
    stats: Stats
    status: Status
    template: CharacterTemplate
    attacked_by: list = field(default_factory=list)

    last_skill: Skill = field(default_factory=Skill)
    last_heal_amount: ctype.int32 = 0
    title: str = ""
    ai_class: str = ""
    hp_updates: UpdateChecks = field(default_factory=UpdateChecks)
    skills: list[Skill] = field(default_factory=list)
    current_zone: WorldRegion = field(default_factory=WorldRegion)
    name_color: ctype.int32 = 2147483647
    title_color: ctype.int32 = 2147483647

    # TODO: Find a better place for those properties
    @property
    def weight_penalty(self) -> ctype.int32:
        return ctype.int32(0)

    @property
    def exp_penalty(self) -> ctype.int32:
        return ctype.int32(0)

    @property
    def exp_protected(self) -> ctype.int32:
        return ctype.int32(0)

    @property
    def death_penalty(self) -> ctype.int32:
        return ctype.int32(0)

    @property
    def inventory_max(self) -> ctype.int16:
        return ctype.int16(80)

    @property
    def warehouse_max(self) -> ctype.int32:
        return ctype.int32(80)

    @property
    def private_sell_max(self) -> ctype.int32:
        return ctype.int32(80)

    @property
    def private_buy_max(self) -> ctype.int32:
        return ctype.int32(80)

    @property
    def freight_max(self) -> ctype.int32:
        return ctype.int32(80)

    @property
    def dwarf_receipt_max(self) -> ctype.int32:
        return ctype.int32(80)

    @property
    def common_receipt_max(self) -> ctype.int32:
        return ctype.int32(80)

    @Broadcaster.broadcast(
        lambda self, *args, **kwargs: game.packets.CharMoveToLocation(
            character=self, new_position=self.position
        ),
        to_me=True,
    )
    async def move(self, new_position):
        self.position = new_position

    @Broadcaster.broadcast(
        lambda self, action_id: game.packets.SocialAction(
            character_id=self.id, action_id=action_id
        ),
        to_me=True,
        pass_args_kwargs=True,
    )
    async def use_social_action(self, action_id):
        pass

    @Broadcaster.broadcast(packet_constructor=lambda self: game.packets.CharInfo(character=self))
    @Broadcaster.broadcast(
        packet_constructor=lambda self: game.packets.CharMoveToLocation(
            character=self, new_position=self.position
        )
    )
    async def spawn(self):
        pass
