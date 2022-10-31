from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bounding_box import BoundingBox
from ..models.vehicle_map_request_coordinate_type import VehicleMapRequestCoordinateType
from ..models.vehicle_map_request_filter_type import VehicleMapRequestFilterType
from ..models.vehicle_map_request_vehicle_types_item import (
    VehicleMapRequestVehicleTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleMapRequest")


@attr.s(auto_attribs=True)
class VehicleMapRequest:
    """
    Attributes:
        bounding_box (BoundingBox):
        language (Union[Unset, str]):  Default: 'de'.
        version (Union[Unset, int]):  Default: 1.
        filter_type (Union[Unset, VehicleMapRequestFilterType]):  Default: VehicleMapRequestFilterType.NO_FILTER.
        period_begin (Union[Unset, int]):
        period_end (Union[Unset, int]):
        without_coords (Union[Unset, bool]):
        coordinate_type (Union[Unset, VehicleMapRequestCoordinateType]):  Default:
            VehicleMapRequestCoordinateType.EPSG_4326.
        vehicle_types (Union[Unset, List[VehicleMapRequestVehicleTypesItem]]):
        realtime (Union[Unset, bool]):
    """

    bounding_box: BoundingBox
    language: Union[Unset, str] = "de"
    version: Union[Unset, int] = 1
    filter_type: Union[
        Unset, VehicleMapRequestFilterType
    ] = VehicleMapRequestFilterType.NO_FILTER
    period_begin: Union[Unset, int] = UNSET
    period_end: Union[Unset, int] = UNSET
    without_coords: Union[Unset, bool] = UNSET
    coordinate_type: Union[
        Unset, VehicleMapRequestCoordinateType
    ] = VehicleMapRequestCoordinateType.EPSG_4326
    vehicle_types: Union[Unset, List[VehicleMapRequestVehicleTypesItem]] = UNSET
    realtime: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bounding_box = self.bounding_box.to_dict()

        language = self.language
        version = self.version
        filter_type: Union[Unset, str] = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type.value

        period_begin = self.period_begin
        period_end = self.period_end
        without_coords = self.without_coords
        coordinate_type: Union[Unset, str] = UNSET
        if not isinstance(self.coordinate_type, Unset):
            coordinate_type = self.coordinate_type.value

        vehicle_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vehicle_types, Unset):
            vehicle_types = []
            for vehicle_types_item_data in self.vehicle_types:
                vehicle_types_item = vehicle_types_item_data.value

                vehicle_types.append(vehicle_types_item)

        realtime = self.realtime

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boundingBox": bounding_box,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if version is not UNSET:
            field_dict["version"] = version
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type
        if period_begin is not UNSET:
            field_dict["periodBegin"] = period_begin
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if without_coords is not UNSET:
            field_dict["withoutCoords"] = without_coords
        if coordinate_type is not UNSET:
            field_dict["coordinateType"] = coordinate_type
        if vehicle_types is not UNSET:
            field_dict["vehicleTypes"] = vehicle_types
        if realtime is not UNSET:
            field_dict["realtime"] = realtime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bounding_box = BoundingBox.from_dict(d.pop("boundingBox"))

        language = d.pop("language", UNSET)

        version = d.pop("version", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: Union[Unset, VehicleMapRequestFilterType]
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = VehicleMapRequestFilterType(_filter_type)

        period_begin = d.pop("periodBegin", UNSET)

        period_end = d.pop("periodEnd", UNSET)

        without_coords = d.pop("withoutCoords", UNSET)

        _coordinate_type = d.pop("coordinateType", UNSET)
        coordinate_type: Union[Unset, VehicleMapRequestCoordinateType]
        if isinstance(_coordinate_type, Unset):
            coordinate_type = UNSET
        else:
            coordinate_type = VehicleMapRequestCoordinateType(_coordinate_type)

        vehicle_types = []
        _vehicle_types = d.pop("vehicleTypes", UNSET)
        for vehicle_types_item_data in _vehicle_types or []:
            vehicle_types_item = VehicleMapRequestVehicleTypesItem(
                vehicle_types_item_data
            )

            vehicle_types.append(vehicle_types_item)

        realtime = d.pop("realtime", UNSET)

        vehicle_map_request = cls(
            bounding_box=bounding_box,
            language=language,
            version=version,
            filter_type=filter_type,
            period_begin=period_begin,
            period_end=period_end,
            without_coords=without_coords,
            coordinate_type=coordinate_type,
            vehicle_types=vehicle_types,
            realtime=realtime,
        )

        vehicle_map_request.additional_properties = d
        return vehicle_map_request

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
