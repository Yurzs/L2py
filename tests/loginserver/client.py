import asyncio
from loginserver.packets.from_server import LoginServerPacket
from loginserver.packets.from_client import RequestGGAuth, RequestAuthLogin
from loginserver.client import LoginClient
from common.transport.protocol import TCPProtocol
from common.transport.packet_transport import PacketTransport
from loginserver.state import Connected, WaitingGGAccept, WaitingAuthenticationAccept


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, message, on_con_lost):
        self.loop = loop
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        self.cli = LoginClient(self)
        self.transport = PacketTransport(transport, self.cli)
        if self.message:
            transport.write(self.message)
            print('Data sent: {!r}'.format(self.message))

    @TCPProtocol.make_async
    @TCPProtocol.data_to_bytearray
    async def data_received(self, data):
        if isinstance(self.cli.state, Connected):
            self.cli.blowfish_key.key = self.cli.blowfish_key.static
            packet = LoginServerPacket.decode(data, self.cli)
            # print('Data received: {!r}'.format(data.decode()))
            print(packet)
            if packet:
                request_gg_auth = RequestGGAuth(self.cli.session_id)
                print(request_gg_auth)
                self.cli.state = WaitingGGAccept()
                self.transport.write(request_gg_auth)
                print(self.cli.__dict__)
        elif isinstance(self.cli.state, WaitingGGAccept):
            print(self.cli.state)
            packet = LoginServerPacket.decode(data, self.cli)
            req_auth = RequestAuthLogin("admin", "admin")
            self.cli.state = WaitingAuthenticationAccept()
            self.transport.write(req_auth)
        elif isinstance(self.cli.state, WaitingAuthenticationAccept):
            print(data.data)
            print(f"ohh {self.cli.state}")
            packet = LoginServerPacket.decode(data, self.cli)
            print(f"www {packet}")

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = None

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(loop, message, on_con_lost),
        '192.168.1.30', 2106)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()
