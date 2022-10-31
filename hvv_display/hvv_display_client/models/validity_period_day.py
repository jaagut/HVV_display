from enum import Enum


class ValidityPeriodDay(str, Enum):
    WEEKDAY = "WEEKDAY"
    WEEKEND = "WEEKEND"

    def __str__(self) -> str:
        return str(self.value)
