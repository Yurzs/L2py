import asyncio
import dataclasses
import os

from common.misc import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.MONGO_URI = os.environ.get("MONGO_URI", "localhost")
