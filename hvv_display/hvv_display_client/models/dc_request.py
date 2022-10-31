import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.dc_request_coordinate_type import DCRequestCoordinateType
from ..models.dc_request_filter_type import DCRequestFilterType
from ..models.dc_request_segments import DCRequestSegments
from ..models.sd_name import SDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DCRequest")


@attr.s(auto_attribs=True)
class DCRequest:
    """
    Attributes:
        line_key (str):
        station (SDName):
        time (datetime.datetime):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, DCRequestFilterType]):  Default: DCRequestFilterType.NO_FILTER.
        direction (Union[Unset, str]):
        origin (Union[Unset, str]):
        service_id (Union[Unset, int]):  Default: -1.
        segments (Union[Unset, DCRequestSegments]):  Default: DCRequestSegments.ALL.
        show_path (Union[Unset, bool]):
        coordinate_type (Union[Unset, DCRequestCoordinateType]):  Default: DCRequestCoordinateType.EPSG_4326.
    """

    line_key: str
    station: SDName
    time: datetime.datetime
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[Unset, DCRequestFilterType] = DCRequestFilterType.NO_FILTER
    direction: Union[Unset, str] = UNSET
    origin: Union[Unset, str] = UNSET
    service_id: Union[Unset, int] = -1
    segments: Union[Unset, DCRequestSegments] = DCRequestSegments.ALL
    show_path: Union[Unset, bool] = False
    coordinate_type: Union[
        Unset, DCRequestCoordinateType
    ] = DCRequestCoordinateType.EPSG_4326
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_key = self.line_key
        station = self.station.to_dict()

        time = self.time.isoformat()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        direction = self.direction
        origin = self.origin
        service_id = self.service_id
        segments: Union[Unset, str] = UNSET
        if not isinstance(self.segments, Unset):
            segments = self.segments.value

        show_path = self.show_path
        coordinate_type: Union[Unset, str] = UNSET
        if not isinstance(self.coordinate_type, Unset):
            coordinate_type = self.coordinate_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineKey": line_key,
                "station": station,
                "time": time,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if direction is not UNSET:
            field_dict["direction"] = direction
        if origin is not UNSET:
            field_dict["origin"] = origin
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if segments is not UNSET:
            field_dict["segments"] = segments
        if show_path is not UNSET:
            field_dict["showPath"] = show_path
        if coordinate_type is not UNSET:
            field_dict["coordinateType"] = coordinate_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_key = d.pop("lineKey")

        station = SDName.from_dict(d.pop("station"))

        time = isoparse(d.pop("time"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, DCRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = DCRequestFilterType(_filter_type)

        direction = d.pop("direction", UNSET)

        origin = d.pop("origin", UNSET)

        service_id = d.pop("serviceId", UNSET)

        _segments = d.pop("segments", UNSET)
        segments: Union[Unset, DCRequestSegments]
        if isinstance(_segments, Unset):
            segments = UNSET
        else:
            segments = DCRequestSegments(_segments)

        show_path = d.pop("showPath", UNSET)

        _coordinate_type = d.pop("coordinateType", UNSET)
        coordinate_type: Union[Unset, DCRequestCoordinateType]
        if isinstance(_coordinate_type, Unset):
            coordinate_type = UNSET
        else:
            coordinate_type = DCRequestCoordinateType(_coordinate_type)

        dc_request = cls(
            line_key=line_key,
            station=station,
            time=time,
            language=language,
            version=version,
            filter_type=filter_type,
            direction=direction,
            origin=origin,
            service_id=service_id,
            segments=segments,
            show_path=show_path,
            coordinate_type=coordinate_type,
        )

        dc_request.additional_properties = d
        return dc_request

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
