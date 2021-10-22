import asyncio
import logging
import sys

LOG = logging.getLogger(f"L2py.{__name__}")


class Application:
    def __init__(self, modules):
        self.modules = modules

    def run(self, config, loop=None, log_level=logging.INFO, cleanup_task=None):
        logging.basicConfig(stream=sys.stdout, level=log_level)

        loop = loop if loop is not None else asyncio.get_event_loop()
        for module in self.modules:
            module.start(config=config.get(module.name, {}), loop=loop)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            if cleanup_task:
                cleanup_task()
            raise
