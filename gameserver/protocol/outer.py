import logging

from common.transport.protocol import TCPProtocol
from asyncio import transports
from gameserver.client import GameClient
from common.transport.packet_transport import PacketTransport
from gameserver.packets.from_client.base import GameClientPacket

LOG = logging.getLogger(f"l2py.{__name__}")


class Lineage2GameProtocol(TCPProtocol):
    def connection_made(self, transport: transports.BaseTransport) -> None:
        print("NEW CONNECTION")
        self.client = GameClient(self)
        self.transport = PacketTransport(transport, self.client)

    @TCPProtocol.make_async
    @TCPProtocol.data_to_bytearray
    async def data_received(self, data, packet_len) -> None:
        packet = GameClientPacket.decode(data, self.client, packet_len=packet_len)
        reply = await self.manager.proceed(packet)
        if reply:
            LOG.debug("Sending packet %s", packet)
            self.transport.write(reply)
