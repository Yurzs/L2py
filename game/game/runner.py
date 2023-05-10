import logging

import common  # noqa: F401
import game.api  # noqa: F401
import game.periodic_tasks  # noqa: F401
from game.application import GAME_SERVER_APPLICATION
from game.config import GameConfig
from game.models.world import WORLD

LOG = logging.getLogger(f"L2py.game")


def update_refs():
    import game.packets

    game.packets.CharSelected.update_forward_refs(Character=game.models.Character)
    game.packets.CharInfo.update_forward_refs(Character=game.models.Character)
    game.packets.CharList.update_forward_refs(Character=game.models.Character)
    game.packets.EtcStatusUpdate.update_forward_refs(Character=game.models.Character)
    game.packets.ExStorageMaxCount.update_forward_refs(Character=game.models.Character)
    game.packets.UserInfo.update_forward_refs(Character=game.models.Character)
    game.packets.CharMoveToLocation.update_forward_refs(Character=game.models.Character)


def main():
    GAME_SERVER_APPLICATION.run(
        {
            "game_web": {
                "host": GameConfig().GAME_SERVER_API_HOST,
                "port": GameConfig().GAME_SERVER_API_PORT,
            },
            "game_tcp": {
                "host": GameConfig().GAME_SERVER_HOST,
                "port": GameConfig().GAME_SERVER_PORT,
            },
        },
        log_level=logging.DEBUG,
        loop=GameConfig().loop,
        cleanup_task=WORLD.shutdown,
    )


if __name__ == "__main__":
    update_refs()
    main()
