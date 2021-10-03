import abc


class Middleware(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def before(cls, session, request):
        pass

    @classmethod
    @abc.abstractmethod
    def after(cls, session, response):
        pass
