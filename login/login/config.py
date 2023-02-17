import asyncio
import os

loop = asyncio.get_event_loop()

# Registration
auto_registration = True  # TODO

# Server config
LOGIN_SERVER_HOST = os.environ.get("LOGIN_SERVER_HOST", "0.0.0.0")
LOGIN_SERVER_PORT = os.environ.get("LOGIN_SERVER_PORT", 2106)

LOGIN_SERVER_API_HOST = os.environ.get("LOGIN_SERVER_API_HOST", "0.0.0.0")
LOGIN_SERVER_API_PORT = os.environ.get("LOGIN_SERVER_API_PORT", 2107)

DEBUG = os.environ.get("DEBUG", False)
