from common.middleware.middleware import Middleware


class EncryptionMiddleware(Middleware):
    @classmethod
    def before(cls, session, request):
        """Decrypts request data."""

        if session.blowfish_enabled:
            request.data = session.blowfish_key.decrypt(request.data)

    @classmethod
    def after(cls, session, response):
        """Encrypts response data."""

        response.data = session.blowfish_key.encrypt(
            response.data, static_key=not session.blowfish_enabled
        )
