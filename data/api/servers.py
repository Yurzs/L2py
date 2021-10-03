from aiojsonapi import JsonTemplate, routes

from data.models.game_server import GameServer
from data.models.login_server import LoginServer


@routes.post("/api/data/servers/login.list")
async def login_servers_list(request):
    return [server async for server in LoginServer.all()]


@routes.post("/api/data/servers/game.list")
async def game_servers_list(request):
    return [server async for server in GameServer.all()]
