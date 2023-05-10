from __future__ import annotations

from typing import Optional

import game.packets
from game.broadcaster import Broadcaster
from game.models.structures.object.object import L2Object


class Playable(L2Object):
    target: Optional[Playable] = None

    @Broadcaster.broadcast(lambda self: game.packets.TargetSelected(me=self, target=self.target))
    async def set_target(self, target: Playable):
        self.target = target

    @Broadcaster.broadcast(
        lambda self: game.packets.TargetUnselected(target_id=self.id, position=self.position)
    )
    async def unset_target(self):
        self.target = None

    # @Broadcaster.broadcast(lambda: True)
    async def attack(self):
        pass

    @Broadcaster.broadcast(
        pass_args_kwargs=True,
        packet_constructor=lambda self, text_type, text: game.packets.CreatureSay(
            object_id=self.id,
            text_type=text_type,
            character_name=self.name,
            text=text,
        ),
        to_me=True,
    )
    async def say(self, text_type, text):
        pass
