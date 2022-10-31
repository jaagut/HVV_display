from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.track_coordinates_request_coordinate_type import (
    TrackCoordinatesRequestCoordinateType,
)
from ..models.track_coordinates_request_filter_type import (
    TrackCoordinatesRequestFilterType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackCoordinatesRequest")


@attr.s(auto_attribs=True)
class TrackCoordinatesRequest:
    """
    Attributes:
        stop_point_keys (List[str]):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, TrackCoordinatesRequestFilterType]):  Default:
            TrackCoordinatesRequestFilterType.NO_FILTER.
        coordinate_type (Union[Unset, TrackCoordinatesRequestCoordinateType]):  Default:
            TrackCoordinatesRequestCoordinateType.EPSG_4326.
    """

    stop_point_keys: List[str]
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, TrackCoordinatesRequestFilterType
    ] = TrackCoordinatesRequestFilterType.NO_FILTER
    coordinate_type: Union[
        Unset, TrackCoordinatesRequestCoordinateType
    ] = TrackCoordinatesRequestCoordinateType.EPSG_4326
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_point_keys = self.stop_point_keys

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        coordinate_type: Union[Unset, str] = UNSET
        if not isinstance(self.coordinate_type, Unset):
            coordinate_type = self.coordinate_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPointKeys": stop_point_keys,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if coordinate_type is not UNSET:
            field_dict["coordinateType"] = coordinate_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stop_point_keys = cast(List[str], d.pop("stopPointKeys"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, TrackCoordinatesRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = TrackCoordinatesRequestFilterType(_filter_type)

        _coordinate_type = d.pop("coordinateType", UNSET)
        coordinate_type: Union[Unset, TrackCoordinatesRequestCoordinateType]
        if isinstance(_coordinate_type, Unset):
            coordinate_type = UNSET
        else:
            coordinate_type = TrackCoordinatesRequestCoordinateType(_coordinate_type)

        track_coordinates_request = cls(
            stop_point_keys=stop_point_keys,
            language=language,
            version=version,
            filter_type=filter_type,
            coordinate_type=coordinate_type,
        )

        track_coordinates_request.additional_properties = d
        return track_coordinates_request

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
