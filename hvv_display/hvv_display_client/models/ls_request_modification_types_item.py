from enum import Enum


class LSRequestModificationTypesItem(str, Enum):
    MAIN = "MAIN"
    POSITION = "POSITION"

    def __str__(self) -> str:
        return str(self.value)
