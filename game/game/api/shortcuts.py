import logging

import game.constants
import game.packets
from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.template import Parameter, Template
from game.models import Character
from game.models.structures.shortcut import Shortcut
from game.request import GameRequest

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(
    game.constants.GAME_REQUEST_SHORTCUT_REG,
    Template(
        [
            Parameter(id="type", start=0, length=4, type=ctype.int32),
            Parameter(id="slot", start="$type.stop", length=4, type=ctype.int32),
            Parameter(id="id", start="$slot.stop", length=4, type=ctype.int32),
        ]
    ),
    states="*",
)
async def request_short_cut_reg(request: GameRequest):
    LOG.debug("saving shortcut", request)
    character: Character = request.session.character
    shortcut = Shortcut(
        slot=ctype.int32(request.validated_data["slot"].value % 12),
        page=ctype.int32(request.validated_data["slot"].value / 12),
        type=ctype.int32(request.validated_data["type"]),
        id=ctype.int32(request.validated_data["id"]),
        level=ctype.int32(-1),
    )
    character.shortcuts.append(shortcut)
    character.update_shortcut(request.session, shortcut)
    await character.commit_changes(fields=["shortcuts"])

