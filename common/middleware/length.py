from common import exceptions
from common.datatypes import Int16
from common.middleware.middleware import Middleware
from common.request import Request
from common.response import Response
from login.session import LoginSession


class DataLengthMiddleware(Middleware):
    @classmethod
    def before(cls, session: LoginSession, request: Request):
        packet_length = Int16.decode(request.data[:2]) - 2
        if packet_length == len(request.data):
            raise exceptions.RequestLengthDoesntMatch()
        request.data = request.data[2:]

    @classmethod
    def after(cls, session: LoginSession, response: Response):
        response.data = Int16(2 + len(response.data)).encode() + response.data
