from enum import Enum


class ElevatorState(str, Enum):
    READY = "READY"
    OUTOFORDER = "OUTOFORDER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
