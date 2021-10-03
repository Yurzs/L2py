class Error(Exception):
    def __init__(self, message):
        super().__init__(message)


class ChecksumMismatch(Error):
    def __init__(self):
        super().__init__("Checksum mismatch.")


class RequestLengthDoesntMatch(Error):
    def __init__(self):
        super().__init__("Requests length byte value doesn't match actual data size.")


class UnknownAction(Error):
    def __init__(self):
        super().__init__("Unknown action.")


class DocumentNotFound(Error):
    def __init__(self):
        super().__init__("Specified document doesn't exist.")
