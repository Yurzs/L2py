from common.datatypes import Bytes, Int32, Int8
from common.packet import add_length, add_padding
from common.utils.blowfish import blowfish_encrypt
from common.utils.xor import xor_encrypt_login
from login_server.packets.from_server.base import LoginServerPacket


class Init(LoginServerPacket):
    type = Int8(0)
    arg_order = ["type", "session_id", "protocol_version", "rsa_key",
                 "unknown1", "unknown2", "unknown3", "unknown4",
                 "blowfish_key", "null_termination"]

    def __init__(self, client):
        self.session_id = Int32(client.session_id)
        self.protocol_version = Int32(0x0000c621)
        self.rsa_key = Bytes(client.rsa_key.scramble_mod())
        self.unknown1 = Int32(0x29DD954E)
        self.unknown2 = Int32(0x77C39CFC)
        self.unknown3 = Int32(0x97ADB620)
        self.unknown4 = Int32(0x07BDE0F7)
        self.blowfish_key = Bytes(client.blowfish_key.key)
        self.null_termination = Int8(0)

    @add_length
    @blowfish_encrypt(init=True)
    @xor_encrypt_login
    @add_padding(xor_key=True)
    def encode(self, client):
        return self.body
