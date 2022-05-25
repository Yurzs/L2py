from common import exceptions
from common.middleware.middleware import Middleware
from common.request import Request
from common.response import Response
from login.packets.init import Init
from login.session import LoginSession


class ChecksumMiddleware(Middleware):
    @staticmethod
    def verify_checksum(data: bytearray) -> bool:

        if len(data) % 4 != 0:
            return False

        cdef unsigned int checksum = 0
        cdef unsigned int check
        cdef int i

        for i in range(0, len(data) - 4, 4):
            check = data[i] & 0xFF
            check |= (data[i + 1] << 8) & 0xFF00
            check |= (data[i + 2] << 0x10) & 0xFF0000
            check |= (data[i + 3] << 0x18) & 0xFF000000

            print(check, checksum)
            checksum ^= check

        check = int.from_bytes(data[-4:], "little")

        return check == checksum

    @staticmethod
    def add_checksum(response_data: bytearray):
        """Adds checksum to response."""

        cdef unsigned int checksum = 0
        cdef unsigned int check
        cdef int i

        for i in range(0, len(response_data) - 4, 4):
            check = response_data[i] & 0xFF
            check |= (response_data[i + 1] << 8) & 0xFF00
            check |= (response_data[i + 2] << 16) & 0xFF0000
            check |= (response_data[i + 3] << 24) & 0xFF000000

            checksum ^= check

        response_data[-4:] = bytearray(checksum.to_bytes(4, "little"))

    @classmethod
    def before(cls, session: LoginSession, request: Request):
        """Checks that requests checksum match."""

        if not cls.verify_checksum(request.data):
            raise exceptions.ChecksumMismatch()

    @classmethod
    def after(cls, session: LoginSession, response: Response):
        """Adds checksum to response data."""

        if not isinstance(response.packet, Init):
            cls.add_checksum(response.data)
