import asyncio
import os

import dotenv

from common.misc import Singleton

dotenv.load_dotenv()


class Config(metaclass=Singleton):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.MONGO_URI = os.environ.get("MONGO_URI", "localhost")
