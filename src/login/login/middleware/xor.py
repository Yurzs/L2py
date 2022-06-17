from src.common.common.ctype import ctype
from src.common.common.middleware.middleware import Middleware
from src.login.login.packets.init import Init


class XORMiddleware(Middleware):
    @staticmethod
    def encrypt(data: bytearray, key: ctype.int32):
        stop = len(data) - 8
        start = 4
        ecx = key

        for pos in range(start, stop, 4):
            edx = ctype.int32(data[pos: pos + 4])

            ecx += edx
            edx ^= ecx

            data[pos : pos + 4] = bytes(edx)

        data[-8:-4] = bytes(ecx)

    @staticmethod
    def decrypt(data: bytearray, key: ctype.int32):
        stop = 2
        pos = len(data) - 12

        ecx = key

        while stop < pos:
            edx = data[pos: pos + 4]

            edx ^= ecx
            ecx -= edx

            data[pos : pos + 4] = bytes(edx)
            pos -= 4

    @classmethod
    def after(cls, session, response):
        if isinstance(response.packet, Init):
            cls.encrypt(response.data, session.xor_key.key)
