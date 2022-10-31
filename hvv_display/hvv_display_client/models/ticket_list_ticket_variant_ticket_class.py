from enum import Enum


class TicketListTicketVariantTicketClass(str, Enum):
    NONE = "NONE"
    SECOND = "SECOND"
    FIRST = "FIRST"
    SCHNELL = "SCHNELL"

    def __str__(self) -> str:
        return str(self.value)
