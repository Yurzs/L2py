from common.middleware.middleware import Middleware
from common.response import Response
from login.session import LoginSession


class PaddingMiddleware(Middleware):
    @classmethod
    def after(cls, session: LoginSession, response: Response):
        cdef char pad_length = 4

        if not session.xor_key.initiated:
            pad_length += 4
            session.xor_key.initiated = True

        pad_length += 8 - (len(response.data) + pad_length) % 8
        response.data.extend(b"\x00" * pad_length)
