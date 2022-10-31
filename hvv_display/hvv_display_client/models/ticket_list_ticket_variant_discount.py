from enum import Enum


class TicketListTicketVariantDiscount(str, Enum):
    NONE = "NONE"
    ONLINE = "ONLINE"
    SOCIAL = "SOCIAL"

    def __str__(self) -> str:
        return str(self.value)
