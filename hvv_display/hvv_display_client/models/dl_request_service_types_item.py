from enum import Enum


class DLRequestServiceTypesItem(str, Enum):
    ZUG = "ZUG"
    UBAHN = "UBAHN"
    SBAHN = "SBAHN"
    AKN = "AKN"
    RBAHN = "RBAHN"
    FERNBAHN = "FERNBAHN"
    BUS = "BUS"
    STADTBUS = "STADTBUS"
    METROBUS = "METROBUS"
    SCHNELLBUS = "SCHNELLBUS"
    NACHTBUS = "NACHTBUS"
    XPRESSBUS = "XPRESSBUS"
    EILBUS = "EILBUS"
    AST = "AST"
    FAEHRE = "FAEHRE"

    def __str__(self) -> str:
        return str(self.value)
