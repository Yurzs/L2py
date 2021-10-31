from common.misc import Singleton


class StaticDataCache(metaclass=Singleton):
    def __init__(self):
        self.data = {}

    def read(self, filepath):
        if filepath not in self.data:
            with open(filepath) as file:
                self.data[filepath] = file.read()
        return self.data[filepath]
