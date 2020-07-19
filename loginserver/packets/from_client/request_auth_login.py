from M2Crypto import RSA

from common.datatypes import Int8, String
from common.helpers.bytearray import ByteArray
from loginserver.packets.from_client.base import LoginClientPacket, add_padding, add_length
from common.utils.checksum import verify_checksum, add_checksum
from common.utils.blowfish import blowfish_encrypt

class RequestAuthLogin(LoginClientPacket):
    type = Int8(0)
    arg_order = ["type", "login", "password"]

    def __init__(self, login, password):
        self.login = String(login)
        self.password = String(password)

    @classmethod
    @verify_checksum
    def parse(cls, data: ByteArray, client: "LoginClient"):
        data = ByteArray(data[1:])
        encrypted = ByteArray(data[0:128])
        key = client.rsa_key.m2crypto_key
        decrypt = key.private_decrypt(bytes(encrypted), RSA.no_padding)
        login = decrypt[94:107]
        password = decrypt[108:124]
        return cls(String.decode(login), String.decode(password))

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        arr = ByteArray(self.type.encode())
        arr.pad(123)
        key = client.rsa_key.m2crypto_key
        encrypted_login = key.public_encrypt(bytes(self.login.encode()), RSA.no_padding)
        encrypted_password = key.public_encrypt(bytes(self.password.encode()), RSA.no_padding)
        arr[94:107] = encrypted_login
        arr[108:124] = encrypted_password
        return arr
