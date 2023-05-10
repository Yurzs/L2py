import functools


class Broadcaster:
    @classmethod
    def broadcast(
        cls,
        packet_constructor,
        radius=500,
        to_me=False,
        pass_args_kwargs=False,
        specific_ids=None,
    ):
        def inner(f):
            @functools.wraps(f)
            async def wrap(obj, *args, **kwargs):
                from game.models.world import WORLD

                result = await f(obj, *args, **kwargs)

                if pass_args_kwargs:
                    packet = packet_constructor(obj, *args, **kwargs)
                else:
                    packet = packet_constructor(obj)

                for session in WORLD.players_sessions_nearby(
                    obj.position,
                    me=obj if not to_me else None,
                    radius=radius,
                ):
                    session.send_packet(packet)
                return result

            return wrap

        return inner

    @classmethod
    def broadcast_packet(
        cls,
        packet,
        obj,
        radius=500,
        to_me=False,
        specific_ids=None,
    ):
        from game.models.world import WORLD

        for session in WORLD.players_sessions_nearby(
            obj.position,
            me=obj if not to_me else None,
            radius=radius,
        ):
            session.send_packet(packet)
