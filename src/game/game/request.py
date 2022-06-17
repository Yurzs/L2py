import dataclasses

from src.common.common.request import Request
from src.game.game.session import GameSession


@dataclasses.dataclass(kw_only=True)
class GameRequest(Request):
    session: GameSession
