from common.model import BaseModel
from game.models.structures.character.character import Character


class Party(BaseModel):
    participants: list
    leader: Character
