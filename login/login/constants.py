from common.helpers.cython import cython

REQUEST_GG_AUTH: cython.char = 7
REQUEST_SERVER_LIST: cython.char = 5
REQUEST_AUTH_LOGIN: cython.char = 0
REQUEST_SERVER_LOGIN: cython.char = 2

LOGIN_FAIL_SYSTEM_ERROR: cython.char = 1
LOGIN_FAIL_WRONG_PASSWORD: cython.char = 2
LOGIN_FAIL_WRONG_LOGIN_OR_PASSWORD: cython.char = 2
LOGIN_FAIL_ACCESS_DENIED: cython.char = 4
LOGIN_FAIL_DATABASE_ERROR: cython.char = 5
LOGIN_FAIL_ACCOUNT_ALREADY_IN_USE: cython.char = 7
LOGIN_FAIL_ACCOUNT_BANNED: cython.char = 9
LOGIN_FAIL_MAINTENANCE: cython.char = 16
LOGIN_FAIL_EXPIRED: cython.char = 18
LOGIN_FAIL_TIME_IS_UP: cython.char = 19


PLAY_FAIL_PASSWORD_MISMATCH: cython.char = 2
PLAY_FAIL_ACCESS_DENIED: cython.char = 4
PLAY_FAIL_TOO_MANY_USERS: cython.char = 15
