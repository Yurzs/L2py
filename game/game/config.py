import asyncio
import os

loop = asyncio.get_event_loop()

LOGIN_SERVER_API_HOST = os.environ["LOGIN_SERVER_API_HOST"]
LOGIN_SERVER_API_PORT = os.environ.get("LOGIN_SERVER_API_PORT", 2107)

DATA_SERVER_HOST = os.environ["DATA_SERVER_HOST"]
DATA_SERVER_PORT = os.environ.get("DATA_SERVER_PORT", 2108)

GAME_SERVER_HOST = os.environ.get("GAME_SERVER_HOST", "0.0.0.0")
GAME_SERVER_PORT = os.environ.get("GAME_SERVER_PORT", 7777)

GAME_API_SERVER_HOST = os.environ.get("GAME_API_SERVER_HOST", "0.0.0.0")
GAME_API_SERVER_PORT = os.environ.get("GAME_API_SERVER_PORT", 7778)
