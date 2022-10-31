from enum import Enum


class TariffOptimizerTicketPersonType(str, Enum):
    ALL = "ALL"
    ADULT = "ADULT"
    ELDERLY = "ELDERLY"
    APPRENTICE = "APPRENTICE"
    PUPIL = "PUPIL"
    STUDENT = "STUDENT"
    CHILD = "CHILD"

    def __str__(self) -> str:
        return str(self.value)
