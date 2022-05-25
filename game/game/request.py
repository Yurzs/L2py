import dataclasses

from common.request import Request
from game.session import GameSession


@dataclasses.dataclass(kw_only=True)
class GameRequest(Request):
    session: GameSession
