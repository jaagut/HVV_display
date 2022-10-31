from enum import Enum


class TicketListResponseReturnCode(str, Enum):
    OK = "OK"
    ERROR_ROUTE = "ERROR_ROUTE"
    ERROR_COMM = "ERROR_COMM"
    ERROR_CN_TOO_MANY = "ERROR_CN_TOO_MANY"
    ERROR_TEXT = "ERROR_TEXT"
    START_DEST_TOO_CLOSE = "START_DEST_TOO_CLOSE"

    def __str__(self) -> str:
        return str(self.value)
