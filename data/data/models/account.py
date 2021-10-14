import base64
import os
from dataclasses import dataclass, field
from hashlib import sha3_512

import pymongo

from common import datatypes
from common.document import Document, DocumentDefaults


@dataclass
class AccountDefaults(DocumentDefaults):
    last_server: datatypes.Int8 = None
    last_character: datatypes.Int32 = None
    salt: datatypes.UTFString = None
    email: datatypes.UTFString = None


@dataclass
class AccountBase:
    id: datatypes.UTFString
    username: datatypes.UTFString
    password: datatypes.UTFString
    status: datatypes.Int8


@dataclass
class Account(Document, AccountDefaults, AccountBase):
    __collection__ = "accounts"
    __database__ = "l2py"

    @classmethod
    async def one(cls, document_id=None, username=None, add_query=None):
        """Finds one account."""

        query = {}
        if document_id is not None:
            query["_id"] = document_id
        if username is not None:
            query["username"] = username

        query.update(add_query or {})

        return await super().one(add_query=query)

    async def set_new_password(self, password: str):
        """Sets new password for user.

        :param password: User defined password.
        """
        salt = base64.b64encode(os.urandom(20)).decode()
        salted_password = password + salt
        self.password = base64.b64encode(sha3_512(salted_password.encode()).digest()).decode()
        self.salt = salt
        await self.commit_changes(fields=["salt", "password"])

    def authenticate(self, password) -> bool:
        """Checks that provided password matches database one.

        :param password: User defined password.
        :return: are passwords match
        """

        salted_password = password + self.salt
        hashed_password = base64.b64encode(sha3_512(salted_password.encode()).digest()).decode()
        return self.password == hashed_password

    @classmethod
    async def create_indexes(cls):
        await cls.collection().create_index(
            [
                ("username", pymongo.ASCENDING),
            ],
            unique=True,
        )
