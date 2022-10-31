from enum import Enum


class GRRequestCoordinateType(str, Enum):
    EPSG_4326 = "EPSG_4326"
    EPSG_31466 = "EPSG_31466"
    EPSG_31467 = "EPSG_31467"
    EPSG_31468 = "EPSG_31468"
    EPSG_31469 = "EPSG_31469"

    def __str__(self) -> str:
        return str(self.value)
