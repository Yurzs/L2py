import time
import typing
from dataclasses import dataclass, field

from common.helpers.cython import convert_numeric_to_bytes, cython
from common.models.game_server import GameServer

from .base import LoginServerPacket


@dataclass
class ServerList(LoginServerPacket):
    type: cython.char = field(default=4, init=False, repr=False)
    servers: typing.List[GameServer] = ()

    def encode(self, session):
        account = session.account
        arr = convert_numeric_to_bytes(cython.char, self.type)
        arr.extend(convert_numeric_to_bytes(cython.char, len(self.servers)))
        arr.append(
            cython.char(0 if account.last_server is None else account.last_server)
        )
        for server in self.servers:
            encoded_fields = server.encoded_fields(
                override={
                    "host": lambda field_type, field_value: bytearray(
                        [int(i) for i in field_value.split(".")]
                    )
                }
            )
            arr.extend(encoded_fields["id"])
            ip = server.host.split(".")
            arr.extend(encoded_fields["host"])
            arr.extend(encoded_fields["port"])
            arr.extend(encoded_fields["age_limit"])
            arr.extend(encoded_fields["is_pvp"])
            arr.extend(encoded_fields["online_count"])
            arr.extend(encoded_fields["max_online"])
            is_online: cython.bing = server.last_alive > time.time() - 15
            arr.extend(is_online)
            arr.extend(encoded_fields["type"])
            arr.extend(encoded_fields["brackets"])
        arr.append(0)
        return arr
