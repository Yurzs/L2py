from common.datatypes import Int8, Int32
from common.middleware.middleware import Middleware


class XORGameMiddleware(Middleware):
    @classmethod
    def before(cls, session, request):
        if session.encryption_enabled:

            temp1 = Int32(0)
            for i in range(0, len(request.data)):
                temp2 = Int32(request.data[i]) & 0xFF
                request.data[i] = Int8(
                    temp2 ^ session.xor_key.incoming_key[i & 15] ^ temp1
                )
                temp1 = temp2

            old = Int32(session.xor_key.incoming_key[8]) & 0xFF
            old |= (Int32(session.xor_key.incoming_key[9]) << 0x08) & 0xFF00
            old |= (Int32(session.xor_key.incoming_key[10]) << 0x10) & 0xFF0000
            old |= (Int32(session.xor_key.incoming_key[11]) << 0x18) & 0xFF000000

            old += Int32(len(request.data))

            session.xor_key.incoming_key[8:12] = old

    @classmethod
    def after(cls, session, response):
        if session.encryption_enabled:

            temp1 = Int32(0)

            for i in range(0, len(response.data)):
                temp2 = Int32(response.data[i] & 0xFF)
                response.data[i] = Int8(
                    temp2 ^ session.xor_key.outgoing_key[i & 15] ^ temp1
                )
                temp1 = response.data[i]

            old = Int32(session.xor_key.outgoing_key[8]) & 0xFF
            old |= (Int32(session.xor_key.outgoing_key[9]) << 0x08) & 0xFF00
            old |= (Int32(session.xor_key.outgoing_key[10]) << 0x10) & 0xFF0000
            old |= (Int32(session.xor_key.outgoing_key[11]) << 0x18) & 0xFF000000

            old += Int32(len(response.data))

            session.xor_key.outgoing_key[8:12] = old
