import asyncio
import os

from motor.motor_asyncio import AsyncIOMotorClient

loop = asyncio.get_event_loop()

mongo_client = AsyncIOMotorClient(os.environ["MONGO_URI"])
database_name = "L2pyGame"

# Login server info
login_server_api_ip = "127.0.0.1"
login_server_api_port = 2107

# Datapack server info
data_server_api_ip = "127.0.0.1"
data_server_api_port = 2108
