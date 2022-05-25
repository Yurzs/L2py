import asyncio
import dataclasses

import bson

from common.ctype import ctype
from common.document import Document


@dataclasses.dataclass(kw_only=True)
class IDFactory(Document):
    __collection__ = "id_factory"
    __database__ = "l2py"

    NAME_ITEMS = "items"
    NAME_CHARACTERS = "characters"
    NAME_ACCOUNTS = "accounts"

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
        self.collection().update_one({"_id": self._id}, {"$inc": {"counter": 1}})
