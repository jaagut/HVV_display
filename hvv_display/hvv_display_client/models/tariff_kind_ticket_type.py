from enum import Enum


class TariffKindTicketType(str, Enum):
    OCCASIONAL_TICKET = "OCCASIONAL_TICKET"
    SEASON_TICKET = "SEASON_TICKET"

    def __str__(self) -> str:
        return str(self.value)
