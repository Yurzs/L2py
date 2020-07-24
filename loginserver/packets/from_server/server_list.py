import typing

from common.datatypes import Int16, Int32, Int8
from common.helpers.bytearray import ByteArray
from common.packet import add_length, add_padding
from loginserver.crypt.blowfish import blowfish_encrypt
from loginserver.checksum import add_checksum
from loginserver.models.game_server import GameServer
from .base import LoginServerPacket


class ServerList(LoginServerPacket):
    type = Int8(4)

    def __init__(self, servers_list: typing.List[GameServer] = None):
        self.servers = servers_list if servers_list is not None else []

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        arr = ByteArray(self.type.encode())
        arr.append(Int8(len(self.servers)))
        arr.append(Int8(client.account.latest_server))
        for server in self.servers:
            arr.extend(Int8(server.id))
            arr.append(Int8(server.ip[0]))
            arr.append(Int8(server.ip[1]))
            arr.append(Int8(server.ip[2]))
            arr.append(Int8(server.ip[3]))
            arr.append(Int32(server.port))
            arr.append(Int8(server.age_limit))
            arr.append(Int8(server.is_pvp))
            arr.append(Int16(server.online))
            arr.append(Int16(server.max_online))
            arr.append(Int8(server.is_online))
            arr.append(Int32(server.server_type))
            arr.append(Int8(server.brackets))
        arr.append(Int8(0))
        return arr
