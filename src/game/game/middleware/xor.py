import src.game.game.session as session
from src.common.common.ctype import ctype
from src.common.common.middleware.middleware import Middleware
from src.common.common.response import Response


class XORGameMiddleware(Middleware):
    @classmethod
    def before(cls, session: session.GameSession, request: Response):
        with session.lock_before:
            if session.encryption_enabled:
                temp1 = ctype.uint32(0)

                for i in range(0, len(request.data)):
                    temp2 = ctype.uint8(request.data[i])
                    request.data[i] = int(temp2 ^ session.xor_key.incoming_key[i & 15] ^ temp1)
                    temp1 = temp2
                key_chunk = ctype.uint32(session.xor_key.incoming_key[8:12])
                key_chunk += len(request.data)
                session.xor_key.incoming_key[8:12] = bytes(key_chunk)

    @classmethod
    def after(cls, session: session.GameSession, response: Response):
        with session.lock_after:
            if session.encryption_enabled:
                temp1 = ctype.uint32(0)

                for i in range(0, len(response.data)):
                    temp2 = ctype.uint8(response.data[i])
                    response.data[i] = int(temp2 ^ session.xor_key.outgoing_key[i & 15] ^ temp1)
                    temp1 = response.data[i]

                key_chunk = ctype.uint32(session.xor_key.outgoing_key[8:12])
                key_chunk += len(response.data)
                session.xor_key.outgoing_key[8:12] = bytes(key_chunk)
