import logging

import game.constants
from common.ctype import ctype
from common.api_handlers import l2_request_handler
from common.template import Template, Parameter

LOG = logging.getLogger(f"l2py.{__name__}")


@l2_request_handler(game.constants.GAME_REQUEST_SHORTCUT_REG,
                    Template([
                        Parameter(id="type", start=0, length=4, type=ctype.int32),
                        Parameter(id="slot", start="$type.stop", length=4, type=ctype.int32),
                        Parameter(id="id", start="$slot.stop", length=4, type=ctype.int32),
                        Parameter(id="unk", start="$id.stop", length=4, type=ctype.int32),
                    ]), states="*")
async def request_short_cut_reg(request):
    LOG.debug("saving shortcut", request)
    pass
