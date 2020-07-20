import os
os.environ["MONGO_URI"] = "localhost"

from loginserver.packets.from_server.base import LoginServerPacket
from common.utils.xor import xor_encrypt_login, xor_decrypt_login
import pytest
from loginserver.client import LoginClient
from common.helpers.bytearray import ByteArray
import copy
from common.keys.xor import LoginXorKey
from loginserver.packets.from_server import Init


@pytest.fixture()
def client():
    return LoginClient(None)


def test_Init_encrypt_decrypt(client):
    out = Init(client).encode(client)
    session_id = client.session_id
    blowfish_key = client.blowfish_key.key

    client.blowfish_key.key = client.blowfish_key.static
    LoginServerPacket.decode(ByteArray(out[2:]), client)
    assert client.blowfish_key.key == blowfish_key
    assert client.session_id == session_id

