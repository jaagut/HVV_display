from enum import Enum


class GRRequestFilterType(str, Enum):
    NO_FILTER = "NO_FILTER"
    HVV_LISTED = "HVV_LISTED"

    def __str__(self) -> str:
        return str(self.value)
