from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.coordinate import Coordinate

T = TypeVar("T", bound="BoundingBox")


@attr.s(auto_attribs=True)
class BoundingBox:
    """
    Attributes:
        lower_left (Coordinate):
        upper_right (Coordinate):
    """

    lower_left: Coordinate
    upper_right: Coordinate
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lower_left = self.lower_left.to_dict()

        upper_right = self.upper_right.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lowerLeft": lower_left,
                "upperRight": upper_right,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lower_left = Coordinate.from_dict(d.pop("lowerLeft"))

        upper_right = Coordinate.from_dict(d.pop("upperRight"))

        bounding_box = cls(
            lower_left=lower_left,
            upper_right=upper_right,
        )

        bounding_box.additional_properties = d
        return bounding_box

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
