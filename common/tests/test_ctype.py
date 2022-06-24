from common.ctype import ctype


def test_types():
    c_types = [eval(f"ctype.{i}") for i in dir(ctype) if i[0:2] != "__"]

    convert_dict = {"bool": (1, True),
                    "byte": (10000, 16),
                    "ubyte": (10000, 16),
                    "char": (bytes(1), b'\x00'),
                    "double": (2.000000000000001, 2.000000000000001),
                    "float": (2.000001, 2.0000009536743164),
                    "long": (-2147483647, -2147483647),  # TODO: incorrect value
                    "short": (10000, 10000),
                    "longlong": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    "ulonglong": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    "ulong": (2147483647, 2147483647),
                    "ushort": (10000, 10000),
                    "int": (2_147_483_647, 2_147_483_647),
                    "int8": (127, 127),
                    "int16": (32767, 32767),
                    "int32": (2_147_483_647, 2_147_483_647),
                    "int64": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    "uint": (2_147_483_647, 2_147_483_647),
                    "uint8": (255, 255),
                    "uint16": (32767, 32767),
                    "uint32": (2_147_483_647, 2_147_483_647),
                    "uint64": (9_223_372_036_854_775_807, 9_223_372_036_854_775_807),
                    }

    for c_type_i in c_types:
        type_name = c_type_i.__name__
        value = c_type_i(convert_dict[type_name][0])
        assert convert_dict[type_name][1] == value, f"{type_name}: {convert_dict[type_name][1]} != {value}"
