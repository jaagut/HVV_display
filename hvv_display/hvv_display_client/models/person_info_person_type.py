from enum import Enum


class PersonInfoPersonType(str, Enum):
    ALL = "ALL"
    ELDERLY = "ELDERLY"
    APPRENTICE = "APPRENTICE"
    PUPIL = "PUPIL"
    STUDENT = "STUDENT"
    CHILD = "CHILD"

    def __str__(self) -> str:
        return str(self.value)
