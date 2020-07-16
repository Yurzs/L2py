import os
import base64
from hashlib import sha3_512

from mdocument import Document

from loginserver.config import database_name, mongo_client


class Account(Document):
    """LoginServer user account.

        structure = {
            "login": str,
            "password": str,
            "salt": str,
            "banned": bool,
            "deleted": bool,
        }

    """

    collection = "accounts"
    database = database_name
    client = mongo_client

    @classmethod
    def create(cls, login, password) -> "Document":
        """Register new user."""

        hashed_password, salt = cls.hash_password(password)

        query = {
            "login": login,
            "password": hashed_password,
            "salt": salt,
        }

        return await super().create(**query)

    @staticmethod
    def hash_password(password, salt=None) -> tuple:
        """Hashes plain text password."""

        salt = base64.urlsafe_b64encode(os.urandom(50)).decode() if not salt else salt
        salt = salt[::-1]
        hashed = sha3_512(password.encode())
        hashed.update(salt.encode())
        return base64.urlsafe_b64encode(hashed.digest()).decode(), salt[::-1]

    def check_password(self, password):
        """Checks that provided password matches hashed in db."""

        hashed_password, salt = self.hash_password(password, self.salt)
        if hashed_password == self.password:
            return True
        return False

    @classmethod
    async def authenticate(cls, login, password):
        """Authenticate account using password."""

        account = await cls.one(login=login)
        if account.check_password(password) and not getattr(account, "deleted", False):
            return account

    @property
    def can_login(self):
        return True if not getattr(self, "banned", False) else False

    async def ban(self):
        """Mark account as banned."""

        self.banned = True
        await self.push_update()
