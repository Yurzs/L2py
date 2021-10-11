import abc


class ApplicationModule(abc.ABC):
    name: str

    @abc.abstractmethod
    async def start(self, config, loop):
        pass
