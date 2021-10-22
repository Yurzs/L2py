import asyncio

from aiojsonapi import JsonTemplate
from aiojsonapi.routes import post

from login.session import LoginSession


async def delete_session(session_uuid):
    await asyncio.sleep(1)
    LoginSession.delete_session(session_uuid)


@post("/api/login/auth_login")
@JsonTemplate(
    {
        "login": String,
        "login_ok1": Int32,
        "login_ok2": Int32,
        "play_ok1": Int32,
        "play_ok2": Int32,
        "__required__": ["__all__"],
    }
)
async def auth_login(request, validated_data):

    session = LoginSession.by_username(validated_data["login"])
    reply = {"authenticated": False, "account": None}
    if session is not None:
        session_uuid, session = list(session.items())[0]
        if (
            session["login_ok1"] == validated_data["login_ok1"]
            and session["login_ok2"] == validated_data["login_ok2"]
            and session["play_ok1"] == validated_data["play_ok1"]
            and session["play_ok2"] == validated_data["play_ok2"]
        ):
            reply.update({"authenticated": True, "account": session["account"]})
            asyncio.create_task(delete_session(session_uuid))
    return reply
