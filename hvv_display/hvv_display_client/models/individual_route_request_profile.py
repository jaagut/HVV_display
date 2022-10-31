from enum import Enum


class IndividualRouteRequestProfile(str, Enum):
    BICYCLE_NORMAL = "BICYCLE_NORMAL"
    BICYCLE_RACING = "BICYCLE_RACING"
    BICYCLE_QUIET_ROADS = "BICYCLE_QUIET_ROADS"
    BICYCLE_MAIN_ROADS = "BICYCLE_MAIN_ROADS"
    BICYCLE_BAD_WEATHER = "BICYCLE_BAD_WEATHER"
    FOOT_NORMAL = "FOOT_NORMAL"

    def __str__(self) -> str:
        return str(self.value)
