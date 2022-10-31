from enum import Enum


class TicketListRequestFilterType(str, Enum):
    NO_FILTER = "NO_FILTER"
    HVV_LISTED = "HVV_LISTED"

    def __str__(self) -> str:
        return str(self.value)
