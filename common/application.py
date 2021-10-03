import abc
import asyncio
import json
import logging
import sys

from aiohttp import web

LOG = logging.getLogger(f"L2py.{__name__}")


class Application:
    def __init__(self, modules):
        self.modules = modules

    def run(self, config, loop=None, log_level=logging.INFO):
        logging.basicConfig(stream=sys.stdout, level=log_level)

        loop = loop if loop is not None else asyncio.get_event_loop()
        for module in self.modules:
            module.start(config=config[module.name], loop=loop)

        loop.run_forever()
