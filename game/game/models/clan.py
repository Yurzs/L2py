from dataclasses import dataclass, field

import pymongo

from common.ctype import ctype
from common.document import Document, DocumentBase


@dataclass(kw_only=True)
class Clan(Document):
    name: str
    leader: ctype.int32

    __collection__ = "clans"
    __database__ = "l2py"

    def create_indexes(self):
        self.sync_collection().create_index([("name", pymongo.ASCENDING)], unique=True)
        self.sync_collection().create_index([("leader", pymongo.ASCENDING)], unique=True)
