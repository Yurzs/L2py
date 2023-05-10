import asyncio
from typing import ClassVar

import bson

from common.ctype import ctype
from common.document import Document


class IDFactory(Document):
    __collection__: ClassVar[str] = "id_factory"
    __database__: ClassVar[str] = "l2py"

    NAME_ITEMS: ClassVar[str] = "items"
    NAME_CHARACTERS: ClassVar[str] = "characters"
    NAME_ACCOUNTS: ClassVar[str] = "accounts"

    name: str
    counter: ctype.int32 = 1

    @classmethod
    async def get_new_id(cls, object_type_name: str):
        item_id_factory = await cls.one(add_query={"name": object_type_name}, required=False)
        if item_id_factory is None:
            item_id_factory = cls(name=object_type_name, _id=str(bson.ObjectId()))
            await item_id_factory.insert()
        asyncio.Task(item_id_factory.increment())
        return item_id_factory.counter

    async def increment(self):
        self.collection().update_one(
            {self.primary_key_field_name: self.primary_key}, {"$inc": {"counter": 1}}
        )
