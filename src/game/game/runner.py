import logging

from src.game.game.application import GAME_SERVER_APPLICATION
from src.game.game.config import GameConfig
from src.game.game.models.world import WORLD

LOG = logging.getLogger(f"L2py.game")


def game_runner():
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
    game_runner()
