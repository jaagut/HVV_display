from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.attribute import Attribute
from ..models.coordinate import Coordinate
from ..models.gti_time import GTITime
from ..models.journey_sd_name_type import JourneySDNameType
from ..models.tariff_details import TariffDetails
from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneySDName")


@attr.s(auto_attribs=True)
class JourneySDName:
    """
    Attributes:
        name (Union[Unset, str]):
        city (Union[Unset, str]):
        combined_name (Union[Unset, str]):
        id (Union[Unset, str]):
        global_id (Union[Unset, str]):
        type (Union[Unset, JourneySDNameType]):  Default: JourneySDNameType.UNKNOWN.
        coordinate (Union[Unset, Coordinate]):
        layer (Union[Unset, int]):
        tariff_details (Union[Unset, TariffDetails]):
        service_types (Union[Unset, List[str]]):
        has_station_information (Union[Unset, bool]):
        arr_time (Union[Unset, GTITime]):
        dep_time (Union[Unset, GTITime]):
        arr_delay (Union[Unset, int]):
        dep_delay (Union[Unset, int]):
        extra (Union[Unset, bool]):
        cancelled (Union[Unset, bool]):
        attributes (Union[Unset, List[Attribute]]):
        platform (Union[Unset, str]):
        realtime_platform (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    combined_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    type: Union[Unset, JourneySDNameType] = JourneySDNameType.UNKNOWN
    coordinate: Union[Unset, Coordinate] = UNSET
    layer: Union[Unset, int] = UNSET
    tariff_details: Union[Unset, TariffDetails] = UNSET
    service_types: Union[Unset, List[str]] = UNSET
    has_station_information: Union[Unset, bool] = UNSET
    arr_time: Union[Unset, GTITime] = UNSET
    dep_time: Union[Unset, GTITime] = UNSET
    arr_delay: Union[Unset, int] = UNSET
    dep_delay: Union[Unset, int] = UNSET
    extra: Union[Unset, bool] = False
    cancelled: Union[Unset, bool] = False
    attributes: Union[Unset, List[Attribute]] = UNSET
    platform: Union[Unset, str] = UNSET
    realtime_platform: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        city = self.city
        combined_name = self.combined_name
        id = self.id
        global_id = self.global_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        coordinate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinate, Unset):
            coordinate = self.coordinate.to_dict()

        layer = self.layer
        tariff_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tariff_details, Unset):
            tariff_details = self.tariff_details.to_dict()

        service_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_types, Unset):
            service_types = self.service_types

        has_station_information = self.has_station_information
        arr_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arr_time, Unset):
            arr_time = self.arr_time.to_dict()

        dep_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dep_time, Unset):
            dep_time = self.dep_time.to_dict()

        arr_delay = self.arr_delay
        dep_delay = self.dep_delay
        extra = self.extra
        cancelled = self.cancelled
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        platform = self.platform
        realtime_platform = self.realtime_platform

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if combined_name is not UNSET:
            field_dict["combinedName"] = combined_name
        if id is not UNSET:
            field_dict["id"] = id
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if type is not UNSET:
            field_dict["type"] = type
        if coordinate is not UNSET:
            field_dict["coordinate"] = coordinate
        if layer is not UNSET:
            field_dict["layer"] = layer
        if tariff_details is not UNSET:
            field_dict["tariffDetails"] = tariff_details
        if service_types is not UNSET:
            field_dict["serviceTypes"] = service_types
        if has_station_information is not UNSET:
            field_dict["hasStationInformation"] = has_station_information
        if arr_time is not UNSET:
            field_dict["arrTime"] = arr_time
        if dep_time is not UNSET:
            field_dict["depTime"] = dep_time
        if arr_delay is not UNSET:
            field_dict["arrDelay"] = arr_delay
        if dep_delay is not UNSET:
            field_dict["depDelay"] = dep_delay
        if extra is not UNSET:
            field_dict["extra"] = extra
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if platform is not UNSET:
            field_dict["platform"] = platform
        if realtime_platform is not UNSET:
            field_dict["realtimePlatform"] = realtime_platform

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        city = d.pop("city", UNSET)

        combined_name = d.pop("combinedName", UNSET)

        id = d.pop("id", UNSET)

        global_id = d.pop("globalId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, JourneySDNameType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = JourneySDNameType(_type)

        _coordinate = d.pop("coordinate", UNSET)
        coordinate: Union[Unset, Coordinate]
        if isinstance(_coordinate, Unset):
            coordinate = UNSET
        else:
            coordinate = Coordinate.from_dict(_coordinate)

        layer = d.pop("layer", UNSET)

        _tariff_details = d.pop("tariffDetails", UNSET)
        tariff_details: Union[Unset, TariffDetails]
        if isinstance(_tariff_details, Unset):
            tariff_details = UNSET
        else:
            tariff_details = TariffDetails.from_dict(_tariff_details)

        service_types = cast(List[str], d.pop("serviceTypes", UNSET))

        has_station_information = d.pop("hasStationInformation", UNSET)

        _arr_time = d.pop("arrTime", UNSET)
        arr_time: Union[Unset, GTITime]
        if isinstance(_arr_time, Unset):
            arr_time = UNSET
        else:
            arr_time = GTITime.from_dict(_arr_time)

        _dep_time = d.pop("depTime", UNSET)
        dep_time: Union[Unset, GTITime]
        if isinstance(_dep_time, Unset):
            dep_time = UNSET
        else:
            dep_time = GTITime.from_dict(_dep_time)

        arr_delay = d.pop("arrDelay", UNSET)

        dep_delay = d.pop("depDelay", UNSET)

        extra = d.pop("extra", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        platform = d.pop("platform", UNSET)

        realtime_platform = d.pop("realtimePlatform", UNSET)

        journey_sd_name = cls(
            name=name,
            city=city,
            combined_name=combined_name,
            id=id,
            global_id=global_id,
            type=type,
            coordinate=coordinate,
            layer=layer,
            tariff_details=tariff_details,
            service_types=service_types,
            has_station_information=has_station_information,
            arr_time=arr_time,
            dep_time=dep_time,
            arr_delay=arr_delay,
            dep_delay=dep_delay,
            extra=extra,
            cancelled=cancelled,
            attributes=attributes,
            platform=platform,
            realtime_platform=realtime_platform,
        )

        journey_sd_name.additional_properties = d
        return journey_sd_name

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
