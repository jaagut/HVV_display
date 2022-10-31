from enum import Enum


class GRRequestRealtime(str, Enum):
    PLANDATA = "PLANDATA"
    REALTIME = "REALTIME"
    AUTO = "AUTO"

    def __str__(self) -> str:
        return str(self.value)
