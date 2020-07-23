from common.manager import PacketManager
from gameserver import packets, state
from gameserver.api import LoginClient


class GameServerPacketManager(PacketManager):

    @classmethod
    async def proceed(cls, packet, client: "GameClient"):
        if (isinstance(client.state, state.Connected) and
                isinstance(packet, packets.from_client.ProtocolVersion)):
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
                client.state = state.WaitingAuthentication()
                return
        elif (isinstance(client.state, state.WaitingAuthentication) and
              isinstance(packet, packets.from_client.RequestAuthLogin)):
            login_client = LoginClient()
            if await login_client.auth_login(packet.login,
                                             packet.login_ok1, packet.login_ok2,
                                             packet.play_ok1, packet.play_ok2):
                char_list = packets.from_server.CharList([])
                client.state = state.WaitingCharacterSelect()
                return char_list
        elif (isinstance(client.state, state.WaitingCharacterSelect) and
              isinstance(packet, packets.from_client.NewCharacter)):
            pass  # TODO
