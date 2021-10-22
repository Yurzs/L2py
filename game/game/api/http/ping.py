import json

from aiohttp.web import Response
from aiojsonapi import routes


@routes.post("/api/ping")
async def ping(request):
    return Response(body=json.dumps({"result": {"pong": True}}), content_type="application/json")
