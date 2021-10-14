import common.datatypes

GAME_REQUEST_AUTH_LOGIN = common.datatypes.Int8(8)
GAME_REQUEST_CHARACTER_CREATE = common.datatypes.Int8(11)
GAME_REQUEST_CHARACTER_DELETE = common.datatypes.Int8(12)
GAME_REQUEST_NEW_CHARACTER = common.datatypes.Int8(14)
GAME_REQUEST_PROTOCOL_VERSION = common.datatypes.Int8(0)
GAME_REQUEST_CHARACTER_RESTORE = common.datatypes.Int8(98)

GAME_AUTH_LOGIN_FAIL_DEFAULT = common.datatypes.Int8(0)
GAME_AUTH_LOGIN_FAIL_SYSTEM_ERROR = common.datatypes.Int8(1)
GAME_AUTH_LOGIN_FAIL_PASSWORD_DOESNT_MATCH = common.datatypes.Int8(2)
GAME_AUTH_LOGIN_FAIL_TRY_LATER = common.datatypes.Int8(4)
GAME_AUTH_LOGIN_FAIL_CONTACT_SUPPORT = common.datatypes.Int8(5)
GAME_AUTH_LOGIN_FAIL_ALREADY_IN_USE = common.datatypes.Int8(7)

GAME_CHAR_CREATE_FAIL_DEFAULT = common.datatypes.Int32(0)
GAME_CHAR_CREATE_FAIL_TOO_MANY = common.datatypes.Int32(1)
GAME_CHAR_CREATE_FAIL_ALREADY_EXIST = common.datatypes.Int32(2)
GAME_CHAR_CREATE_FAIL_ENCODING_ERROR = common.datatypes.Int32(3)
