import json
import typing
from typing import ClassVar

import bson
import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import Field

from common import exceptions
from common.config import Config
from common.json import JsonEncoder
from common.model import BaseModel


class Document(BaseModel):
    __primary_key__: ClassVar[str] = "object_id"

    __database__: ClassVar[str]
    __collection__: ClassVar[str]

    NotFoundError: ClassVar = exceptions.DocumentNotFound

    object_id: str = Field(default_factory=lambda: str(bson.ObjectId()), alias="_id")

    @property
    def primary_key(self):
        return getattr(self, self.__primary_key__)

    @property
    def primary_key_field_name(self):
        return self.__fields__[self.__primary_key__].alias

    @classmethod
    def client(cls) -> AsyncIOMotorClient:
        return AsyncIOMotorClient(Config().MONGO_URI)

    @classmethod
    def sync_client(cls) -> pymongo.MongoClient:
        return pymongo.MongoClient(Config().MONGO_URI)

    @classmethod
    def database(cls):
        return cls.client()[cls.__database__]

    @classmethod
    def sync_database(cls):
        return cls.sync_client()[cls.__database__]

    @classmethod
    def collection(cls):
        return cls.database()[cls.__collection__]

    @classmethod
    def sync_collection(cls):
        return cls.sync_database()[cls.__collection__]

    @classmethod
    async def one(cls, document_id=None, add_query=None, required=True, **kwargs):
        """Finds one document by ID."""

        query = {}
        if document_id is not None:
            query["_id"] = document_id
        if add_query is not None:
            query.update(add_query)

        encoder = JsonEncoder()
        query = encoder.encode_dict(query)

        result = await cls.collection().find_one(query, **kwargs)
        if result is not None:
            return cls(**result)
        elif required:
            raise cls.NotFoundError()

    @classmethod
    async def all(cls, document_ids=None, add_query=None, **kwargs):
        """Finds all documents based in IDs."""

        query = {}
        if document_ids is not None:
            query["_id"] = {"$in": document_ids}
        if add_query is not None:
            query.update(add_query)

        documents = []
        async_for = True

        encoder = JsonEncoder()
        query = encoder.encode_dict(query)

        cursor = cls.collection().find(query, **kwargs)
        if isinstance(cursor, typing.Coroutine):
            cursor = await cursor
            async_for = False

        if async_for:
            async for document in cursor:
                documents.append(cls(**document))
        else:
            for document in cursor:
                documents.append(cls(**document))
        return documents

    def delete(self):
        """Deletes document from collection."""

        return self.collection().delete_one({self.primary_key_field_name: self.primary_key})

    async def commit_changes(self, fields=None):
        """Saves changed document to collection."""

        search_query = {self.primary_key_field_name: self.primary_key}
        update_query = {"$set": {}}
        fields = fields if fields is not None else [field for field in self.dict()]

        data = self.dict()

        for field in fields:
            update_query["$set"].update({field: data[field]})
        return await self.collection().update_one(search_query, update_query)

    async def insert(self):
        """Inserts document into collection."""

        return await self.collection().insert_one(self.dict())
