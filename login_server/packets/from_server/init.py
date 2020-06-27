from login_server.packets.from_server.base import LoginServerPacket
from common.datatypes import Int, String, Char, Bytes
from collections import OrderedDict
from common.keys.blowfish import BlowfishKey
from common.keys.rsa import L2RsaKey


class Init(LoginServerPacket):
    type = 0

    def __init__(self, session_id,
                 protocol_version,
                 public_key,
                 blowfish_key):
        self.data = OrderedDict([
            ("session_id", Int(session_id)),
            ("protocol_version", Int(protocol_version)),
            ("public_key", Bytes(public_key)),
            ("unknown", Bytes(
                b"\x29\xDD\x95\x4E" +
                b"\x77\xC3\x9C\xFC" +
                b"\x97\xAD\xB6\x20" +
                b"\x07\xBD\xE0\xF7")),
            ("blowfish_key", Bytes(blowfish_key)),
            ("null_termination", Char(0))
        ])

    @classmethod
    def parse(cls, packet_len, packet_type, data):
        return cls(
            Int.decode(data[0:4]),
            Int.decode(data[4:8]),
            String.decode(data[8:24]),
            String.decode(data[24:40])
        )
