from enum import Enum


class SingleTicketOptimizerRequestRouteExtraFareType(str, Enum):
    NO = "NO"
    POSSIBLE = "POSSIBLE"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
