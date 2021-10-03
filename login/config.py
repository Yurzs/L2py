import asyncio
import os

from motor.motor_asyncio import AsyncIOMotorClient

from common.client.data_client import DataClient

loop = asyncio.get_event_loop()

# Database connection
mongo_client = AsyncIOMotorClient(os.environ["MONGO_URI"])
database_name = "L2pyLogin"

# Registration
auto_registration = True

# Server config
SERVER_HOST = os.environ.get("SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.environ.get("SERVER_PORT", 2106)
server_info = (SERVER_HOST, SERVER_PORT)

SERVER_API_HOST = os.environ.get("SERVER_API_HOST", "0.0.0.0")
SERVER_API_PORT = os.environ.get("SERVER_API_PORT", 2107)
server_api_info = (SERVER_API_HOST, SERVER_API_PORT)

# Data server config
DATA_SERVER_IP = os.environ.get("DATA_SERVER_IP", "localhost")
DATA_SERVER_PORT = os.environ.get("DATA_SERVER_PORT", 2108)
data_server_connection_info = (DATA_SERVER_IP, DATA_SERVER_PORT)
