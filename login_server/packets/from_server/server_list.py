from .base import LoginServerPacket, add_length, add_padding
from common.utils.blowfish import blowfish_encrypt
from common.datatypes import Int32, Int8, Int16
from common.helpers.bytearray import ByteArray


class ServerList(LoginServerPacket):
    type = Int8(4)

    def __init__(self, servers_dict):
        self.servers = servers_dict

    @add_length
    @blowfish_encrypt()
    @add_padding()
    def encode(self, client):
        encoded = ByteArray(self.type.encode())
        encoded.append(Int8(len(self.servers)))
        encoded.append(Int8(0))
        for server in self.servers:
            encoded.append(Int8(server.id))
            encoded.append(Int32(server.ip))
            encoded.append(Int32(server.port))
            encoded.append(Int8(server.age_limit))
            encoded.append(Int8(server.is_pvp))
            encoded.append(Int16(server.online))
            encoded.append(Int16(server.max_online))
            encoded.append(Int8(server.is_test))
            encoded.append(Int8(0))
        return encoded
