import logging

import game.constants
import game.packets
import game.states
from common.api_handlers import l2_request_handler
from common.template import Parameter, Template
from game.models.character import Character
from game.models.structures.character.template import CharacterTemplate
from game.models.world import WORLD
from game.static.character_template import StaticCharacterTemplate

LOG = logging.getLogger(f"l2py.{__name__}")


async def _char_list(session):
    session.set_state(game.states.WaitingCharacterSelect)
    session.send_packet(
        game.packets.CharList(await Character.all(account_username=session.account.username))
    )


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_CREATE,
    Template(
        [
            Parameter("name", start=0, type=String, func=String.read),
            Parameter("race", start="$name.stop", length=4, type=Int32),
            Parameter("sex", start="$race.stop", length=4, type=Int32),
            Parameter("class_id", start="$sex.stop", length=4, type=Int32),
            Parameter("INT", start="$class_id.stop", length=4, type=Int32),
            Parameter("STR", start="$INT.stop", length=4, type=Int32),
            Parameter("CON", start="$STR.stop", length=4, type=Int32),
            Parameter("MEN", start="$CON.stop", length=4, type=Int32),
            Parameter("DEX", start="$MEN.stop", length=4, type=Int32),
            Parameter("WIT", start="$DEX.stop", length=4, type=Int32),
            Parameter("hair_style", start="$WIT.stop", length=4, type=Int32),
            Parameter("hair_color", start="$hair_style.stop", length=4, type=Int32),
            Parameter("face", start="$hair_color.stop", length=4, type=Int32),
        ]
    ),
    states=[game.states.CreatingCharacter],
)
async def character_create(request):

    templates = {template.class_id: template for template in StaticCharacterTemplate.read_file()}
    class_template = templates[request.validated_data["class_id"]]
    account = request.session.account

    char_template = CharacterTemplate.from_static_template(
        class_template, request.validated_data["sex"]
    )

    new_char = await Character.from_template(
        char_template,
        request.validated_data["name"],
        account,
        request.validated_data["sex"],
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
        return game.packets.CharCreateFail(1)
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
    return game.packets.CharTemplates(templates)


@l2_request_handler(
    game.constants.GAME_REQUEST_CHARACTER_DELETE,
    Template([Parameter("character_slot", start=0, length=4, type=Int32)]),
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
    Template([Parameter("character_slot", start=0, length=4, type=Int32)]),
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
    Template([Parameter("character_slot", start=0, length=4, type=Int32)]),
    states=[game.states.WaitingCharacterSelect],
)
async def character_selected(request):
    account = request.session.account

    for slot_id, character in enumerate(await Character.all(account_username=account.username)):
        if slot_id == request.validated_data["character_slot"]:
            request.session.set_state(game.states.CharacterSelected)
            request.session.set_character(character)
            WORLD.enter(request.session, character)
            request.session.send_packet(game.packets.CharSelected(character))
            account.last_character = character.name
            await account.commit_changes(fields=["last_character"])


@l2_request_handler(
    game.constants.GAME_REQUEST_RESTART,
    Template([]),
    states="*",
)
async def restart(request):

    account = request.session.account

    request.session.send_packet(game.packets.RestartResponse("Good bye!"))

    request.session.set_state(game.states.WaitingCharacterSelect)
    request.session.logout_character()

    request.session.send_packet(
        game.packets.CharList(await Character.all(account_username=account.username))
    )
