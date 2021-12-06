class ApiException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class WrongCredentials(ApiException):
    pass


class DocumentDoesntExist(ApiException):
    pass
