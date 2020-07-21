from common.manager import PacketManager
from gameserver import state, packets


class GameServerPacketManager(PacketManager):

    @classmethod
    async def proceed(cls, packet, client: "GameClient"):
        if isinstance(client.state, state.Connected) and \
                isinstance(packet, packets.from_client.ProtocolVersion):
            if packet.protocol_version != 746 and packet.protocol_version != 251:
                reply = packets.from_server.CryptInit(client.xor_key.outgoing_key, 0)
                client.protocol.transport.write(reply)
                client.protocol.transport.close()
                return
            elif packet.protocol_version == -1:
                reply = packets.from_server.CryptInit(client.xor_key.outgoing_key, 0)
                client.protocol.transport.write(reply)
                client.protocol.transport.close()
                return
            else:
                reply = packets.from_server.CryptInit(client.xor_key.outgoing_key, 1)
                client.protocol.transport.write(reply)
                client.encryption_enabled = True
                return
        print(packet)
