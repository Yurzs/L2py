from common.middleware.middleware import Middleware


class PaddingMiddleware(Middleware):
    @classmethod
    def after(cls, session, response):
        pad_length = 4
        if not session.xor_key.initiated:
            pad_length += 4
            session.xor_key.initiated = True
        pad_length += 8 - (len(response.data) + pad_length) % 8
        response.data.pad(pad_length)
