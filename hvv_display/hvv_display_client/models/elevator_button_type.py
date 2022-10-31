from enum import Enum


class ElevatorButtonType(str, Enum):
    BRAILLE = "BRAILLE"
    ACUSTIC = "ACUSTIC"
    COMBI = "COMBI"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
