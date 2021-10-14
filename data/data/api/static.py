import collections

from aiojsonapi import JsonTemplate, routes

from data.models import structures


class StaticDataCache(collections.defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = self.default_factory(key)
        return self[key]


cache = StaticDataCache(lambda key: getattr(structures, key).read_file())


@routes.post("/api/static_data")
@JsonTemplate({"classname": str, "__required__": ["classname"]})
async def static_data(request, validated_data):
    print()
    return cache[validated_data["classname"]]
