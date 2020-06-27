from login_server.packets.from_client.base import LoginClientPacket


class RequestAuthLogin(LoginClientPacket):
    type = 0

    @classmethod
    def parse(cls, packet_len, packet_type, data):
        print(packet_type, packet_len, data)
