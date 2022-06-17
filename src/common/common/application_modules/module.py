import abc


class ApplicationModule(abc.ABC):
    """Application extension module base."""

    name: str

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    async def start(self, config, loop):
        """Initializes application module. MUST be set in each module."""
