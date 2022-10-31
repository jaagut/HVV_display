from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.coordinate import Coordinate
from ..models.station_list_entry_vehicle_types_item import (
    StationListEntryVehicleTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StationListEntry")


@attr.s(auto_attribs=True)
class StationListEntry:
    """
    Attributes:
        id (str):
        name (Union[Unset, str]):
        city (Union[Unset, str]):
        combined_name (Union[Unset, str]):
        shortcuts (Union[Unset, List[str]]):
        aliasses (Union[Unset, List[str]]):
        vehicle_types (Union[Unset, List[StationListEntryVehicleTypesItem]]):
        coordinate (Union[Unset, Coordinate]):
        exists (Union[Unset, bool]):  Default: True.
    """

    id: str
    name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    combined_name: Union[Unset, str] = UNSET
    shortcuts: Union[Unset, List[str]] = UNSET
    aliasses: Union[Unset, List[str]] = UNSET
    vehicle_types: Union[Unset, List[StationListEntryVehicleTypesItem]] = UNSET
    coordinate: Union[Unset, Coordinate] = UNSET
    exists: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        city = self.city
        combined_name = self.combined_name
        shortcuts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.shortcuts, Unset):
            shortcuts = self.shortcuts

        aliasses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aliasses, Unset):
            aliasses = self.aliasses

        vehicle_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vehicle_types, Unset):
            vehicle_types = []
            for vehicle_types_item_data in self.vehicle_types:
                vehicle_types_item = vehicle_types_item_data.value

                vehicle_types.append(vehicle_types_item)

        coordinate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinate, Unset):
            coordinate = self.coordinate.to_dict()

        exists = self.exists

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if combined_name is not UNSET:
            field_dict["combinedName"] = combined_name
        if shortcuts is not UNSET:
            field_dict["shortcuts"] = shortcuts
        if aliasses is not UNSET:
            field_dict["aliasses"] = aliasses
        if vehicle_types is not UNSET:
            field_dict["vehicleTypes"] = vehicle_types
        if coordinate is not UNSET:
            field_dict["coordinate"] = coordinate
        if exists is not UNSET:
            field_dict["exists"] = exists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        city = d.pop("city", UNSET)

        combined_name = d.pop("combinedName", UNSET)

        shortcuts = cast(List[str], d.pop("shortcuts", UNSET))

        aliasses = cast(List[str], d.pop("aliasses", UNSET))

        vehicle_types = []
        _vehicle_types = d.pop("vehicleTypes", UNSET)
        for vehicle_types_item_data in _vehicle_types or []:
            vehicle_types_item = StationListEntryVehicleTypesItem(
                vehicle_types_item_data
            )

            vehicle_types.append(vehicle_types_item)

        _coordinate = d.pop("coordinate", UNSET)
        coordinate: Union[Unset, Coordinate]
        if isinstance(_coordinate, Unset):
            coordinate = UNSET
        else:
            coordinate = Coordinate.from_dict(_coordinate)

        exists = d.pop("exists", UNSET)

        station_list_entry = cls(
            id=id,
            name=name,
            city=city,
            combined_name=combined_name,
            shortcuts=shortcuts,
            aliasses=aliasses,
            vehicle_types=vehicle_types,
            coordinate=coordinate,
            exists=exists,
        )

        station_list_entry.additional_properties = d
        return station_list_entry

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
