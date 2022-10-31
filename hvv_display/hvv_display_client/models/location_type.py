from enum import Enum


class LocationType(str, Enum):
    SINGLE_LINE = "SINGLE_LINE"
    ALL_LINES_OF_CARRIER = "ALL_LINES_OF_CARRIER"
    COMPLETE_NET = "COMPLETE_NET"

    def __str__(self) -> str:
        return str(self.value)
