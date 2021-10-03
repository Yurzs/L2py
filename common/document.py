import collections
import dataclasses
import os

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from common import exceptions
from common.dataclass import BaseDataclass

_CLIENTS = collections.defaultdict(lambda: AsyncIOMotorClient(os.environ["MONGO_URI"]))


@dataclasses.dataclass
class Document(BaseDataclass):
    __collection__: str
    __database__: str

    __primary_key__ = "_id"

    NotFoundError = exceptions.DocumentNotFound

    @property
    def id(self):
        return self._id

    @classmethod
    def client(cls) -> AsyncIOMotorClient:
        return _CLIENTS[os.getpid()]

    @classmethod
    def database(cls) -> AsyncIOMotorDatabase:
        return cls.client()[cls.__database__]

    @classmethod
    def collection(cls) -> AsyncIOMotorCollection:
        return cls.database()[cls.__collection__]

    @classmethod
    async def one(cls, document_id=None, add_query=None):
        """Finds one document by ID."""

        query = {}
        if document_id is not None:
            query["_id"] = document_id
        if add_query is not None:
            query.update(add_query)

        result = await cls.collection().find_one(query)
        if result is not None:
            return cls(**result)

    @classmethod
    async def all(cls, document_ids=None, add_query=None):
        """Finds all documents based in IDs."""

        query = {}
        if document_ids is not None:
            query["_id"] = {"$in": document_ids}
        if add_query is not None:
            query.update(add_query)

        async for document in cls.collection().find(query):
            yield cls(**document)

    def delete(self):
        """Deletes document from collection."""

        return self.collection().delete_one(
            {self.__primary_key__: getattr(self, self.__primary_key__)}
        )

    def commit_changes(self, fields=None):
        """Saves changed document to collection."""

        search_query = {self.__primary_key__: getattr(self, self.__primary_key__)}
        update_query = {"$set": {}}
        updated_document_dict = self.to_dict()
        if fields is not None:
            update_query["$set"].update(
                {field: updated_document_dict[field] for field in fields}
            )
        else:
            update_query["$set"] = {
                field: updated_document_dict[field] for field in self._fields
            }

        return self.collection().update_one(search_query, update_query)

    async def insert(self):
        """Inserts document into collection."""

        return await self.collection().insert_one(self.to_dict())
