from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.required_region_type_type import RequiredRegionTypeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequiredRegionType")


@attr.s(auto_attribs=True)
class RequiredRegionType:
    """
    Attributes:
        type (RequiredRegionTypeType):
        count (Union[Unset, int]):
    """

    type: RequiredRegionTypeType
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RequiredRegionTypeType(d.pop("type"))

        count = d.pop("count", UNSET)

        required_region_type = cls(
            type=type,
            count=count,
        )

        required_region_type.additional_properties = d
        return required_region_type

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
