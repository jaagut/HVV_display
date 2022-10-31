from enum import Enum


class LLRequestModificationTypesItem(str, Enum):
    MAIN = "MAIN"
    SEQUENCE = "SEQUENCE"

    def __str__(self) -> str:
        return str(self.value)
