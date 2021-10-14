from __future__ import annotations

import typing
from dataclasses import dataclass, field

import common.datatypes
import data.models.structures.skill.skill
from data.models.structures.character.effects import Effects
from data.models.structures.character.stats import Stats
from data.models.structures.character.status import Status
from data.models.structures.character.template import CharacterTemplate
from data.models.structures.character.updates import UpdateChecks
from data.models.structures.object.object import L2Object, L2ObjectBase, L2ObjectDefaults
from data.models.structures.skill.skill import Skill


@dataclass
class CharacterBase(L2ObjectBase):
    stats: Stats
    status: Status
    template: CharacterTemplate


@dataclass
class CharacterDefaults(L2ObjectDefaults):
    attacked_by: typing.List[Character] = field(default_factory=list)
    last_skill: typing.Optional[data.models.structures.skill.skill.Skill] = None
    last_heal_amount: common.datatypes.Int32 = 0
    effects: Effects = Effects()
    title: common.datatypes.UTFString = ""
    ai_class: common.datatypes.UTFString = None
    hp_updates: UpdateChecks = UpdateChecks()
    is_champion: common.datatypes.Bool = False
    skills: typing.List[Skill] = field(default_factory=list)
    current_zone: None = None


@dataclass
class Character(L2Object, CharacterDefaults, CharacterBase):
    pass


Character.update_forward_refs()
