from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tariff_region_info_region_type import TariffRegionInfoRegionType
from ..models.tariff_region_list import TariffRegionList
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffRegionInfo")


@attr.s(auto_attribs=True)
class TariffRegionInfo:
    """
    Attributes:
        region_type (TariffRegionInfoRegionType):
        alternatives (Union[Unset, List[TariffRegionList]]):
    """

    region_type: TariffRegionInfoRegionType
    alternatives: Union[Unset, List[TariffRegionList]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_type = self.region_type.value

        alternatives: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alternatives, Unset):
            alternatives = []
            for alternatives_item_data in self.alternatives:
                alternatives_item = alternatives_item_data.to_dict()

                alternatives.append(alternatives_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regionType": region_type,
            }
        )
        if alternatives is not UNSET:
            field_dict["alternatives"] = alternatives

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_type = TariffRegionInfoRegionType(d.pop("regionType"))

        alternatives = []
        _alternatives = d.pop("alternatives", UNSET)
        for alternatives_item_data in _alternatives or []:
            alternatives_item = TariffRegionList.from_dict(alternatives_item_data)

            alternatives.append(alternatives_item)

        tariff_region_info = cls(
            region_type=region_type,
            alternatives=alternatives,
        )

        tariff_region_info.additional_properties = d
        return tariff_region_info

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
