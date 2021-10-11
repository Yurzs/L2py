import logging

import game.api.http  # noqa: F401
import game.api.l2  # noqa: F401
import game.clients
import game.config
from common.document import register_adapter
from data.models.adapters.http import HttpAdapter
from game.application import GAME_SERVER_APPLICATION
from game.session import GameSession

LOG = logging.getLogger(f"L2py.game")


def main():
    register_adapter(HttpAdapter(game.clients.DATA_CLIENT))
    GameSession.start()
    GAME_SERVER_APPLICATION.run(
        {
            "game_web": {
                "host": game.config.GAME_API_SERVER_HOST,
                "port": game.config.GAME_API_SERVER_PORT,
            },
            "game_tcp": {
                "host": game.config.GAME_SERVER_HOST,
                "port": game.config.GAME_SERVER_PORT,
            },
        },
        loop=game.config.loop,
    )


if __name__ == "__main__":
    main()
