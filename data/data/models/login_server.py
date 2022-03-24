from dataclasses import dataclass, field

from common import datatypes
from common.document import Document


@dataclass
class LoginServer(Document):
    __collection__: datatypes.String = field(default="login_servers", repr=False, init=False)
    __database__: datatypes.String = field(default="l2py", repr=False, init=False)

    _id: datatypes.String
    host: datatypes.String
    port: datatypes.Int16
    status: datatypes.Int8
