from common import exceptions
from common.middleware.middleware import Middleware
from login.packets.init import Init


class ChecksumMiddleware(Middleware):
    @staticmethod
    def verify_checksum(data):
        if len(data) % 4 != 0:
            return False

        checksum = Int32(0)
        for i in range(0, len(data) - 4, 4):
            check = Int32(data[i]) & 0xFF
            check |= Int32(data[i + 1]) << 8 & 0xFF00
            check |= Int32(data[i + 2]) << 0x10 & 0xFF0000
            check |= Int32(data[i + 3]) << 0x18 & 0xFF000000

            checksum ^= check

        check = Int32(data[-4:])

        return check == checksum

    @staticmethod
    def add_checksum(response_data):
        """Adds checksum to response."""

        checksum = Int32(0)

        for i in range(0, len(response_data) - 4, 4):
            check = Int32(response_data[i]) & 0xFF
            check |= Int32(response_data[i + 1]) << 8 & 0xFF00
            check |= Int32(response_data[i + 2]) << 0x10 & 0xFF0000
            check |= Int32(response_data[i + 3]) << 0x18 & 0xFF000000

            checksum ^= check

        response_data[-4:] = checksum

    @classmethod
    def before(cls, session, request):
        """Checks that requests checksum match."""

        if not cls.verify_checksum(request.data):
            raise exceptions.ChecksumMismatch()

    @classmethod
    def after(cls, client, response):
        """Adds checksum to response data."""

        if not isinstance(response.packet, Init):
            cls.add_checksum(response.data)
