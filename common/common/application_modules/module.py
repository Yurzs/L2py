import abc


class ApplicationModule(abc.ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    async def start(self, config, loop):
        pass
