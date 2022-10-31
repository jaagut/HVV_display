from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.service_type import ServiceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Service")


@attr.s(auto_attribs=True)
class Service:
    """
    Attributes:
        name (str):
        type (ServiceType):
        direction (Union[Unset, str]):
        direction_id (Union[Unset, int]):
        origin (Union[Unset, str]):
        id (Union[Unset, str]):
        dlid (Union[Unset, str]):
        carrier_name_short (Union[Unset, str]):
        carrier_name_long (Union[Unset, str]):
    """

    name: str
    type: ServiceType
    direction: Union[Unset, str] = UNSET
    direction_id: Union[Unset, int] = UNSET
    origin: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    dlid: Union[Unset, str] = UNSET
    carrier_name_short: Union[Unset, str] = UNSET
    carrier_name_long: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.to_dict()

        direction = self.direction
        direction_id = self.direction_id
        origin = self.origin
        id = self.id
        dlid = self.dlid
        carrier_name_short = self.carrier_name_short
        carrier_name_long = self.carrier_name_long

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if direction_id is not UNSET:
            field_dict["directionId"] = direction_id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if id is not UNSET:
            field_dict["id"] = id
        if dlid is not UNSET:
            field_dict["dlid"] = dlid
        if carrier_name_short is not UNSET:
            field_dict["carrierNameShort"] = carrier_name_short
        if carrier_name_long is not UNSET:
            field_dict["carrierNameLong"] = carrier_name_long

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = ServiceType.from_dict(d.pop("type"))

        direction = d.pop("direction", UNSET)

        direction_id = d.pop("directionId", UNSET)

        origin = d.pop("origin", UNSET)

        id = d.pop("id", UNSET)

        dlid = d.pop("dlid", UNSET)

        carrier_name_short = d.pop("carrierNameShort", UNSET)

        carrier_name_long = d.pop("carrierNameLong", UNSET)

        service = cls(
            name=name,
            type=type,
            direction=direction,
            direction_id=direction_id,
            origin=origin,
            id=id,
            dlid=dlid,
            carrier_name_short=carrier_name_short,
            carrier_name_long=carrier_name_long,
        )

        service.additional_properties = d
        return service

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
