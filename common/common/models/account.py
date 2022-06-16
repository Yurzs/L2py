import base64
import dataclasses
import os
from dataclasses import field
from hashlib import sha3_512

import pymongo

from common.ctype import ctype
from common.dataclass import BaseDataclass
from common.document import Document
from common.models.id_factory import IDFactory


@dataclasses.dataclass(kw_only=True)
class GameAuth(BaseDataclass):
    server_id: ctype.char = 0
    play_ok1: ctype.int32 = field(default_factory=ctype.int32.random)
    play_ok2: ctype.int32 = field(default_factory=ctype.int32.random)
    login_ok1: ctype.int32 = field(default_factory=ctype.int32.random)
    login_ok2: ctype.int32 = field(default_factory=ctype.int32.random)


@dataclasses.dataclass(kw_only=True)
class Account(Document):
    id: ctype.int32
    username: str
    password: str

    __collection__ = "accounts"
    __database__ = "l2py"

    status: ctype.char = 0
    last_server: ctype.char = 0
    last_character: str = ""
    email: str = ""
    salt: str = ""
    game_auth: GameAuth = field(default_factory=GameAuth)

    @classmethod
    async def create_index(cls):
        return await cls.collection().create_index(
            [
                ("username", pymongo.ASCENDING),
            ]
        )

    @classmethod
    async def new(cls, username: str, password: str):
        """Constructs new account."""

        new_id = await IDFactory.get_new_id(IDFactory.NAME_ACCOUNTS)
        acc = Account(
            id=new_id,
            username=username,
            password="",
        )
        await acc.insert()
        await acc.set_new_password(password=password)
        return acc

    @classmethod
    async def one(
        cls, document_id=None, username=None, add_query=None, **kwargs
    ) -> "Account":
        """Finds one account."""

        query = {}
        if document_id is not None:
            query["_id"] = document_id
        if username is not None:
            query["username"] = username

        query.update(add_query or {})

        return await super().one(add_query=query, **kwargs)

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

    async def login_authenticated(
        self, server_id, play_ok1, play_ok2, login_ok1, login_ok2
    ):
        """Saves information for game server auth."""

        self.game_auth = GameAuth(
            server_id=server_id,
            play_ok1=play_ok1,
            play_ok2=play_ok2,
            login_ok1=login_ok1,
            login_ok2=login_ok2,
        )

        self.last_server = server_id
        await self.commit_changes(fields=["game_auth", "last_server"])
