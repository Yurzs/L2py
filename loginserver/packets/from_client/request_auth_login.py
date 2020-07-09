from M2Crypto import RSA

from common.datatypes import Int8, String
from common.helpers.bytearray import ByteArray
from loginserver.packets.from_client.base import LoginClientPacket


class RequestAuthLogin(LoginClientPacket):
    type = Int8(0)

    def __init__(self, login, password):
        self.login = String(login)
        self.password = String(password)

    @classmethod
    def parse(cls, data: ByteArray, client: "LoginClient"):
        data = ByteArray(data[1:])
        encrypted = ByteArray(data[0:128])
        key = client.rsa_key.m2crypto_key
        decrypt = key.private_decrypt(bytes(encrypted), RSA.no_padding)
        login = decrypt[94:107]
        password = decrypt[108:124]
        return cls(String.decode(login), String.decode(password))
