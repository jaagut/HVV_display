from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.coordinate_type import CoordinateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Coordinate")


@attr.s(auto_attribs=True)
class Coordinate:
    """
    Attributes:
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        type (Union[Unset, CoordinateType]):  Default: CoordinateType.EPSG_4326.
    """

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    type: Union[Unset, CoordinateType] = CoordinateType.EPSG_4326
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x = self.x
        y = self.y
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CoordinateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CoordinateType(_type)

        coordinate = cls(
            x=x,
            y=y,
            type=type,
        )

        coordinate.additional_properties = d
        return coordinate

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
