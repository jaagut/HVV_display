from enum import Enum


class TariffOptimizerTicketRegionType(str, Enum):
    RING = "RING"
    ZONE = "ZONE"
    COUNTY = "COUNTY"
    GH_ZONE = "GH_ZONE"

    def __str__(self) -> str:
        return str(self.value)
