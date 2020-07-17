import logging

from common.transport.packet_transport import PacketTransport
from loginserver.client import LoginClient
from loginserver.packets.from_client.base import LoginClientPacket
from loginserver.packets.from_server import Init
from common.transport.protocol import TCPProtocol

LOG = logging.getLogger(f"l2py.{__name__}")


class Lineage2LoginProtocol(TCPProtocol):
    def connection_made(self, transport):
        self.client = LoginClient(self)
        self.transport = PacketTransport(transport, self.client)
        init_packet = Init(self.client)
        self.transport.write(init_packet)
        LOG.debug("New connection from %s:%s",
                  *self.transport._transport.get_extra_info("peername"))

    @TCPProtocol.make_async
    @TCPProtocol.data_to_bytearray
    async def data_received(self, data):
        packet = LoginClientPacket.decode(data, self.client)
        reply = await self.manager.proceed(self.client, packet)
        if reply:
            LOG.debug("Sending packet %s to %s:%s", reply,
                      *self.transport._transport.get_extra_info("peername"))
            self.transport.write(reply)

    def connection_lost(self, exc) -> None:
        super().connection_lost(exc)
        LOG.debug("Connection lost to %s:%s",
                  *self.transport._transport.get_extra_info("peername"))
