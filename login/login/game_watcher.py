import asyncio
import logging
import time
import typing

import login.clients
from common.application_modules.module import ApplicationModule
from common.client.game_client import GameClient

LOG = logging.getLogger(f"l2py.{__name__}")


class GameServersChecker(ApplicationModule):
    GAME_SERVERS: typing.Dict[typing.Tuple, asyncio.Task] = {}
    LAST_ACTIVE: typing.Dict[typing.Tuple, asyncio.Task] = {}

    def start(self, config, loop):
        LOG.info("Starting game server checker.")
        loop.create_task(self.watch())

    async def _ping(self, host, port):
        try:
            client = GameClient(host, port, https=False)
            while True:
                result = await client.ping()
                if result.get("pong") is True:
                    self.LAST_ACTIVE[(host, port - 1)] = int(time.time())
                await asyncio.sleep(10)
        except Exception as e:
            LOG.exception(e)

    async def watch(self):
        while True:
            for pinger in self.GAME_SERVERS.values():
                pinger.cancel()
            for server in await login.clients.DATA_CLIENT.get_game_servers():
                self.GAME_SERVERS[(server.host, server.port)] = asyncio.Task(
                    self._ping(server.host, server.port + 1)
                )
            await asyncio.sleep(60)
