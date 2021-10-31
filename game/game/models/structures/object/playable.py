from __future__ import annotations

import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from game.models.structures.object.object import L2Object, L2ObjectDefaults


@dataclass
class PlayableDefaults(L2ObjectDefaults):
    target: typing.Union[None, Playable] = None


@dataclass
class Playable(L2Object, PlayableDefaults):
    def set_target(self, target: Playable):
        self.target = target
