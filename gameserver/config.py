import asyncio
import os

from motor.motor_asyncio import AsyncIOMotorClient

loop = asyncio.get_event_loop()

mongo_client = AsyncIOMotorClient(os.environ["MONGO_URI"])
database_name = "L2pyGame"
