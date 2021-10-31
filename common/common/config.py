import asyncio
import os

from dotenv import load_dotenv

from common.misc import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        load_dotenv()
        self.loop = asyncio.get_event_loop()
        self.MONGO_URI = os.environ["MONGO_URI"]
