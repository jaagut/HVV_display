from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attribute import Attribute
from ..models.sd_name import SDName
from ..models.service import Service
from ..types import UNSET, Unset

T = TypeVar("T", bound="Departure")


@attr.s(auto_attribs=True)
class Departure:
    """
    Attributes:
        line (Service):
        direction_id (Union[Unset, int]):
        time_offset (Union[Unset, int]):
        delay (Union[Unset, int]):
        extra (Union[Unset, bool]):
        cancelled (Union[Unset, bool]):
        service_id (Union[Unset, int]):
        station (Union[Unset, SDName]):
        platform (Union[Unset, str]):
        realtime_platform (Union[Unset, str]):
        attributes (Union[Unset, List[Attribute]]):
    """

    line: Service
    direction_id: Union[Unset, int] = UNSET
    time_offset: Union[Unset, int] = UNSET
    delay: Union[Unset, int] = UNSET
    extra: Union[Unset, bool] = False
    cancelled: Union[Unset, bool] = False
    service_id: Union[Unset, int] = UNSET
    station: Union[Unset, SDName] = UNSET
    platform: Union[Unset, str] = UNSET
    realtime_platform: Union[Unset, str] = UNSET
    attributes: Union[Unset, List[Attribute]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line = self.line.to_dict()

        direction_id = self.direction_id
        time_offset = self.time_offset
        delay = self.delay
        extra = self.extra
        cancelled = self.cancelled
        service_id = self.service_id
        station: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.station, Unset):
            station = self.station.to_dict()

        platform = self.platform
        realtime_platform = self.realtime_platform
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line": line,
            }
        )
        if direction_id is not UNSET:
            field_dict["directionId"] = direction_id
        if time_offset is not UNSET:
            field_dict["timeOffset"] = time_offset
        if delay is not UNSET:
            field_dict["delay"] = delay
        if extra is not UNSET:
            field_dict["extra"] = extra
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if station is not UNSET:
            field_dict["station"] = station
        if platform is not UNSET:
            field_dict["platform"] = platform
        if realtime_platform is not UNSET:
            field_dict["realtimePlatform"] = realtime_platform
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line = Service.from_dict(d.pop("line"))

        direction_id = d.pop("directionId", UNSET)

        time_offset = d.pop("timeOffset", UNSET)

        delay = d.pop("delay", UNSET)

        extra = d.pop("extra", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        service_id = d.pop("serviceId", UNSET)

        _station = d.pop("station", UNSET)
        station: Union[Unset, SDName]
        if isinstance(_station, Unset):
            station = UNSET
        else:
            station = SDName.from_dict(_station)

        platform = d.pop("platform", UNSET)

        realtime_platform = d.pop("realtimePlatform", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        departure = cls(
            line=line,
            direction_id=direction_id,
            time_offset=time_offset,
            delay=delay,
            extra=extra,
            cancelled=cancelled,
            service_id=service_id,
            station=station,
            platform=platform,
            realtime_platform=realtime_platform,
            attributes=attributes,
        )

        departure.additional_properties = d
        return departure

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
