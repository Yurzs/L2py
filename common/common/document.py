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
    async def one(cls, document_id=None, add_query=None, required=True, **kwargs):
        """Finds one document by ID."""

        query = {}
        if document_id is not None:
            query["_id"] = document_id
        if add_query is not None:
            query.update(add_query)

        print(required)
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

    def commit_changes(self, fields=None):
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
            update_query["$set"].update(
                {field: value.to_dict() if isinstance(value, BaseDataclass) else value}
            )

        return self.collection().update_one(search_query, update_query)

    async def insert(self):
        """Inserts document into collection."""

        return await self.collection().insert_one(self.to_dict())
