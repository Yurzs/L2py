from common.transport.packet_transport import PacketTransport
from loginserver.client import LoginClient
from loginserver.packets.from_client.base import LoginClientPacket
from loginserver.packets.from_server import Init
from common.transport.protocol import TCPProtocol


class Lineage2LoginProtocol(TCPProtocol):
    def connection_made(self, transport):
        self.client = LoginClient(self)
        self.transport = PacketTransport(transport, self.client)
        init_packet = Init(self.client)
        self.transport.write(init_packet)

    @TCPProtocol.make_async
    @TCPProtocol.data_to_bytearray
    async def data_received(self, data):
        packet = LoginClientPacket.decode(data, self.client)
        reply = await self.manager.proceed(self.client, packet)
        if reply:
            self.transport.write(reply)
