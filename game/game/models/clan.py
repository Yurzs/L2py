from dataclasses import dataclass, field

import pymongo

from common.document import Document, DocumentBases, DocumentDefaults


@dataclass
class ClanBases(DocumentBases):
    name: UTFString
    leader: cython.long


@dataclass
class ClanDefaults(DocumentDefaults):
    __collection__: str = field(default="clans", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)


@dataclass
class Clan(Document, ClanDefaults, ClanBases):
    def create_indexes(self):
        self.sync_collection().create_index([("name", pymongo.ASCENDING)], unique=True)
        self.sync_collection().create_index([("leader", pymongo.ASCENDING)], unique=True)
