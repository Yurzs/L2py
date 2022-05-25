import dataclasses

from common.dataclass import BaseDataclass
from game.models.structures.character.character import Character


@dataclasses.dataclass(kw_only=True)
class Party(BaseDataclass):
    participants: list
    leader: Character
