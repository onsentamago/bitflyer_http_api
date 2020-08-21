import logging


class ServerConnectionError(Exception):

    def __init__(self):
        self.message = "Connection error occurred"
        logging.exception(self.message)
        super().__init__(self.message)
