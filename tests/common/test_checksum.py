import pytest
import os

from common.helpers.bytearray import ByteArray
from loginserver.checksum import add_checksum, verify_checksum


@pytest.mark.parametrize(["data", "result"], [
    (
        "0B00001D83000000000000000000000000000000000000000000000000000000",
        "0B00001D8300000000000000000000000000000000000000000000008800001D"
    ),
    (
        "03475F60D412923F6B0000000000000000000003EA0000000000000000000000000000000000000000000000000000000000000000000000",
        "03475F60D412923F6B0000000000000000000003EA000000000000000000000000000000000000000000000000000000000000005655CD5C"
    )
])
def test_add_checksum(data, result):

    data = ByteArray(bytes.fromhex(data))
    result = ByteArray(bytes.fromhex(result))

    @add_checksum
    def _add_checksum(_data):
        return _data

    assert _add_checksum(data) == result


@pytest.mark.parametrize("data", [
    "0B00001D8300000000000000000000000000000000000000000000008800001D",
    "03475F60D412923F6B0000000000000000000003EA000000000000000000000000000000000000000000000000000000000000005655CD5C",
])
def test_verify_checksum(data):

    data = ByteArray(bytes.fromhex(data))

    @verify_checksum
    def _verify_checksum(packet, _data, *args):
        return _data

    assert _verify_checksum(None, data) is not None
