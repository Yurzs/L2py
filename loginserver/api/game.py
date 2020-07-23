from aiojson import JsonTemplate
from aiojson.routes import post

from common.datatypes import Int32, String
from loginserver.session_storage import session_storage


@post("/game/auth_login")
@JsonTemplate({
    "login": String,
    "login_ok1": Int32,
    "login_ok2": Int32,
    "play_ok1": Int32,
    "play_ok2": Int32,
    "__required__": ["login", "login_ok1", "login_ok2", "play_ok1", "play_ok2"],
})
async def auth_login(request, validated_data):
    if session_storage.get(validated_data["login"]):
        session_data = session_storage[validated_data.pop("login")]
        if validated_data == session_data:
            return True
    return False
