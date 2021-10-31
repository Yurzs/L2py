import asyncio
from dataclasses import dataclass, field

from common.document import Document


@dataclass
class IDFactoryDocument(Document):
    __collection__: String = field(default="id_factory", repr=False, init=False)
    __database__: String = field(default="l2py", repr=False, init=False)

    counter: Int32 = 0


class IdFactory:
    def __init__(self):
        self.document = asyncio.run(self.get_counter_document())

    @property
    def counter(self):
        return self.document.counter

    async def get_counter_document(self):
        document = await IDFactoryDocument.one()
        if document is None:
            document = IDFactoryDocument()
            await document.insert()
        return document

    async def update_counter(self):
        IDFactoryDocument.collection().update_one(
            {"_id": self.document._id}, {"$inc": {"counter": 1}}
        )

    def acquire_id(self):
        self.document.counter += 1
        asyncio.create_task(self.update_counter())


ID_FACTORY = IdFactory()
