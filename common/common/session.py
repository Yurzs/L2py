import uuid
from threading import Lock


class Session:
    state: type
    STORAGE: dict
    protocol: "common.transport.protocol.TCPProtocol"

    def __init__(self):
        self.uuid = uuid.uuid4()
        self.lock_before = Lock()
        self.lock_after = Lock()

        self.account: "Account" = None

    def set_state(self, new_state):
        """Sets new session state.

        :param new_state:
        :return:
        """
        self.state = new_state

    def send_packet(self, packet):
        from common.response import Response

        response = Response(packet=packet, session=self)
        return self.protocol.transport.write(response)
