import asyncio
import functools

from common.helpers.bytearray import ByteArray
from common.transport.packet_transport import PacketTransport
from login_server.client import Client
from login_server.config import loop
from login_server.manager import LoginManager
from login_server.packets.from_client.base import LoginClientPacket
from login_server.packets.from_server import Init


def make_async(func):
    @functools.wraps(func)
    async def async_wrap(self, data, packet_len):
        await func(self, data, packet_len)

    @functools.wraps(func)
    def wrap(self, data):
        data = ByteArray(data)
        data.reverse()
        packet_len = data[-2:]
        data = ByteArray(data[:-2])
        return asyncio.Task(async_wrap(self, data, packet_len), loop=loop)

    return wrap


class Lineage2LoginProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.client = Client(self)
        self.transport = PacketTransport(transport, self.client)
        init_packet = Init(self.client)
        self.transport.write(init_packet)

    @make_async
    async def data_received(self, data, packet_len):
        packet = LoginClientPacket.decode(data, self.client, packet_len=packet_len)
        reply = await LoginManager.proceed(self.client, packet)
        self.transport.write(reply)
