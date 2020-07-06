from motor.motor_asyncio import AsyncIOMotorClient
import os
import asyncio


loop = asyncio.get_event_loop()

mongo_client = AsyncIOMotorClient(os.environ["MONGO_URI"])
database_name = "L2pyLogin"
