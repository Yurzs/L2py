import asyncio
import functools
from Cryptodome.Cipher import PKCS1_OAEP
from common.datatypes import Int

from login_server.packets.from_server import Init, LoginFail
from common.keys.rsa import L2RsaKey
from common.keys.blowfish import BlowfishKey
from login_server.client import Client
from login_server.packets import LoginClientPacket
rsa_key = L2RsaKey.generate()
blowfish_key = BlowfishKey()


def make_async(func):
    @functools.wraps(func)
    async def async_wrap(self, data):
        await func(self, data)

    @functools.wraps(func)
    def wrap(self, data):
        return asyncio.Task(async_wrap(self, data))
    return wrap


class Lineage2LoginProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.client = Client(self)
        p = Init(session_id=1234,
                 protocol_version=0xc621,
                 public_key=rsa_key.scramble_mod(),
                 blowfish_key=self.client.blowfish_key.key)
        self.transport.write(p.encoded_with_checksum)

    @make_async
    async def data_received(self, data):
        print(data[0], data[1], data[2])
        LoginClientPacket.decode(data)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        decrypted = self.client.blowfish_key.decrypt(data[3:])
        print(decrypted[0])
        cipher_rsa.decrypt(decrypted)
        e = LoginFail(1)
        self.transport.write(e.encoded)
