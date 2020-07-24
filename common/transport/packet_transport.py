from common.packet import Packet


class PacketTransport:

    def __init__(self, transport, client):
        self._transport = transport
        self.client = client

    def write(self, packet: Packet):
        result = packet.encode(self.client)
        return self._transport.write(bytes(result))

    def close(self):
        return self._transport.close()
