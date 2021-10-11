import base64
import os
from dataclasses import dataclass, field
from hashlib import sha3_512

import pymongo

from common import datatypes
from common.document import Document


@dataclass
class Account(Document):
    __collection__: str = field(default="accounts", init=False, repr=False)
    __database__: str = field(default="l2py", init=False, repr=False)

    _id: datatypes.String
    username: datatypes.UTFString
    email: datatypes.UTFString
    password: datatypes.UTFString
    salt: datatypes.UTFString
    last_server: datatypes.Int8
    last_character: datatypes.Int32
    status: datatypes.Int8 = 1

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
        self.password = base64.b64encode(
            sha3_512(salted_password.encode()).digest()
        ).decode()
        self.salt = salt
        await self.commit_changes(fields=["salt", "password"])

    def authenticate(self, password) -> bool:
        """Checks that provided password matches database one.

        :param password: User defined password.
        :return: are passwords match
        """

        salted_password = password + self.salt
        hashed_password = base64.b64encode(
            sha3_512(salted_password.encode()).digest()
        ).decode()
        return self.password == hashed_password

    @classmethod
    async def create_indexes(cls):
        await cls.collection().create_index(
            [
                ("username", pymongo.ASCENDING),
            ],
            unique=True,
        )
