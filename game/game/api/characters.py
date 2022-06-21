import logging

import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.ctype import ctype
from common.misc import decode_str
from common.template import Parameter, Template
from game.models.character import Character
from game.models.structures.character.template import CharacterTemplate
from game.models.world import WORLD
from game.static.character_template import StaticCharacterTemplate

LOG = logging.getLogger(f"l2py.{__name__}")


async def _char_list(session):
    session.set_state(game.states.WaitingCharacterSelect)
    session.send_packet(
        game.packets.CharList(
            characters=await Character.all(account_username=session.account.username)
        )
    )


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_CREATE,
    Template(
        [
            Parameter(id="name", start=0, type=str, func=decode_str()),
            Parameter(id="race", start="$name.stop", length=4, type=ctype.int32),
            Parameter(id="sex", start="$race.stop", length=4, type=ctype.int32),
            Parameter(id="class_id", start="$sex.stop", length=4, type=ctype.int32),
            Parameter(id="INT", start="$class_id.stop", length=4, type=ctype.int32),
            Parameter(id="STR", start="$INT.stop", length=4, type=ctype.int32),
            Parameter(id="CON", start="$STR.stop", length=4, type=ctype.int32),
            Parameter(id="MEN", start="$CON.stop", length=4, type=ctype.int32),
            Parameter(id="DEX", start="$MEN.stop", length=4, type=ctype.int32),
            Parameter(id="WIT", start="$DEX.stop", length=4, type=ctype.int32),
            Parameter(id="hair_style", start="$WIT.stop", length=4, type=ctype.int32),
            Parameter(
                id="hair_color", start="$hair_style.stop", length=4, type=ctype.int32
            ),
            Parameter(id="face", start="$hair_color.stop", length=4, type=ctype.int32),
        ]
    ),
    states=[game.states.CreatingCharacter],
)
async def character_create(request):

    templates = {
        template.class_id: template for template in StaticCharacterTemplate.read_file()
    }
    class_template = templates[request.validated_data["class_id"]]
    account = request.session.account

    char_template = CharacterTemplate.from_static_template(
        class_template, ctype.bool(request.validated_data["sex"])
    )

    new_char = await Character.from_template(
        char_template,
        request.validated_data["name"],
        account,
        ctype.bool(request.validated_data["sex"]),
        request.validated_data["race"],
        request.validated_data["face"],
        request.validated_data["hair_style"],
        request.validated_data["hair_color"],
    )

    try:
        await new_char.insert()
    except Exception as e:
        LOG.exception(e)
        request.session.set_state(game.states.CreatingCharacter)
        return game.packets.CharCreateFail(reason_id=1)
    else:
        request.session.set_state(game.states.WaitingCharacterSelect)
        request.session.send_packet(game.packets.CharCreateOk())
        await _char_list(request.session)


@l2_request_handler(
    game.constants.GAME_REQUEST_NEW_CHARACTER,
    Template([]),
    states=[game.states.WaitingCharacterSelect, game.states.CreatingCharacter],
)
async def new_character(request):
    templates = StaticCharacterTemplate.read_file()
    request.session.set_state(game.states.CreatingCharacter)
    return game.packets.CharTemplates(templates=templates)


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_DELETE,
    Template([Parameter(id="character_slot", start=0, length=4, type=ctype.int32)]),
    states=[game.states.WaitingCharacterSelect],
)
async def character_delete(request):

    for slot_id, character in enumerate(
        await Character.all(account_username=request.session.account.username)
    ):
        if slot_id == request.validated_data["character_slot"]:
            await character.mark_deleted()
            request.session.send_packet(game.packets.CharDeleteOk())
            await _char_list(request.session)
    else:
        return game.packets.CharDeleteFail()


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_RESTORE,
    Template([Parameter(id="character_slot", start=0, length=4, type=ctype.int32)]),
    states=[game.states.WaitingCharacterSelect],
)
async def character_restore(request):

    for slot_id, character in enumerate(
        await Character.all(account_username=request.session.account.username)
    ):
        if slot_id == request.validated_data["character_slot"]:
            await character.remove_deleted_mark()
            await _char_list(request.session)


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_SELECTED,
    Template([Parameter(id="character_slot", start=0, length=4, type=ctype.int32)]),
    states=[game.states.WaitingCharacterSelect],
)
async def character_selected(request):
    account = request.session.account

    for slot_id, character in enumerate(
        await Character.all(account_username=account.username)
    ):
        if slot_id == request.validated_data["character_slot"]:
            request.session.set_state(game.states.CharacterSelected)
            request.session.set_character(character)
            WORLD.enter(request.session, character)
            request.session.send_packet(game.packets.CharSelected(character=character))
            account.last_character = character.name
            await account.commit_changes(fields=["last_character"])


@l2_request_handler(
    game.constants.GAME_REQUEST_RESTART,
    Template([]),
    states="*",
)
async def restart(request):

    request.session.send_packet(game.packets.RestartResponse(message="Good bye!"))

    request.session.set_state(game.states.WaitingCharacterSelect)
    request.session.logout_character()

    await _char_list(request.session)
