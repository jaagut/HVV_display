from enum import Enum


class DCRequestSegments(str, Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    ALL = "ALL"

    def __str__(self) -> str:
        return str(self.value)
