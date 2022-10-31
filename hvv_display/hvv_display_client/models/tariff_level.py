from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.required_region_type import RequiredRegionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffLevel")


@attr.s(auto_attribs=True)
class TariffLevel:
    """
    Attributes:
        label (str):
        required_region_type (RequiredRegionType):
        id (Union[Unset, int]):
    """

    label: str
    required_region_type: RequiredRegionType
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        required_region_type = self.required_region_type.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "requiredRegionType": required_region_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        required_region_type = RequiredRegionType.from_dict(d.pop("requiredRegionType"))

        id = d.pop("id", UNSET)

        tariff_level = cls(
            label=label,
            required_region_type=required_region_type,
            id=id,
        )

        tariff_level.additional_properties = d
        return tariff_level

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
