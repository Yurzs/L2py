import asyncio
from dataclasses import dataclass, field

from common.document import Document, DocumentBases


@dataclass
class IDFactoryBases(DocumentBases):
    name: UTFString


@dataclass
class IDFactory(Document, IDFactoryBases):
    __collection__: String = field(default="id_factory", repr=False, init=False)
    __database__: String = field(default="l2py", repr=False, init=False)

    NAME_ITEMS = "items"
    NAME_CHARACTERS = "characters"

    counter: Int32 = 1

    @classmethod
    async def get_new_id(cls, object_type_name: str):
        item_id_factory = await cls.one(add_query={"name": object_type_name}, required=False)
        if item_id_factory is None:
            item_id_factory = cls(cls.NAME_ITEMS)
            await item_id_factory.insert()
        asyncio.Task(item_id_factory.increment())
        return item_id_factory.counter

    async def increment(self):
        self.collection().update_one({"_id": self._id}, {"$inc": {"counter": 1}})
