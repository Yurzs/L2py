from typing import ClassVar

from pydantic import Field

from common.ctype import ctype
from common.document import Document


class LoginServer(Document):
    id: str = Field(alias="_id")
    host: str
    port: ctype.int
    status: ctype.int8

    __collection__: ClassVar[str] = "login_servers"
    __database__: ClassVar[str] = "l2py"
