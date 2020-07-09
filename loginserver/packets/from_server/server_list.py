from common.datatypes import Int16, Int32, Int8
from common.helpers.bytearray import ByteArray
from common.packet import add_length, add_padding
from common.utils.blowfish import blowfish_encrypt
from common.utils.checksum import add_checksum
from .base import LoginServerPacket


class ServerList(LoginServerPacket):
    type = Int8(4)

    def __init__(self, servers_dict):
        self.servers = servers_dict

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        encoded = ByteArray(self.type.encode())
        encoded.append(Int8(len(self.servers)))
        encoded.append(Int8(1))
        for server in self.servers:
            encoded.append(Int8(server.id))
            if len(server.ip.split(".")) != 4:
                ip = "0.0.0.0"
            else:
                ip = server.ip
            for sub_ip in ip.split("."):
                encoded.append(Int8(int(sub_ip)))
            encoded.append(Int32(server.port))
            encoded.append(Int8(server.age_limit))
            encoded.append(Int8(server.is_pvp))
            encoded.append(Int16(server.online))
            encoded.append(Int16(server.max_online))
            encoded.append(Int8(getattr(server, "is_online", False)))
            encoded.append(Int32(server.server_type))
            encoded.append(Int8(0))
        encoded.append(Int8(0))
        return encoded
