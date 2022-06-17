import asyncio
import os

from src.common.common.config import Config


class GameConfig(Config):
    def __init__(self):
        super().__init__()
        self.GAME_SERVER_HOST = os.environ.get("GAME_SERVER_HOST", "0.0.0.0")
        self.GAME_SERVER_PORT = os.environ.get("GAME_SERVER_PORT", 7777)
        self.GAME_API_SERVER_HOST = os.environ.get("GAME_API_SERVER_HOST", "0.0.0.0")
        self.GAME_API_SERVER_PORT = os.environ.get("GAME_API_SERVER_PORT", 7778)
        self.GAME_SERVER_ID = os.environ["GAME_SERVER_ID"]
