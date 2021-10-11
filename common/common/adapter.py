import abc


class DataAdapter(abc.ABC):
    @abc.abstractmethod
    def client(self):
        pass

    @abc.abstractmethod
    def collection(self, database_name, collection_name):
        pass

    @abc.abstractmethod
    def database(self, database_name):
        pass
