from enum import Enum


class JourneySDNameType(str, Enum):
    UNKNOWN = "UNKNOWN"
    STATION = "STATION"
    ADDRESS = "ADDRESS"
    POI = "POI"
    COORDINATE = "COORDINATE"

    def __str__(self) -> str:
        return str(self.value)
