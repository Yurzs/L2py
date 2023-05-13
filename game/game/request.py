from common.request import Request
from game.session import GameSession


class GameRequest(Request):
    session: GameSession
