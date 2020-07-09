from common.utils.xor import xor_encrypt_login, xor_decrypt_login
import pytest
from login_server.client import LoginClient
from common.helpers.bytearray import ByteArray
import copy


@pytest.fixture()
def client():
    return LoginClient(None)


@pytest.mark.parametrize(["key", "data", "expected"], [
    (12345, ByteArray(b"V\x9b~]\t\xe5\xb4\xed\xab\xcd\xd0P\xe5\xf9j\xb5+v]\xc8\x8f'!\xfe\x14\xf1\x80\xfe\xec\x9d\xfe&\xa9\x90\x8c_z\x8e@X\xebe\x85\xb0\xaa\xbe\xdb\x8a\xacnx=\x0e\x9e\xba\xe5g\xf8\x8cG\xa1\x14\x16\x8c@Z\x19\x16\xf4V'W\x17\xabw\xa5\x00\xe7\x81l:\x8b\xf5\x10{\xa0\x04"), 805306457)
])
def test_xor_encrypt_decrypt(client, key, data, expected):

    client.xor_key._key = key

    @xor_encrypt_login
    def encrypt(packet, client, *args, **kwargs):
        return data

    @xor_decrypt_login
    def decrypt(data, client, *args, **kwargs):
        return data

    data2 = copy.deepcopy(data)

    result = encrypt(None, client)
