from __future__ import annotations

import typing
from dataclasses import dataclass, field

import game.models.structures.skill.skill
from game.models.structures.character.stats import Stats
from game.models.structures.character.status import Status
from game.models.structures.character.template import CharacterTemplate
from game.models.structures.character.updates import UpdateChecks
from game.models.structures.object.object import L2ObjectBases
from game.models.structures.object.playable import Playable, PlayableDefaults
from game.models.structures.skill.skill import Skill


@dataclass
class CharacterBase(L2ObjectBases):
    stats: Stats
    status: Status
    template: CharacterTemplate


@dataclass
class CharacterDefaults(PlayableDefaults):
    attacked_by: typing.List[Character] = field(default_factory=list)
    last_skill: typing.Optional[game.models.structures.skill.skill.Skill] = None
    last_heal_amount: Int32 = 0
    title: UTFString = ""
    ai_class: UTFString = None
    hp_updates: UpdateChecks = UpdateChecks()
    is_champion: Bool = False
    skills: typing.List[Skill] = field(default_factory=list)
    current_zone: None = None
    name_color: Int32 = 2147483647
    title_color: Int32 = 2147483647


@dataclass
class Character(Playable, CharacterDefaults, CharacterBase):

    # TODO: Find a better place for those properties
    @property
    def weight_penalty(self):
        return Int32(0)

    @property
    def exp_penalty(self):
        return Int32(0)

    @property
    def exp_protected(self):
        return Int32(0)

    @property
    def death_penalty(self):
        return Int32(0)

    @property
    def inventory_max(self):
        return Int32(80)

    @property
    def warehouse_max(self):
        return Int32(80)

    @property
    def private_sell_max(self):
        return Int32(80)

    @property
    def private_buy_max(self):
        return Int32(80)

    @property
    def freight_max(self):
        return Int32(80)

    @property
    def dwarf_receipt_max(self):
        return Int32(80)

    @property
    def common_receipt_max(self):
        return Int32(80)


Character.update_forward_refs()
