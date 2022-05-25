from Cryptodome.PublicKey import RSA


class L2RsaKey(RSA.RsaKey):
    def scramble_mod(self) -> bytes:
        n = bytearray(self.n_bytes)

        # step 1: 0x4d - 0x50 <-> 0x00 - 0x04
        for i in range(4):
            n[i], n[0x4D + i] = n[0x4D + i], n[i]

        # step 2 : xor first 0x40 bytes with  last 0x40 bytes
        for i in range(0x40):
            n[i] = n[i] ^ n[0x40 + i]

        # step 3 : xor bytes 0x0d-0x10 with bytes 0x34-0x38
        for i in range(4):
            n[0x0D + i] = n[0x0D + i] ^ n[0x34 + i]

        # step 4 : xor last 0x40 bytes with first 0x40 bytes
        for i in range(0x40):
            n[0x40 + i] = n[0x40 + i] ^ n[i]

        return bytes(n)

    @classmethod
    def unscramble_mod(cls, n: bytearray) -> int:

        for i in range(0x40):
            n[0x40 + i] = n[0x40 + i] ^ n[i]

        for i in range(4):
            n[0x0D + i] = n[0x0D + i] ^ n[0x34 + i]

        for i in range(0x40):
            n[i] = n[i] ^ n[0x40 + i]

        for i in range(4):
            temp = n[0x00 + i]
            n[0x00 + i] = n[0x4D + i]
            n[0x4D + i] = temp

        return int.from_bytes(bytes(n), "big")

    @property
    def n_bytes(self):
        return self.n.to_bytes(128, "big")

    @classmethod
    def generate(cls, bits=1024, randfunc=None, e=65537) -> "L2RsaKey":
        key = RSA.generate(bits, randfunc, e)
        key.__class__ = cls
        return key

    def __repr__(self):
        return "L2" + super().__repr__()

    def private_decrypt(self, data: bytearray):
        cipher_int = int.from_bytes(data, "big")
        plain_int = pow(cipher_int, self.d, self.n)
        return plain_int.to_bytes((self.n.bit_length() - 1) // 8 + 1, "big")
