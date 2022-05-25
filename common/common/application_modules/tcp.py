import asyncio
import logging

from common.application_modules.module import ApplicationModule

LOG = logging.getLogger(f"L2py.{__name__}")


class TCPServerModule(ApplicationModule):
    """TCP requests handler module.

    Serves requests passed to TCP port.
    """

    def __init__(self, name, protocol, middleware=None):
        super().__init__(name)
        self.protocol = protocol
        self.middleware = middleware or []
        self.loop = None

    def start(self, config, loop):
        async def inner_start():
            server = await loop.create_server(
                lambda: self.protocol(self.loop, self.middleware),
                config["host"],
                config["port"],
            )

            LOG.info(
                f"Starting L2 %s server on %s:%s",
                self.name,
                config["host"],
                config["port"],
            )
            async with server:
                await server.start_serving()
                while True:
                    await asyncio.sleep(3600)

        return loop.create_task(inner_start())
