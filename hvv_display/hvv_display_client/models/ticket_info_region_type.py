from enum import Enum


class TicketInfoRegionType(str, Enum):
    ZONE = "ZONE"
    GH_ZONE = "GH_ZONE"
    RING = "RING"
    COUNTY = "COUNTY"
    GH = "GH"
    NET = "NET"
    ZG = "ZG"
    STADTVERKEHR = "STADTVERKEHR"

    def __str__(self) -> str:
        return str(self.value)
