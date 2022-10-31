from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.shop_info_shop_type import ShopInfoShopType

T = TypeVar("T", bound="ShopInfo")


@attr.s(auto_attribs=True)
class ShopInfo:
    """
    Attributes:
        shop_type (ShopInfoShopType):
        url (str):
    """

    shop_type: ShopInfoShopType
    url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shop_type = self.shop_type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shopType": shop_type,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shop_type = ShopInfoShopType(d.pop("shopType"))

        url = d.pop("url")

        shop_info = cls(
            shop_type=shop_type,
            url=url,
        )

        shop_info.additional_properties = d
        return shop_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
