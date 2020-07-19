from common.utils.xor import xor_encrypt_login, xor_decrypt_login
import pytest
from loginserver.client import LoginClient
from common.helpers.bytearray import ByteArray
import copy
from common.keys.xor import LoginXorKey


@pytest.fixture()
def client():
    return LoginClient(None)


@pytest.mark.parametrize("data", [
    ByteArray(b"\x00\xFA\xFB\x00\xFA\xFB\x00\xFA\xFB\x00\xFA\xFB\x00\x00\x00\x00"
              b"\x00\xFA\xFB\x00\xFA\xFB\x00\xFA\x00\x00\x00\x00\x00\x00\x00\x00")
])
def test_xor_encrypt_decrypt(client, data):

    @xor_encrypt_login
    def encrypt(packet, client, *args, **kwargs):
        return data

    @xor_decrypt_login
    def decrypt(packet, _data, *args, **kwargs):
        return _data

    data2 = copy.deepcopy(data)

    result = encrypt(None, client)

    assert decrypt(None, result).data[:-8] == data2.data[:-8]


@pytest.mark.parametrize(["data", "result", "key"], [
    (
        "00000030390000C621982822CC88992F14FAE16F5354E96BCD778A5BD904517F6D9F7C9AD746EE5706623B9D5AC8B279EC66495FB7F7E0F38927111E77C8F3BB6203F8C5C573B16347A9DFB28F2D2EE33F5DED87FD690996013BB1B98F036C1D3F78F23BF32BACDA61834A082A5E0D2AE7B53345380DB55430A3FFEB0BC3FDD2C99E51C2F3928BB8BE29DD954E77C39CFC97ADB62007BDE0F737C902B848227231613E0987D06E2B54000000000000000000000000000000",
        "000000304B300000B25000CA93D95B3867B145E895CB64985E609214B51838B1B42499F267443A97B00634C34AE570AE10F54268047C0CD9B594EC56C4B302BF777C110F1F812B4D6635A5533FE48627D07B7BCB11F99674ECF0E125F3CCD0A4843F5DCE5D58F70A6E74EFD0130BBE28C7BED402601529C8B818646398BD64899583BADFBC22FD6EB3F38EF91526D495AB7E690957F73C40991F82A19E394F6766B395175972746166A31A4A32A31A4A32A31A4A00000000",
        12345
    )
])
def test_xor_encrypt(client, data, result, key):

    data = ByteArray(bytes.fromhex(data))
    result = ByteArray(bytes.fromhex(result))

    @xor_encrypt_login
    def _xor_encrypt(_data, _client):
        return _data

    client.xor_key = LoginXorKey(key)
    _result = _xor_encrypt(data, client)
    assert bytes(_result).hex() == bytes(result).hex()
