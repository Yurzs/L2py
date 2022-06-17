import dataclasses

from src.common.common.dataclass import BaseDataclass
from src.game.game.models.structures.character.character import Character


@dataclasses.dataclass(kw_only=True)
class Party(BaseDataclass):
    participants: list
    leader: Character
