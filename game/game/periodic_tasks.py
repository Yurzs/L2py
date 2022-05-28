import time

from common.application_modules.scheduler import ScheduleModule
from common.models import GameServer
from game.config import GameConfig


@ScheduleModule.job("interval", seconds=10)
async def i_am_alive():
    server = await GameServer.one(GameConfig().GAME_SERVER_ID)
    server.last_alive = int(time.time())
    await server.commit_changes(fields=["last_alive"])
