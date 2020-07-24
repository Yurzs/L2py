from M2Crypto import RSA

from common.datatypes import Int8, String
from common.helpers.bytearray import ByteArray
from loginserver.packets.from_client.base import LoginClientPacket, add_padding, add_length
from loginserver.checksum import add_checksum, verify_checksum
from loginserver.crypt.blowfish import blowfish_encrypt


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

        encrypt_arr = ByteArray(b"")
        encrypt_arr.pad(128)
        encrypt_arr[0x5b] = 0x24
        enc_login = self.login.encode()
        enc_password = self.password.encode()
        encrypt_arr[0x5e: 0x5e + len(enc_login)] = enc_login
        encrypt_arr[0x6c: 0x6c + len(enc_password)] = enc_password

        key = client.rsa_key.m2crypto_key
        encrypted_login_info = key.public_encrypt(bytes(encrypt_arr), RSA.no_padding)
        arr += ByteArray(encrypted_login_info)
        arr.append(client.session_id)
        arr += ByteArray([0x23, 0x01, 0x00, 0x00, 0x67, 0x45, 0x00, 0x00, 0xab, 0x89, 0x00,
                          0x00, 0xef, 0xcd, 0x00, 0x00])
        arr += ByteArray([0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

        footer = ByteArray(b"")
        footer.pad(16)
        arr += footer

        return arr
