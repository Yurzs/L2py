import math
import struct
from Cryptodome.PublicKey import RSA


class L2RsaKey(RSA.RsaKey):

    def scramble_mod(self) -> bytes:
        n = self.n
        n = n.to_bytes(math.ceil(n.bit_length() / 8), "big")
        n = list(struct.unpack("!{}".format("b" * len(n)), n))

        # step 1: 0x4d - 0x50 <-> 0x00 - 0x04
        for i in range(4):
            n[i], n[0x4d + i] = n[0x4d + i], n[i]

        # step 2 : xor first 0x40 bytes with  last 0x40 bytes
        for i in range(0x40):
            n[i] = n[i] ^ n[0x40 + i]

        # step 3 : xor bytes 0x0d-0x10 with bytes 0x34-0x38
        for i in range(4):
            n[0x0d + i] = n[0x0d + i] ^ n[0x34 + i]

        # step 4 : xor last 0x40 bytes with first 0x40 bytes
        for i in range(0x40):
            n[0x40 + i] = n[0x40 + i] ^ n[i]

        return struct.pack("!{}".format("b" * len(n)), *n)

    @classmethod
    def unscramble_mod(cls, n: bytes) -> int:
        n = list(struct.unpack("!{}".format("b" * len(n)), n))

        for i in range(0x40):
            n[0x40 + i] = n[0x40 + i] ^ n[i]

        for i in range(4):
            n[0x0d + i] = n[0x0d + i] ^ n[0x34 + i]

        for i in range(0x40):
            n[i] = n[i] ^ n[0x40 + i]

        for i in range(4):
            temp = n[0x00 + i]
            n[0x00 + i] = n[0x4d + i]
            n[0x4d + i] = temp

        return int.from_bytes(struct.pack("!{}".format("b" * len(n)), *n), "big")

    @classmethod
    def from_scrambled(cls, data) -> "L2RsaKey":
        modulus = cls.unscramble_mod(data)
        key = RSA.construct((modulus, 65537))
        key.__class__ = L2RsaKey
        return key

    @classmethod
    def generate(cls, bits=1024, randfunc=None, e=65537) -> "L2RsaKey":
        key = RSA.generate(bits, randfunc, e)
        key.__class__ = cls
        return key

    def __repr__(self):
        return "L2" + super().__repr__()
