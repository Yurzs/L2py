from dataclasses import dataclass, field

from src.common.common.ctype import ctype
from src.common.common.document import Document, DocumentBases, DocumentDefaults


@dataclass(kw_only=True)
class LoginServerDefaults(DocumentDefaults):
    __collection__: str = field(default="login_servers", repr=False, init=False)
    __database__: str = field(default="l2py", repr=False, init=False)


@dataclass(kw_only=True)
class LoginServerBases(DocumentBases):
    _id: str
    host: str
    port: ctype.int
    status: ctype.int8


@dataclass(kw_only=True)
class LoginServer(Document, DocumentBases, DocumentDefaults):
    pass
