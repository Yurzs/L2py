from src.common.common import exceptions
from src.common.common.ctype import ctype
from src.common.common.middleware.middleware import Middleware
from src.common.common.request import Request
from src.common.common.response import Response
from src.login.login.packets.init import Init
from src.login.login.session import LoginSession


class ChecksumMiddleware(Middleware):
    @staticmethod
    def verify_checksum(data: bytearray) -> bool:

        if len(data) % 4 != 0:
            return False

        checksum = ctype.int32(0)

        for i in range(0, len(data) - 4, 4):
            checksum ^= ctype.int32(data[i: i + 4])

        check = ctype.int32(data[-4:])

        return check == checksum

    @staticmethod
    def add_checksum(response_data: bytearray):
        """Adds checksum to response."""

        checksum = ctype.int32(0)

        for i in range(0, len(response_data) - 4, 4):
            checksum ^= ctype.int32(response_data[i: i + 4])

        response_data[-4:] = bytearray(bytes(checksum))

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
