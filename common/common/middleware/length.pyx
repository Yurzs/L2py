from common import exceptions
from common.middleware.middleware import Middleware
from common.request import Request
from common.response import Response
from common.session import Session


class DataLengthMiddleware(Middleware):
    @classmethod
    def before(cls, session: Session, request: Request):
        cdef int packet_length = int.from_bytes(request.data[:2], "little")

        if packet_length != len(request.data):
            raise exceptions.RequestLengthDoesntMatch()
        request.data = request.data[2:]

    @classmethod
    def after(cls, session: Session, response: Response):
        cdef short packet_len = 2 + len(response.data)
        response.data = packet_len.to_bytes(2, "little") + response.data
