from common import exceptions
from common.ctype import ctype
from common.middleware.middleware import Middleware
from common.request import Request
from common.response import Response
from common.session import Session


class DataLengthMiddleware(Middleware):
    @classmethod
    def before(cls, session: Session, request: Request):
        packet_length = ctype.uint16(request.data[:2])

        if packet_length != len(request.data):
            raise exceptions.RequestLengthDoesntMatch()
        request.data = request.data[2:]

    @classmethod
    def after(cls, session: Session, response: Response):
        packet_len = ctype.int16(2 + len(response.data))
        response.data = bytearray(bytes(packet_len) + response.data)
