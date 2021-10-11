from __future__ import annotations

import typing
from dataclasses import dataclass, field

import common.datatypes
import data.models.structures.skill.skill
from data.models.structures.character.effects import Effects
from data.models.structures.character.stats import Stats
from data.models.structures.character.status import Status
from data.models.structures.character.template import CharacterBaseTemplate
from data.models.structures.character.updates import UpdateChecks
from data.models.structures.object.object import L2Object
from data.models.structures.skill.skill import Skill


@dataclass
class Character(L2Object):
    attacked_by: typing.List[Character] = field(default_factory=lambda: [])
    last_skill: typing.Optional[data.models.structures.skill.skill.Skill] = None
    effects: Effects = Effects()
    last_heal_amount: common.datatypes.Int32 = 0
    stats: Stats = Stats()
    status: Status = Status()
    template: CharacterBaseTemplate = CharacterBaseTemplate()
    title: common.datatypes.UTFString = ""
    ai_class: common.datatypes.UTFString = None
    hp_updates: UpdateChecks = UpdateChecks()
    is_champion: common.datatypes.Bool = False
    current_zone: None = None
    skills: typing.List[Skill] = field(default_factory=lambda: [])


Character.update_forward_refs()
