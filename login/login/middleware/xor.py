from common.helpers.bytearray import ByteArray
from common.middleware.middleware import Middleware
from login.packets.init import Init


class XORMiddleware(Middleware):
    @staticmethod
    def encrypt(data: ByteArray, key):
        stop = len(data) - 8
        start = 4
        ecx = Int32(key)

        for pos in range(start, stop, 4):
            edx = Int32(data[pos]) & 255
            edx |= (Int32(data[pos + 1]) & 255) << 8
            edx |= (Int32(data[pos + 2]) & 255) << 16
            edx |= (Int32(data[pos + 3]) & 255) << 24

            ecx += edx
            edx ^= ecx

            data[pos : pos + 4] = edx

        data[-8:-4] = ecx

    @staticmethod
    def decrypt(data, key):
        stop = 2
        pos = len(data) - 12
        ecx = Int32(key)

        while stop < pos:
            edx = Int32(data[pos]) & 255
            edx |= (Int32(data[pos + 1]) & 255) << 8
            edx |= (Int32(data[pos + 2]) & 255) << 16
            edx |= (Int32(data[pos + 3]) & 255) << 24

            edx ^= ecx
            ecx -= edx

            data[pos : pos + 4] = edx
            pos -= 4

    @classmethod
    def after(cls, session, response):
        if isinstance(response.packet, Init):
            cls.encrypt(response.data, session.xor_key.key)
