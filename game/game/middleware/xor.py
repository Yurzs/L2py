from common.middleware.middleware import Middleware


class XORGameMiddleware(Middleware):
    @classmethod
    def before(cls, session, request):
        with session.lock_before:
            if session.encryption_enabled:
                temp1 = Int32(0)
                for i in range(0, len(request.data)):
                    temp2 = Int32(request.data[i]) & 0xFF
                    request.data[i] = Int8(temp2 ^ session.xor_key.incoming_key[i & 15] ^ temp1)
                    temp1 = temp2
                session.xor_key.incoming_key[8:12] = Int32(
                    session.xor_key.incoming_key[8:12]
                ) + Int32(len(request.data))

    @classmethod
    def after(cls, session, response):
        with session.lock_after:
            if session.encryption_enabled:
                temp1 = Int32(0)

                for i in range(0, len(response.data)):
                    temp2 = Int32(response.data[i] & 0xFF)
                    response.data[i] = Int8(temp2 ^ session.xor_key.outgoing_key[i & 15] ^ temp1)
                    temp1 = response.data[i]

                session.xor_key.outgoing_key[8:12] = Int32(
                    session.xor_key.outgoing_key[8:12]
                ) + Int32(len(response.data))
