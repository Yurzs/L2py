import typing
import uuid
from multiprocessing.managers import SyncManager

MANAGER = SyncManager()


class Session:
    state: type
    STORAGE: dict
    protocol: "common.transport.protocol.TCPProtocol"

    def __init__(self):
        self.uuid = uuid.uuid4()

    @classmethod
    def data(cls):
        return cls.STORAGE.get(cls.__name__, {})

    @classmethod
    def start(cls):
        MANAGER.start()
        cls.STORAGE = MANAGER.dict()

    def set_state(self, new_state, clear_data=False):
        """Sets new session state.

        :param new_state:
        :param clear_data:
        :return:
        """
        self.state = new_state
        if clear_data:
            session_data = self.STORAGE.get(self.__class__.__name__, {})
            session_data.pop(self.uuid, None)
            self.STORAGE[self.__class__.__name__] = session_data

    def set_data(self, data: typing.Mapping):
        """Sets session data.

        :param data: dict with new data
        """

        session_data = self.STORAGE.get(self.__class__.__name__, {})
        session_data.setdefault(self.uuid, {}).update(data)
        self.STORAGE[self.__class__.__name__] = session_data

    def get_data(self):
        return self.STORAGE.get(self.__class__.__name__, {}).get(self.uuid, {})

    def delete(self):
        data = self.STORAGE.get(self.__class__.__name__, {})
        try:
            data.pop(self.uuid)
        except KeyError:
            return
        self.STORAGE[self.__class__.__name__] = data

    @classmethod
    def delete_session(cls, session_uuid):
        data = cls.STORAGE.get(cls.__name__, {})
        data.pop(session_uuid, None)
        cls.STORAGE[cls.__name__] = data

    def send_packet(self, packet):
        from common.response import Response

        response = Response(packet, self)
        return self.protocol.transport.write(response)
