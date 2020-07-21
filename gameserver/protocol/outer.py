import logging

from common.transport.protocol import TCPProtocol
from asyncio import transports
from gameserver.client import GameClient
from common.transport.packet_transport import PacketTransport
from gameserver.packets.from_client.base import GameClientPacket

LOG = logging.getLogger(f"l2py.{__name__}")


class Lineage2GameProtocol(TCPProtocol):
    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.client = GameClient(self)
        self.transport = PacketTransport(transport, self.client)

    @TCPProtocol.make_async
    @TCPProtocol.data_to_bytearray
    async def data_received(self, data) -> None:
        packet = GameClientPacket.decode(data, self.client)
        reply = await self.manager.proceed(packet, self.client)
        if reply:
            LOG.debug("Sending packet %s", packet)
            self.transport.write(reply)
