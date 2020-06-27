import os
from common.datatypes import Bytes
from Cryptodome.Cipher import Blowfish


class BlowfishKey:

    static = bytes(
        b"\x6b" +
        b"\x60" +
        b"\xCB" +
        b"\x5b" +
        b"\x82" +
        b"\xce" +
        b"\x90" +
        b"\xb1" +
        b"\xcc" +
        b"\x2b" +
        b"\x6c" +
        b"\x55" +
        b"\x6c" +
        b"\x6c" +
        b"\x6c" +
        b"\x6c"
    )

    def __init__(self, key=None):
        self.key = key or self.static
        self.decoder = Blowfish.new(key or self.static, Blowfish.MODE_CBC)
        self.encoder = Blowfish.new(key or self.static, Blowfish.MODE_CBC)

    @classmethod
    def generate(cls):
        return cls(os.urandom(16))

    def decrypt(self, data):
        pad_len = (8 - (len(data) % 8)) % 8
        return self.decoder.decrypt(data + pad_len * b"\x00")

    def encrypt(self, data):
        return self.encoder.encrypt(data)
