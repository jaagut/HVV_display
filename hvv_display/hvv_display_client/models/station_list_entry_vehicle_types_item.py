from enum import Enum


class StationListEntryVehicleTypesItem(str, Enum):
    REGIONALBUS = "REGIONALBUS"
    METROBUS = "METROBUS"
    NACHTBUS = "NACHTBUS"
    SCHNELLBUS = "SCHNELLBUS"
    XPRESSBUS = "XPRESSBUS"
    AST = "AST"
    SCHIFF = "SCHIFF"
    U_BAHN = "U_BAHN"
    S_BAHN = "S_BAHN"
    A_BAHN = "A_BAHN"
    R_BAHN = "R_BAHN"
    F_BAHN = "F_BAHN"
    EILBUS = "EILBUS"

    def __str__(self) -> str:
        return str(self.value)
