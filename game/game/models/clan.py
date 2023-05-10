from typing import ClassVar

import pymongo

from common.ctype import ctype
from common.document import Document


class Clan(Document):
    name: str
    leader: ctype.int32

    __collection__: ClassVar[str] = "clans"
    __database__: ClassVar[str] = "l2py"

    def create_indexes(self):
        self.sync_collection().create_index([("name", pymongo.ASCENDING)], unique=True)
        self.sync_collection().create_index([("leader", pymongo.ASCENDING)], unique=True)
