import dataclasses
import typing

import bson

from common import exceptions
from common.adapter import DataAdapter
from common.dataclass import BaseDataclass

_ADAPTER = {"adapter": DataAdapter}


def register_adapter(adapter):
    _ADAPTER["adapter"] = adapter


@dataclasses.dataclass
class DocumentDefaults:
    _id: bson.ObjectId = dataclasses.field(default_factory=bson.ObjectId)


@dataclasses.dataclass
class Document(BaseDataclass, DocumentDefaults):
    __primary_key__ = "_id"

    NotFoundError = exceptions.DocumentNotFound

    @property
    def primary_key(self):
        return getattr(self, self.__primary_key__)

    @classmethod
    def client(cls):
        return _ADAPTER["adapter"].client()

    @classmethod
    def database(cls):
        return _ADAPTER["adapter"].database(cls.__database__)

    @classmethod
    def collection(cls):
        return _ADAPTER["adapter"].collection(cls.__database__, cls.__collection__)

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

        documents = []
        async_for = True

        cursor = cls.collection().find(query)
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

    def commit_changes(self, fields=None):
        """Saves changed document to collection."""

        search_query = {self.__primary_key__: getattr(self, self.__primary_key__)}
        update_query = {"$set": {}}
        updated_document_dict = self.to_dict()
        if fields is not None:
            update_query["$set"].update({field: updated_document_dict[field] for field in fields})
        else:
            update_query["$set"] = {field: updated_document_dict[field] for field in self._fields}

        return self.collection().update_one(search_query, update_query)

    async def insert(self):
        """Inserts document into collection."""

        return await self.collection().insert_one(self.to_dict())
