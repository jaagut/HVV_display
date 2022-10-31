from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.vehicle_map_path_coordinate_type import VehicleMapPathCoordinateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleMapPath")


@attr.s(auto_attribs=True)
class VehicleMapPath:
    """
    Attributes:
        coordinate_type (VehicleMapPathCoordinateType):
        track (Union[Unset, List[float]]):
    """

    coordinate_type: VehicleMapPathCoordinateType
    track: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        coordinate_type = self.coordinate_type.value

        track: Union[Unset, List[float]] = UNSET
        if not isinstance(self.track, Unset):
            track = self.track

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coordinateType": coordinate_type,
            }
        )
        if track is not UNSET:
            field_dict["track"] = track

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        coordinate_type = VehicleMapPathCoordinateType(d.pop("coordinateType"))

        track = cast(List[float], d.pop("track", UNSET))

        vehicle_map_path = cls(
            coordinate_type=coordinate_type,
            track=track,
        )

        vehicle_map_path.additional_properties = d
        return vehicle_map_path

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
