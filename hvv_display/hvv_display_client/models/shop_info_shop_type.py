from enum import Enum


class ShopInfoShopType(str, Enum):
    AST = "AST"

    def __str__(self) -> str:
        return str(self.value)
