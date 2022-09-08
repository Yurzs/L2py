GAME_REQUEST_AUTH_LOGIN = 8
GAME_REQUEST_CHARACTER_CREATE = 11
GAME_REQUEST_CHARACTER_DELETE = 12
GAME_REQUEST_NEW_CHARACTER = 14
GAME_REQUEST_PROTOCOL_VERSION = 0
GAME_REQUEST_CHARACTER_RESTORE = 98
GAME_REQUEST_CHARACTER_SELECTED = 13
GAME_REQUEST_ENTER_WORLD = 3
GAME_REQUEST_MOVE_BACK_TO_LOCATION = 1
GAME_REQUEST_RESTART = 70
GAME_REQUEST_SAY2 = 56
GAME_REQUEST_ACTION = 4
GAME_REQUEST_TARGET_CANCEL = 55
GAME_REQUEST_ATTACK = 10
GAME_REQUEST_OPEN_MINIMAP = 205
GAME_REQUEST_ACTION_USE = 69
GAME_REQUEST_SOCIAL_ACTION = 27
GAME_REQUEST_VALIDATE_POSITION = 72
GAME_REQUEST_JOIN_PARTY = 41
GAME_REQUEST_WITHDRAW_PARTY = 43
GAME_REQUEST_KICK_PARTY_MEMBER = 44
GAME_REQUEST_PARTY_MATCH_CONFIG = 111
GAME_REQUEST_HAND_OVER_PARTY_LEADER = 208
GAME_REQUEST_ASK_JOIN_MPCC = 208
GAME_REQUEST_GROUP_DUEL = 208
GAME_REQUEST_MAKE_MACRO = 193
GAME_REQUEST_DELETE_MACRO = 194
GAME_REQUEST_FRIEND_INVITE = 94
GAME_REQUEST_FRIEND_INVITE_ANSWER = 95
GAME_REQUEST_FRIEND_MESSAGE = 204
GAME_REQUEST_FRIEND_DELETE = 97

GAME_REQUEST_SHORTCUT_REG = 51  # 0x33

GAME_AUTH_LOGIN_FAIL_DEFAULT = 0
GAME_AUTH_LOGIN_FAIL_SYSTEM_ERROR = 1
GAME_AUTH_LOGIN_FAIL_PASSWORD_DOESNT_MATCH = 2
GAME_AUTH_LOGIN_FAIL_TRY_LATER = 4
GAME_AUTH_LOGIN_FAIL_CONTACT_SUPPORT = 5
GAME_AUTH_LOGIN_FAIL_ALREADY_IN_USE = 7

GAME_CHAR_CREATE_FAIL_DEFAULT = 0
GAME_CHAR_CREATE_FAIL_TOO_MANY = 1
GAME_CHAR_CREATE_FAIL_ALREADY_EXIST = 2
GAME_CHAR_CREATE_FAIL_ENCODING_ERROR = 3

BODY_PART_HEAD = "head"
BODY_PART_HEAD_ALL = "dhead"
BODY_PART_FACE = "face"
BODY_PART_HAIR = "hair"
BODY_PART_DHAIR = "dhair"
BODY_PART_LEFT_EAR = "lear"
BODY_PART_RIGHT_EAR = "rear"
BODY_PART_NECK = "neck"
BODY_PART_LEFT_FINGER = "lfinger"
BODY_PART_RIGHT_FINGER = "rfinger"
BODY_PART_GLOVES = "gloves"
BODY_PART_CHEST = "chest"
BODY_PART_LEGS = "legs"
BODY_PART_FEET = "feet"
BODY_PART_FULL_ARMOR = "fullarmor"
BODY_PART_UNDERWEAR = "underwear"
BODY_PART_WOLF = "wolf"
BODY_PART_HATCHLING = "hatchling"
BODY_PART_STRIDER = "strider"
BODY_PART_BABY_PET = "babypet"

ALL_BODY_PARTS = [
    BODY_PART_HEAD,
    BODY_PART_HEAD_ALL,
    BODY_PART_FACE,
    BODY_PART_HAIR,
    BODY_PART_DHAIR,
    BODY_PART_LEFT_EAR,
    BODY_PART_RIGHT_EAR,
    BODY_PART_NECK,
    BODY_PART_LEFT_FINGER,
    BODY_PART_RIGHT_FINGER,
    BODY_PART_GLOVES,
    BODY_PART_CHEST,
    BODY_PART_LEGS,
    BODY_PART_FEET,
    BODY_PART_FULL_ARMOR,
    BODY_PART_UNDERWEAR,
    BODY_PART_WOLF,
    BODY_PART_HATCHLING,
    BODY_PART_STRIDER,
    BODY_PART_BABY_PET,
]

ARMOR_TYPE_LIGHT = "light"
ARMOR_TYPE_HEAVY = "heavy"

ACTION_TARGET = 0
ACTION_TARGET_SHIFT = 1
ACTION_SIT = 0
ACTION_RUN = 1
ACTION_FAKE_DEATH_START = 2
ACTION_FAKE_DEATH_STOP = 3
ACTION_COMMON_CRAFT = 51

SOCIAL_ACTION_HELLO = 2
SOCIAL_ACTION_VICTORY = 3
SOCIAL_ACTION_ADVANCE = 4
SOCIAL_ACTION_NO = 5
SOCIAL_ACTION_YES = 6
SOCIAL_ACTION_BOW = 7
SOCIAL_ACTION_UNAWARE = 8
SOCIAL_ACTION_WAITING = 9
SOCIAL_ACTION_LAUGH = 10
SOCIAL_ACTION_APPLAUD = 11
SOCIAL_ACTION_DANCE = 12
SOCIAL_ACTION_SORROW = 13
PUBLIC_SOCIAL_ACTIONS = [
    SOCIAL_ACTION_HELLO,
    SOCIAL_ACTION_VICTORY,
    SOCIAL_ACTION_ADVANCE,
    SOCIAL_ACTION_NO,
    SOCIAL_ACTION_YES,
    SOCIAL_ACTION_BOW,
    SOCIAL_ACTION_UNAWARE,
    SOCIAL_ACTION_WAITING,
    SOCIAL_ACTION_LAUGH,
    SOCIAL_ACTION_APPLAUD,
    SOCIAL_ACTION_DANCE,
    SOCIAL_ACTION_SORROW,
]

SEVEN_SIGNS_PERIOD_COMPETITION_RECRUITING = 0
SEVEN_SIGNS_PERIOD_COMPETITION = 1
SEVEN_SIGNS_PERIOD_COMPETITION_RESULTS = 2
SEVEN_SIGNS_PERIOD_SEAL_VALIDATION = 3

WAIT_TYPE_SITTING = 0
WAIT_TYPE_STANDING = 1
WAIT_TYPE_START_FAKE_DEATH = 2
WAIT_TYPE_STOP_FAKE_DEATH = 3
