from enum import Enum


class AnnouncementRequestFilterPlanned(str, Enum):
    NO_FILTER = "NO_FILTER"
    ONLY_PLANNED = "ONLY_PLANNED"
    ONLY_UNPLANNED = "ONLY_UNPLANNED"

    def __str__(self) -> str:
        return str(self.value)
