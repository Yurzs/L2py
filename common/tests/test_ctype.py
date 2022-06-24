from common.ctype import ctype


def test_ctypes():
    """
    This test check if all ctypes attributes present,
    do they properly work and named.
    """

    c_types = [eval(f"ctype.{i}") for i in dir(ctype) if i[0:2] != "__"]
    assert len(c_types) == 21, "Amount of types are changed, convert_dict should be updated or ctypes restored."

    convert_dict = {"int": (2_147_483_647, 2_147_483_647),
                    "int8": (127, 127),
                    "int16": (32767, 32767),
                    "int32": (2_147_483_647, 2_147_483_647),
                    "int64": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    "uint": (2_147_483_647, 2_147_483_647),
                    "uint8": (255, 255),
                    "uint16": (32767, 32767),
                    "uint32": (2_147_483_647, 2_147_483_647),
                    "uint64": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    "bool": (1, True),
                    "byte": (10000, 16),
                    "char": (bytes(1), b'\x00'),
                    "double": (2.000000000000001, 2.000000000000001),
                    "float": (2.000001, 2.0000009536743164),
                    "short": (10000, 10000),
                    "long": (-2147483647, -2147483647),
                    "longlong": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    "ushort": (10000, 10000),
                    "ulong": (2147483647, 2147483647),
                    "ulonglong": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    }

    for key in convert_dict:
        value = eval(f"ctype.{key}({convert_dict[key][0]})")
        assert convert_dict[key][1] == value, f"{key}: {convert_dict[key][1]} != {value}"
