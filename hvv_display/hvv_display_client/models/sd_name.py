from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.coordinate import Coordinate
from ..models.sd_name_type import SDNameType
from ..models.tariff_details import TariffDetails
from ..types import UNSET, Unset

T = TypeVar("T", bound="SDName")


@attr.s(auto_attribs=True)
class SDName:
    """
    Attributes:
        name (Union[Unset, str]):
        city (Union[Unset, str]):
        combined_name (Union[Unset, str]):
        id (Union[Unset, str]):
        global_id (Union[Unset, str]):
        type (Union[Unset, SDNameType]):  Default: SDNameType.UNKNOWN.
        coordinate (Union[Unset, Coordinate]):
        layer (Union[Unset, int]):
        tariff_details (Union[Unset, TariffDetails]):
        service_types (Union[Unset, List[str]]):
        has_station_information (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    combined_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    type: Union[Unset, SDNameType] = SDNameType.UNKNOWN
    coordinate: Union[Unset, Coordinate] = UNSET
    layer: Union[Unset, int] = UNSET
    tariff_details: Union[Unset, TariffDetails] = UNSET
    service_types: Union[Unset, List[str]] = UNSET
    has_station_information: Union[Unset, bool] = UNSET
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
        type: Union[Unset, SDNameType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SDNameType(_type)

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

        sd_name = cls(
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
        )

        sd_name.additional_properties = d
        return sd_name

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
