from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffInfoSelector")


@attr.s(auto_attribs=True)
class TariffInfoSelector:
    """
    Attributes:
        tariff (Union[Unset, str]):  Default: 'HVV'.
        tariff_regions (Union[Unset, bool]):  Default: True.
        kinds (Union[Unset, List[int]]):
    """

    tariff: Union[Unset, str] = "HVV"
    tariff_regions: Union[Unset, bool] = True
    kinds: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tariff = self.tariff
        tariff_regions = self.tariff_regions
        kinds: Union[Unset, List[int]] = UNSET
        if not isinstance(self.kinds, Unset):
            kinds = self.kinds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tariff is not UNSET:
            field_dict["tariff"] = tariff
        if tariff_regions is not UNSET:
            field_dict["tariffRegions"] = tariff_regions
        if kinds is not UNSET:
            field_dict["kinds"] = kinds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tariff = d.pop("tariff", UNSET)

        tariff_regions = d.pop("tariffRegions", UNSET)

        kinds = cast(List[int], d.pop("kinds", UNSET))

        tariff_info_selector = cls(
            tariff=tariff,
            tariff_regions=tariff_regions,
            kinds=kinds,
        )

        tariff_info_selector.additional_properties = d
        return tariff_info_selector

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
