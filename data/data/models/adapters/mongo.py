import asyncio
import collections
import typing

import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from common.adapter import DataAdapter
from data.config import MONGO_URI


class MongoAdapter(DataAdapter):
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    def client(self):
        return AsyncIOMotorClient(MONGO_URI)

    def collection(self, database_name, collection_name):
        return self.database(database_name)[collection_name]

    def database(self, database_name):
        return self.client()[database_name]

    async def proceed_action(self, query):

        database_name = query["database"]
        collection_name = query["collection"]
        args = query["args"]
        kwargs = query["kwargs"]
        action_name = query["action"]

        print(query)
        result = getattr(self.collection(database_name, collection_name), action_name)(
            *args, **kwargs
        )
        if isinstance(result, (typing.Coroutine, asyncio.Future)):
            return await result
        elif isinstance(result, motor.motor_asyncio.AsyncIOMotorCursor):
            return [doc async for doc in result]
        return result
