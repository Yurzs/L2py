import dataclasses
import json
import typing

import bson
import pymongo
from motor.motor_asyncio import AsyncIOMotorClient

from common import exceptions
from common.config import Config
from common.dataclass import BaseDataclass
from common.json import JsonEncoder


class DocumentBase(BaseDataclass):
    __primary_key__ = "_id"

    NotFoundError = exceptions.DocumentNotFound

    @property
    def primary_key(self):
        return getattr(self, self.__primary_key__)

    @classmethod
    def client(cls):
        return AsyncIOMotorClient(Config().MONGO_URI)

    @classmethod
    def sync_client(cls):
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

        result = await cls.collection().find_one(query, **kwargs)
        if result is not None:
            return cls(**cls.convert_dataclasses(result))
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

        return self.collection().delete_one(
            {self.__primary_key__: getattr(self, self.__primary_key__)}
        )

    async def commit_changes(self, fields=None):
        """Saves changed document to collection."""

        search_query = {self.__primary_key__: getattr(self, self.__primary_key__)}
        update_query = {"$set": {}}
        fields = (
            fields
            if fields is not None
            else [field for field in self._fields if not field.startswith("__")]
        )

        for field in fields:
            value = getattr(self, field)
            update_query["$set"].update({field: json.dumps(value, cls=JsonEncoder)})
        return await self.collection().update_one(search_query, update_query)

    async def insert(self):
        """Inserts document into collection."""

        return await self.collection().insert_one(self.to_dict())


@dataclasses.dataclass(kw_only=True)
class Document(DocumentBase):
    _id: str = dataclasses.field(default_factory=lambda: str(bson.ObjectId()))


class MetaDocumentMixin(type):
    def __new__(mcs, name, bases, namespace):
        fields = []
        for field in dataclasses.fields(Document):
            field.kw_only = True
            fields.append((field.name, field.type, field))
        return dataclasses.make_dataclass(
            name, fields=fields, bases=bases, namespace=namespace
        )
