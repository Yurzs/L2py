import os

from blowfish import Cipher

from common.helpers.bytearray import ByteArray


class BlowfishKey:
    static = bytes(
        b"\x6b"
        b"\x60"
        b"\xCB"
        b"\x5b"
        b"\x82"
        b"\xce"
        b"\x90"
        b"\xb1"
        b"\xcc"
        b"\x2b"
        b"\x6c"
        b"\x55"
        b"\x6c"
        b"\x6c"
        b"\x6c"
        b"\x6c"
    )

    def __init__(self, key=None):
        self.key = key if key else self.static
        self.static_encoder = Cipher(self.static, byte_order="little")

    @property
    def encoder(self):
        return Cipher(self.key, byte_order="little")

    @classmethod
    def generate(cls):
        return cls(os.urandom(16))

    def decrypt(self, data):
        return ByteArray(b"".join(self.encoder.decrypt_ecb(bytes(data))))

    def encrypt(self, data: ByteArray, static_key=False):
        if static_key:
            encrypted = ByteArray(b"".join(self.static_encoder.encrypt_ecb(bytes(data))))
        else:
            encrypted = ByteArray(b"".join(self.encoder.encrypt_ecb(bytes(data))))
        return encrypted
