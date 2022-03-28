from .base import DataType

# class String(DataType, str):
#     def encode(self):
#         from common.helpers.bytearray import to_bytearray
#
#         return to_bytearray((self.value + "\0").encode("ascii"))
#
#     @classmethod
#     def decode(cls, data):
#         return cls(data.decode("ascii").replace("\0", ""))
#
#     @classmethod
#     def read(cls, data):
#         from common.helpers.bytearray import ByteArray
#
#         string = ByteArray(b"")
#         pos = 0
#         while pos < len(data):
#             if Ucython.int(data[pos : pos + 2]) != 0:
#                 string += ByteArray(data[pos : pos + 2])
#                 pos += 2
#             else:
#                 pos += 2
#                 break
#         return cls(bytes(string).decode("utf-16")), pos
#
#
# class str(bytes):
#     short_separator = int.to_bytes(0, 1, "little")
#     separator = short_separator + int.to_bytes(0, 1, "little")
#     full_separator = separator + int.to_bytes(0, 1, "little")
#
#     def encode(self):
#         from common.helpers.bytearray import to_bytearray
#
#         return to_bytearray(self.value.encode("utf-16-le") + self.separator)
#
#     @classmethod
#     def read(cls, data):
#
#         data = bytes(data)
#         splitted = data.split(cls.full_separator)
#         try:
#             return (
#                 cls((splitted[0] + cls.short_separator).decode("utf-16-le")),
#                 len(splitted[0]) + 3,
#             )
#         except UnicodeDecodeError:
#             return cls((splitted[0] + cls.separator).decode("utf-16-le")), len(splitted[0]) + 4
