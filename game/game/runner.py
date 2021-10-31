import logging

import common  # noqa: F401
import game.api.http  # noqa: F401
import game.api.l2  # noqa: F401
import game.periodic_tasks  # noqa: F401
from game.application import GAME_SERVER_APPLICATION
from game.config import GameConfig
from game.models.world import WORLD
from game.session import GameSession

LOG = logging.getLogger(f"L2py.game")


def main():
    GAME_SERVER_APPLICATION.run(
        {
            "game_web": {
                "host": GameConfig().GAME_API_SERVER_HOST,
                "port": GameConfig().GAME_API_SERVER_PORT,
            },
            "game_tcp": {
                "host": GameConfig().GAME_SERVER_HOST,
                "port": GameConfig().GAME_SERVER_PORT,
            },
        },
        loop=GameConfig().loop,
        cleanup_task=WORLD.shutdown,
    )


if __name__ == "__main__":
    main()
