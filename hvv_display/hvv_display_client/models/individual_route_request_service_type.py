from enum import Enum


class IndividualRouteRequestServiceType(str, Enum):
    BUS = "BUS"
    TRAIN = "TRAIN"
    SHIP = "SHIP"
    FOOTPATH = "FOOTPATH"
    BICYCLE = "BICYCLE"
    AIRPLANE = "AIRPLANE"
    CHANGE = "CHANGE"
    CHANGE_SAME_PLATFORM = "CHANGE_SAME_PLATFORM"

    def __str__(self) -> str:
        return str(self.value)
