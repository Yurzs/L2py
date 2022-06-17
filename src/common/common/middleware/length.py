from src.common.common import exceptions
from src.common.common.ctype import ctype
from src.common.common.middleware.middleware import Middleware
from src.common.common.request import Request
from src.common.common.response import Response
from src.common.common.session import Session


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
        response.data = bytes(packet_len) + response.data
