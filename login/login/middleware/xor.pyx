import cython

from common.middleware.middleware import Middleware
from login.packets.init import Init


class XORMiddleware(Middleware):
    @staticmethod
    def encrypt(data: bytearray, key: cython.int):
        cdef short stop = len(data) - 8
        cdef short start = 4
        cdef int ecx = key
        cdef short pos
        cdef int edx

        for pos in range(start, stop, 4):
            edx = data[pos] & 255
            edx |= (data[pos + 1] & 255) << 8
            edx |= (data[pos + 2] & 255) << 16
            edx |= (data[pos + 3] & 255) << 24

            ecx += edx
            edx ^= ecx

            data[pos : pos + 4] = edx.to_bytes(4, "little", signed=True)

        data[-8:-4] = ecx.to_bytes(4, "little", signed=True)

    @staticmethod
    def decrypt(data: bytearray, key: cython.int):
        cdef short stop = 2
        cdef short pos = len(data) - 12

        cdef int ecx = key
        cdef int edx

        while stop < pos:
            edx = data[pos] & 255
            edx |= (data[pos + 1] & 255) << 8
            edx |= (data[pos + 2] & 255) << 16
            edx |= (data[pos + 3] & 255) << 24

            edx ^= ecx
            ecx -= edx

            data[pos : pos + 4] = edx
            pos -= 4

    @classmethod
    def after(cls, session, response):
        if isinstance(response.packet, Init):
            cls.encrypt(response.data, session.xor_key.key)
