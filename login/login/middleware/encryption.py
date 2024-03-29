from common.middleware.middleware import Middleware
from common.request import Request
from common.response import Response
from login.session import LoginSession


class EncryptionMiddleware(Middleware):
    @classmethod
    def before(cls, session: LoginSession, request: Request):
        """Decrypts request data."""

        if session.blowfish_enabled:
            request.data = session.blowfish_key.decrypt(request.data)

    @classmethod
    def after(cls, session: LoginSession, response: Response):
        """Encrypts response data."""

        response.data = session.blowfish_key.encrypt(
            response.data, static_key=not session.blowfish_enabled
        )
